# 📓 Project Development Log (Changelog)

This document tracks the iterative development of the Purple Team & DFIR Automation Framework, detailing offensive and defensive capabilities engineered throughout the project lifecycle.

---

<details>
<summary><b>Day 6: Windows Internals, Hardening & EVTX Forensics</b></summary>
<br>

* **DevSecOps:** Configured WinRM and provisioned Windows 10 Enterprise via Ansible. Implemented declarative GPO bypasses for BitLocker without TPM, enforced strict password policies, and configured Advanced Audit Policies.
* **Offensive:** Developed a PowerShell APT framework simulating Defense Evasion (Firewall rule masquerading) and Persistence (Scheduled Tasks with Base64-encoded reverse shell beacons) bypassing standard UAC.
* **DFIR:** Exported and parsed raw `Security.evtx` logs using Python (`python-evtx`). Built a custom Threat Hunter to detect LOLBAS execution (Event ID 4688) and malicious Firewall modifications (Event ID 4946). Successfully filtered 130+ False Positives using an internal whitelist.
</details>

<details>
<summary><b>Day 5: Linux Enterprise Hardening, Auditd & Persistence</b></summary>
<br>

* **DevSecOps:** Implemented declarative Linux hardening via Ansible. Enforced strict Discretionary Access Control (DAC) with `0770` permissions, SSH PubKey-only authentication, and `iptables` default `DROP` policies for egress/ingress filtering.
* **Blue Team:** Deployed and configured `auditd` to monitor critical file access (`/etc/shadow`, `authorized_keys`) and track privilege escalation syscalls (`fchmodat`, `execve`) at the kernel level.
* **Offensive:** Developed a Python Auto-Pwn framework simulating APT persistence techniques, including recursive SSH Authorized Keys injection and malicious System Cron (`/etc/cron.d`) beaconing.
* **DFIR:** Built Python parsers to extract anomalies from raw `audit.log` and hunt for persistence mechanisms across `cron` and `systemd`. Integrated with the Telegram API for instant SOAR alerting and Executive Markdown report generation.
</details>

<details>
<summary><b>Day 4: Packet Investigation & TCP Stream Carving</b></summary>
<br>

* **Offensive:** Engineered raw socket SMBv3 crafting (Negotiate Protocol Request) to trigger NTA sensors, and developed a Base64-obfuscated Reverse Shell generator to bypass Egress filters.
* **DFIR:** Automated TCP Stream Reassembly and Endianness (Little-Endian/Big-Endian) parsing from raw PCAP dumps using `pyshark` to reconstruct interactive Command & Control (C2) sessions.
</details>

<details>
<summary><b>Day 3: Advanced Routing, VLANs, OSPF & HSRP</b></summary>
<br>

* **Offensive:** Crafted advanced Scapy modules for 802.1Q Double Tagging (VLAN Hopping) into isolated networks and HSRP State Hijacking (Coup d'état) via Multicast spoofing.
* **DevSecOps:** Hardened L2/L3 infrastructure topologies using Ansible by disabling DTP, isolating native VLANs, and enforcing OSPF MD5 and HSRP cryptographic authentication.
* **DFIR:** Developed memory-optimized PCAP parsers (`PcapReader`) to detect Plaintext/Null OSPF protocols and unauthorized HSRP State Changes.
</details>

<details>
<summary><b>Day 2: Routing, Naming Services & DHCP Attacks</b></summary>
<br>

* **Offensive:** Simulated L2 Denial of Service via automated DHCP Starvation (MAC spoofing) and Rogue DHCP deployment to intercept target traffic.
* **DFIR:** Engineered an automated SSH log auditor (`auth.log`) with Regex parsing and built-in Threat Intelligence enrichment via the AbuseIPDB API for brute-force detection. Built a PCAP hunter using MAC whitelisting.
</details>

<details>
<summary><b>Day 1: L2/L3 Network Architecture & Covert Channels</b></summary>
<br>

* **Offensive:** Developed Docker-compatible ARP Poisoning (MitM) modules with L2 encapsulation and L3 Exfiltration scripts hiding XOR-encrypted and Base64-encoded payloads inside ICMP Echo Requests (Beaconing with Jitter).
* **DFIR:** Wrote Python decryptors to carve, decode, and decrypt exfiltrated data from intercepted network traffic, successfully restoring compromised files.
</details>