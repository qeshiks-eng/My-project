#!/usr/bin/env python3
"""
DFIR Tool: Windows Security Event Log (EVTX) Parser.
Parses raw .evtx dumps to identify anomalous Process Creations (Event ID 4688)
and Firewall Modifications (Event ID 4946), detecting LOLBAS techniques.

Author: 18ilya99
Role: SOC Analyst / Incident Responder
"""

import argparse
import sys
import os
import xml.etree.ElementTree as ET
from typing import List, Dict

try:
    from Evtx.Evtx import Evtx
except ImportError:
    sys.exit("[-] Critical Error: 'python-evtx' module not found. Run: pip3 install python-evtx --break-system-packages")

# Microsoft Event XML Namespace
NS = "{http://schemas.microsoft.com/win/2004/08/events/event}"

def parse_evtx(evtx_path: str) -> List[Dict[str, str]]:
    """
    Reads a Windows .evtx file, parses the XML of each record, and extracts IoCs.
    """
    alerts = []
    
    if not os.path.isfile(evtx_path):
        print(f"[-] Error: File '{evtx_path}' not found.")
        return alerts

    print(f"[*] Starting DFIR EVTX Analysis on: {evtx_path}")

    try:
        with Evtx(evtx_path) as log:
            for record in log.records():
                xml_str = record.xml()
                root = ET.fromstring(xml_str)
                
                # Extract EventID
                event_id_elem = root.find(f".//{NS}EventID")
                if event_id_elem is None: 
                    continue
                
                event_id = event_id_elem.text
                
                # 1. Detect Firewall Rule Changes (Event ID 4946)
                if event_id == "4946":
                    rule_name = "Unknown"
                    for data in root.findall(f".//{NS}Data"):
                        if data.get("Name") == "RuleName": 
                            rule_name = data.text
                            break
                    
                    alerts.append({
                        "type": "Firewall", 
                        "id": "4946", 
                        "details": rule_name
                    })

                # 2. Detect Suspicious Process Creation (Event ID 4688) & LOLBAS Hunting
                elif event_id == "4688":
                    cmdline = "Unknown"
                    process_name = "Unknown"
                    
                    for data in root.findall(f".//{NS}Data"):
                        if data.get("Name") == "CommandLine": 
                            cmdline = data.text or ""
                        elif data.get("Name") == "NewProcessName": 
                            process_name = data.text or ""
                    
                    # LOLBAS Threat Hunting Logic (Regex/String matching)
                    suspicious_flags = ["-enc", "-encodedcommand", "bypass", "hidden", "schtasks"]
                    
                    if cmdline and any(flag in cmdline.lower() for flag in suspicious_flags):
                        alerts.append({
                            "type": "LOLBAS", 
                            "id": "4688", 
                            "details": f"{process_name} | {cmdline}"
                        })

    except Exception as e:
        print(f"[-] Error parsing EVTX: {e}")
        
    return alerts


def main() -> None:
    parser = argparse.ArgumentParser(description="Advanced DFIR EVTX Parser")
    parser.add_argument("-f", "--file", required=True, type=str, help="Path to the Security.evtx dump")
    
    args = parser.parse_args()
    alerts = parse_evtx(args.file)
    
    # Standalone execution output
    if alerts:
        print("-" * 60)
        for a in alerts:
            print(f"[!] SOC ALERT [{a['type']}] (Event ID {a['id']}): {a['details']}")
        print("-" * 60)
        print(f"[!] Total raw anomalies found: {len(alerts)}")
    else:
        print("[+] Log analysis complete. No specific anomalies found.")


if __name__ == "__main__":
    main()