#!/usr/bin/env python3
"""
DFIR Tool: Persistence Mechanisms Hunter.
Scans cron directories and systemd paths for suspicious reverse shells, 
downloaders, or obfuscated payloads commonly used by APTs.

Author: 18ilya99
Role: SOC Analyst / Incident Responder
"""

import os
import re
import argparse
from typing import List, Dict, Optional

# Patterns: C2 Beacons, Reverse Shells, Base64
SUSPICIOUS_PATTERN = re.compile(r'(curl|wget|bash\s+-i|/dev/tcp/|nc\s+-e|base64)', re.IGNORECASE)

PERSISTENCE_DIRS =[
    '/etc/cron.d',
    '/etc/cron.daily',
    '/etc/cron.hourly',
    '/etc/cron.monthly',
    '/etc/cron.weekly',
    '/var/spool/cron/crontabs',
    '/etc/systemd/system',
    '/usr/lib/systemd/system'
]

def scan_persistence() -> Optional[List[Dict[str, str]]]:
    """
    Iterates over known persistence locations and scans for malicious regex patterns.
    """
    print("[*] Starting Threat Hunt for Cron & Systemd Persistence...")
    incidents =[]

    for p_dir in PERSISTENCE_DIRS:
        if not os.path.exists(p_dir):
            continue

        for root, _, files in os.walk(p_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            if SUSPICIOUS_PATTERN.search(line):
                                print(f"[!!!] SOC ALERT: Suspicious Persistence Found!")
                                print(f"      File: {file_path}")
                                print(f"      Line: {line.strip()}")
                                
                                incidents.append({
                                    "file": file_path,
                                    "line": str(line_num),
                                    "content": line.strip()
                                })
                except PermissionError:
                    pass
                except Exception as e:
                    print(f"[-] Failed to read {file_path}: {e}")

    if not incidents:
        print("[+] System appears clean. No suspicious persistence mechanisms found.")
    
    return incidents

def main() -> None:
    # Adding argparse just to keep interface consistency
    parser = argparse.ArgumentParser(description="Cron and Systemd Persistence Hunter")
    parser.parse_args()
    scan_persistence()

if __name__ == "__main__":
    main()