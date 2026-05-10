#!/usr/bin/env python3
"""
DFIR Tool: Auditd Log Parser.
Parses raw /var/log/audit/audit.log to identify unauthorized file modifications
and suspicious privilege escalations (SUID usage).

Author: 18ilya99
Role: SOC Analyst / Incident Responder
"""

import re
import argparse
import sys
import os
from typing import List, Dict, Optional

# Regex to extract key fields from auditd SYSCALL and PATH logs
SYSCALL_PATTERN = re.compile(r'type=SYSCALL.*?auid=(?P<auid>4294967295|-1|\d+).*?pid=(?P<pid>\d+).*?exe="(?P<exe>[^"]+)"')
PATH_PATTERN = re.compile(r'type=PATH.*?name="(?P<path>[^"]+)"')

CRITICAL_PATHS =["/etc/shadow", ".ssh/authorized_keys", "/etc/sudoers"]
SUSPICIOUS_EXES =["/usr/bin/chmod", "/bin/chmod", "/usr/bin/chown"]

def parse_audit_log(log_path: str) -> Optional[List[Dict[str, str]]]:
    """
    Scans the auditd log for malicious activities.
    """
    print(f"[*] Starting Auditd Log Forensics on: {log_path}")
    
    if not os.path.isfile(log_path):
        print(f"[-] Error: Log file '{log_path}' not found. Run with sudo.")
        return None

    incidents =[]

    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
            for i, line in enumerate(lines):
                # 1. Look for Syscalls changing permissions
                if "type=SYSCALL" in line:
                    match = SYSCALL_PATTERN.search(line)
                    if match:
                        data = match.groupdict()
                        auid = data['auid']
                        
                        # Trigger: chmod usage OR any monitored syscall by a real user (auid >= 1000)
                        if data['exe'] in SUSPICIOUS_EXES or (auid.isdigit() and int(auid) >= 1000):
                            incident = {
                                "type": "Suspicious Syscall",
                                "pid": data['pid'],
                                "auid": auid,
                                "exe": data['exe'],
                                "target": "Unknown"
                            }
                            
                            # Peek ahead for the PATH record associated with this syscall
                            if i + 1 < len(lines) and "type=PATH" in lines[i+1]:
                                path_match = PATH_PATTERN.search(lines[i+1])
                                if path_match:
                                    incident["target"] = path_match.group('path')
                            
                            incidents.append(incident)
                            print(f"[!!!] SOC ALERT: Suspicious Executable Run | AUID: {auid} | EXE: {data['exe']} | Target: {incident['target']}")
                
                # 2. Direct matches against critical files
                if any(path in line for path in CRITICAL_PATHS) and "type=PATH" in line:
                    path_match = PATH_PATTERN.search(line)
                    if path_match:
                        target = path_match.group('path')
                        incidents.append({"type": "Critical File Access", "pid": "N/A", "auid": "N/A", "exe": "N/A", "target": target})
                        print(f"[!!!] SOC ALERT: Critical File Accessed | Target: {target}")

    except PermissionError:
        print("[-] Permission Denied. You must run this script as root to read audit.log.")
        return None
    except Exception as e:
        print(f"[-] Critical parsing error: {e}")
        return None

    if not incidents:
        print("[+] No malicious activities found in audit logs.")
    
    return incidents

def main() -> None:
    parser = argparse.ArgumentParser(description="Auditd Log Forensics Parser")
    parser.add_argument("-l", "--log", default="/var/log/audit/audit.log", help="Path to audit.log")
    args = parser.parse_args()
    parse_audit_log(args.log)

if __name__ == "__main__":
    main()