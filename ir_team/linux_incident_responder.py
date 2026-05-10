#!/usr/bin/env python3
"""
DFIR Master Orchestrator: Linux Host Compromise.
Aggregates logs from auditd and persistence hunters, generates an Executive Report,
and triggers SOAR alerts via Telegram.

Author: 18ilya99
Role: SOC Analyst / Incident Responder
"""

import argparse
import datetime
import os
import sys
import requests
import socket
from typing import Optional

# Correctly importing Python modules instead of using subprocess
try:
    from auditd_parser import parse_audit_log
    from persistence_hunter import scan_persistence
except ImportError as e:
    print(f"[-] Import Error: {e}. Ensure all modules are in the same directory.")
    sys.exit(1)


def send_telegram_alert(message: str, token: str, chat_id: str) -> None:
    """Sends incident alert to SOC Telegram channel."""
    print("[*] Triggering SOAR Telegram Alert...")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        print("[+] Alert successfully dispatched.")
    except Exception as e:
        print(f"[-] Telegram API Error: {e}")


def generate_report(log_path: str, output_dir: str, bot_token: Optional[str], chat_id: Optional[str]) -> None:
    """Orchestrates DFIR scripts and generates Markdown report."""
    print("[*] Initializing Master Linux DFIR Orchestrator...")
    print("-" * 50)
    
    # Run sub-modules
    audit_results = parse_audit_log(log_path)
    print("-" * 50)
    cron_results = scan_persistence()
    print("-" * 50)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = os.path.join(output_dir, f"Linux_Compromise_Report_{timestamp}.md")
    hostname = socket.gethostname()
    
    incident_active = bool(audit_results or cron_results)

    # Markdown Generation
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🛡️ DFIR Incident Report: Linux Host Compromise\n\n")
            f.write(f"**Host:** `{hostname}`\n")
            f.write(f"**Generated:** `{datetime.datetime.now().isoformat()}`\n\n")
            f.write("---\n\n")
            
            f.write("## 1. Auditd Subsystem Anomalies\n")
            if audit_results:
                f.write("🚨 **CRITICAL: Unauthorized File Access / Syscalls Detected!**\n\n")
                f.write("| AUID | PID | Executable | Target File |\n")
                f.write("|------|-----|------------|-------------|\n")
                for res in audit_results:
                    f.write(f"| `{res['auid']}` | {res['pid']} | `{res['exe']}` | `{res['target']}` |\n")
                f.write("\n> **Mitigation:** Revoke SSH keys, inspect identified binaries, and restore file permissions.\n\n")
            else:
                f.write("✅ **Status:** Clean. No anomalies in auditd logs.\n\n")

            f.write("## 2. Persistence Mechanisms (Cron/Systemd)\n")
            if cron_results:
                f.write("🚨 **CRITICAL: Suspicious Persistence Found!**\n\n")
                for res in cron_results:
                    f.write(f"- **File:** `{res['file']}` (Line {res['line']})\n")
                    f.write(f"  - **Payload:** `{res['content']}`\n")
                f.write("\n> **Mitigation:** Remove malicious files, kill active C2 connections, block target IPs on NGFW.\n")
            else:
                f.write("✅ **Status:** Clean. No backdoors found in scheduled tasks.\n")

        print(f"[+] Incident Report saved to: {os.path.abspath(report_filename)}")

        # SOAR Alert
        if incident_active and bot_token and chat_id:
            alert_msg = (f"🚨 *SOC ALERT: Linux Compromise Detected!*\n"
                         f"Host: `{hostname}`\n"
                         f"Audit Anomalies: {len(audit_results) if audit_results else 0}\n"
                         f"Persistence Found: {len(cron_results) if cron_results else 0}\n"
                         f"Check report: `{os.path.basename(report_filename)}`")
            send_telegram_alert(alert_msg, bot_token, chat_id)

    except PermissionError:
        print(f"[-] Permission Denied. Cannot write report to {output_dir}")
    except Exception as e:
        print(f"[-] Report Generation Error: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Master DFIR Orchestrator: Linux Server Compromise")
    parser.add_argument("-l", "--log", type=str, default="/var/log/audit/audit.log", help="Path to audit.log")
    parser.add_argument("-o", "--output", type=str, default=".", help="Output directory for the report")
    parser.add_argument("--telegram-token", type=str, help="Telegram Bot Token")
    parser.add_argument("--telegram-chat", type=str, help="Telegram Chat ID")
    
    args = parser.parse_args()
    generate_report(args.log, args.output, args.telegram_token, args.telegram_chat)

if __name__ == "__main__":
    main()