#!/usr/bin/env python3
"""
Automated DFIR Analyzer (Digital Forensics and Incident Response).
Reconstructs Base64 chunks from exfiltrated C2 traffic, decrypts XOR, 
and restores the original compromised file.

Author: 18ilya99
Role: SOC Analyst / Incident Responder
"""

import base64
import sys
import argparse

def xor_decrypt(data: bytes, key: int) -> bytes:
    """
    Decrypts byte array using a single-byte XOR key.
    (A ^ B) ^ B = A
    """
    return bytearray([b ^ key for b in data])

def process_chunks(chunks_file: str, output_file: str, xor_key: int):
    """
    Reads extracted Base64 chunks, decodes and decrypts them,
    and writes the restored original file to disk.
    """
    try:
        with open(chunks_file, "r") as f:
            # Читаем строки, убираем префиксы "[+] Sent chunk..." и оставляем только Base64
            b64_lines =[]
            for line in f:
                if "WEV" in line or "Q0" in line or ":" in line:
                    # Извлекаем только Base64 часть после двоеточия
                    b64_part = line.split(":")[-1].strip()
                    if b64_part:
                        b64_lines.append(b64_part)
                        
        if not b64_lines:
            print("[-] Error: No valid Base64 chunks found in the input file.")
            sys.exit(1)
            
        full_b64 = "".join(b64_lines)
        print(f"[*] Successfully extracted {len(b64_lines)} chunks.")
        
        print("[*] Decoding Base64 payload...")
        encrypted_data = base64.b64decode(full_b64)
        
        print(f"[*] Decrypting with XOR key ({xor_key})...")
        decrypted_data = xor_decrypt(encrypted_data, xor_key)
        
        with open(output_file, "wb") as out_f:
            out_f.write(decrypted_data)
            
        print(f"\n[+] Incident Response Complete!")
        print(f"[+] Restored file saved to: {output_file}")
        
        print("\n--- COMPROMISED DATA PREVIEW (First 250 bytes) ---")
        # Выводим начало файла, игнорируя символы, которые не удалось декодировать
        print(decrypted_data.decode('utf-8', errors='ignore')[:250] + "...\n")
        print("--------------------------------------------------")

    except Exception as e:
        print(f"[-] DFIR Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="DFIR Tool: ICMP Covert Channel Payload Extractor")
    parser.add_argument("-i", "--input", required=True, help="Text file containing intercepted chunks")
    parser.add_argument("-o", "--output", required=True, help="Path to save the restored file")
    parser.add_argument("-k", "--key", type=int, default=42, help="XOR decryption key (default: 42)")
    
    args = parser.parse_args()
    process_chunks(args.input, args.output, args.key)

if __name__ == "__main__":
    main()