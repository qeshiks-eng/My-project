#!/usr/bin/env python3
"""
DFIR Master Orchestrator: Windows Endpoint Compromise.
Correlates parsed EVTX logs, filters out False Positives (UWP apps, Skype, Xbox),
generates an Executive Markdown Report, and triggers SOAR Telegram alerts.

Author: 18ilya99
Role: SOC Analyst / Incident Responder
"""

import argparse
import datetime
import os
import sys
import requests
from typing import Optional

try:
    from evtx_parser import parse_evtx
except ImportError:
    sys.exit("[-] Import Error: 'evtx_parser.py' not found in the current directory.")

# Enterprise Whitelist: Ignore standard Windows UWP noise
WHITELIST = ["skype", "game bar", "microsoft.", "xbox", "onenote", "solitaire"]


def is_false_positive(details: str) -> bool:
    """
    Checks if the alert matches known benign Windows noise.
    """
    details_lower = details.lower()
    return any(noise in details_lower for noise in WHITELIST)


def send_telegram_alert(message: str, token: str, chat_id: str) -> None:
    """
    Triggers a SOAR alert via the Telegram API.
    """
    print("[*] Dispatching Telegram SOAR Alert...")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    try:
        response = requests.post(
            url, 
            json={"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}, 
            timeout=5
        )
        response.raise_for_status()
        print("[+] Alert sent successfully.")
    except Exception as e:
        print(f"[-] Telegram API Error: {e}")


def generate_report(evtx_path: str, output_dir: str, bot_token: Optional[str] = None, chat_id: Optional[str] = None) -> None:
    """
    Orchestrates the DFIR workflow, filters alerts, and generates the final report.
    """
    print("[*] Initializing Windows Master DFIR Orchestrator...")
    print("-" * 60)
    
    # 1. Parse raw EVTX
    raw_alerts = parse_evtx(evtx_path)
    
    # 2. Filtering Logic (Tuning)
    true_positives = []
    false_positives_count = 0
    
    for alert in raw_alerts:
        # We only whitelist Firewall rules. LOLBAS process executions are always treated as True Positives.
        if alert["type"] == "Firewall" and is_false_positive(alert["details"]):
            false_positives_count += 1
        else:
            true_positives.append(alert)

    print(f"[*] Analysis Complete. Filtered out {false_positives_count} False Positives.")
    print(f"[!] True Positives (Confirmed IoCs): {len(true_positives)}")
    print("-" * 60)

    # 3. Markdown Generation
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = os.path.join(output_dir, f"Windows_Compromise_Report_{timestamp}.md")
    
    try:
        with open(report_file, "w", encoding="utf-8") as f:
            f.write("# 🛡️ DFIR Incident Report: Windows APT Compromise\n\n")
            f.write(f"**Generated:** `{datetime.datetime.now().isoformat()}`\n")
            f.write(f"**Analyzed Log:** `{os.path.abspath(evtx_path)}`\n\n")
            f.write("---\n\n")
            
            f.write("## 1. Validated Indicators of Compromise (IoCs)\n\n")
            if true_positives:
                for tp in true_positives:
                    if tp["type"] == "LOLBAS":
                        f.write(f"🚨 **CRITICAL (Event 4688): LOLBAS Execution Detected!**\n")
                        f.write(f"- Command: `{tp['details']}`\n\n")
                    elif tp["type"] == "Firewall":
                        f.write(f"⚠️ **WARNING (Event 4946): Suspicious Firewall Rule Creation**\n")
                        f.write(f"- Rule Name: `{tp['details']}`\n\n")
                
                f.write("> **Mitigation:** Isolate host from the network. Investigate the parent process of PowerShell. Check Task Scheduler for persistence.\n")
            else:
                f.write("✅ **Status:** Clean. No confirmed anomalies.\n")
                
        print(f"[+] Report generated: {os.path.abspath(report_file)}")

        # 4. SOAR Integration
        if true_positives and bot_token and chat_id:
            msg = (f"🚨 *SOC ALERT: Windows Host Compromised!*\n"
                   f"Alerts: {len(true_positives)}\n"
                   f"Report: `{os.path.basename(report_file)}`")
            send_telegram_alert(msg, bot_token, chat_id)

    except PermissionError:
        print(f"[-] Permission Denied. Cannot write report to {output_dir}")
    except Exception as e:
        print(f"[-] Report Generation Error: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advanced Windows Incident Responder & Orchestrator")
    parser.add_argument("-f", "--file", required=True, type=str, help="Path to Security.evtx dump")
    parser.add_argument("-o", "--output", type=str, default=".", help="Output directory for the report")
    parser.add_argument("--telegram-token", type=str, help="Telegram Bot Token for SOAR alerts (Optional)")
    parser.add_argument("--telegram-chat", type=str, help="Telegram Chat ID for SOAR alerts (Optional)")
    
    args = parser.parse_args()
    
    generate_report(args.file, args.output, args.telegram_token, args.telegram_chat)


if __name__ == "__main__":
    main()