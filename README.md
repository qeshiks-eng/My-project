# 🛡️ Purple Team & DFIR Automation Framework

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Ansible](https://img.shields.io/badge/Ansible-Automation-red.svg)
![Suricata](https://img.shields.io/badge/Suricata-IDS%2FIPS-orange.svg)
![Wireshark](https://img.shields.io/badge/Wireshark-Network_Forensics-1679A7.svg)
![Linux](https://img.shields.io/badge/Linux-Enterprise_Hardening-yellow.svg)

## 📖 Executive Summary
A comprehensive cybersecurity framework simulating the full lifecycle of Advanced Persistent Threats (APTs) in Enterprise networks. This project is divided into three core domains: **DevSecOps (Infrastructure Provisioning & Hardening)**, **Offensive Security (Red Team)**, and **Digital Forensics & Incident Response (DFIR)**.

The framework demonstrates practical implementation of L2-L7 network attacks, automated mitigation strategies, and SOAR (Security Orchestration, Automation, and Response) capabilities.

## 🏗️ Repository Architecture

```text
my-security-portfolio/
├── infrastructure/        # IaC, Ansible roles, and configuration baselines
├── blue_team/             # IDS signatures (Suricata), YARA rules, defensive configs
├── red_team/              # Offensive Python tooling (Scapy, Raw Sockets, C2)
├── ir_team/               # Automated DFIR parsers, Log analyzers, SOAR integrations
├── logs/                  # PCAP dumps, extracted artifacts, and raw logs (Gitignored)
└── docs/                  # Security policies and architectural documentation
🔐 Core Domains
1. Offensive Security (GReAT / Red Team)
L2/L3 Network Attacks: Custom Scapy scripts for ARP Poisoning, DHCP Starvation, Rogue DHCP, and VLAN Hopping (Double Tagging).
Routing Protocol Hijacking: OSPF LSA spoofing and HSRP Active-Router Hijacking (Coup d'état) via Multicast manipulation.
Covert Channels & Evasion: L3 data exfiltration using single-byte XOR, Base64, and randomized beaconing delays (Jitter) over ICMP. Reverse Shell generation bypassing Egress filtering.
Endpoint Compromise: Automated Linux persistence deployment (Cron Backdoors, SSH Authorized Keys injection).
2. DevSecOps & Blue Team
Infrastructure as Code: Declarative hardening via Ansible playbooks.
Network Defense: Implementation of Port Security, DHCP Snooping, BPDU Guard, DTP disabling, and OSPF/HSRP MD5 authentication.
Endpoint Hardening: Strict DAC isolation, sshd hardening, and iptables default DROP policies (Egress/Ingress filtering).
Detection Engineering: Custom Suricata IDS rules targeting plaintext routing protocols, malicious ICMP payloads, and Reverse Shell TCP streams.
3. DFIR & Threat Hunting
Network Forensics: Memory-optimized PCAP parsers (via pyshark and scapy) for TCP Stream Reassembly, SMB Endianness extraction, and Rogue DHCP identification.
Host-Based Forensics: Low-level syscall monitoring via auditd (fchmodat, execve) and regular expression-based Threat Hunting across cron and systemd.
SOAR Integration: Automated correlation orchestrators with Threat Intelligence API enrichment (AbuseIPDB) and instant Telegram alerting.
📓 Project Development Log (Changelog)
<details>
<summary><b>Day 5: Linux Enterprise Hardening, Auditd & Persistence</b></summary>
<br>
DevSecOps: Declarative Linux hardening via Ansible. Enforced strict DAC (0770 permissions), SSH PubKey-only authentication, and iptables DROP policies.
Blue Team: Deployed and configured auditd to monitor critical file access and privilege escalation syscalls at the kernel level.
Offensive: Developed a Python Auto-Pwn framework simulating APT persistence (SSH Authorized Keys injection, malicious System Cron beacons).
DFIR: Built Python parsers to extract anomalies from raw audit.log and hunt for persistence mechanisms across cron and systemd. Integrated with Telegram API for instant SOAR alerting.
</details>
<details>
<summary><b>Day 4: Packet Investigation & TCP Stream Carving</b></summary>
<br>
Offensive: Implemented raw socket SMBv3 crafting (Negotiate Protocol Request) and Base64 Reverse Shell generation bypassing Egress filters.
DFIR: Automated TCP Stream Reassembly and Endianness (Little-Endian/Big-Endian) parsing from raw PCAP dumps using PyShark to reconstruct interactive C2 sessions.
</details>
<details>
<summary><b>Day 3: Advanced Routing, VLANs, OSPF & HSRP</b></summary>
<br>
Offensive: Crafted Scapy modules for 802.1Q Double Tagging (VLAN Hopping) and HSRP State Hijacking via Multicast spoofing.
DevSecOps: Hardened L2/L3 topology using Ansible (disabled DTP, enforced OSPF MD5 and HSRP authentication).
DFIR: Developed memory-optimized PCAP parsers to detect Plaintext OSPF protocols and unauthorized HSRP State Changes.
</details>
<details>
<summary><b>Day 2: Routing, Naming Services & DHCP Attacks</b></summary>
<br>
Offensive: Simulated L2 Denial of Service via DHCP Starvation (MAC spoofing) and Rogue DHCP deployment.
DFIR: Engineered an automated SSH log auditor (auth.log) with Threat Intelligence enrichment via the AbuseIPDB API for brute-force detection. Built a PCAP hunter using MAC whitelisting.
</details>
<details>
<summary><b>Day 1: L2/L3 Network Architecture & Covert Channels</b></summary>
<br>
Offensive: Developed Docker-compatible ARP Poisoning modules and L3 Exfiltration scripts hiding encrypted payload inside ICMP Echo Requests.
DFIR: Wrote Python decryptors to carve, Base64-decode, and XOR-decrypt exfiltrated data from intercepted network traffic.
</details>
```