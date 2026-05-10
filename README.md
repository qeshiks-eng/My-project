# 🛡️ Purple Team & DFIR Automation Framework

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Ansible](https://img.shields.io/badge/Ansible-Automation-red.svg)
![Suricata](https://img.shields.io/badge/Suricata-IDS%2FIPS-orange.svg)
![Wireshark](https://img.shields.io/badge/Wireshark-Network_Forensics-1679A7.svg)
![Linux](https://img.shields.io/badge/Linux-Enterprise_Hardening-yellow.svg)

## 📖 Executive Summary
A comprehensive cybersecurity framework simulating the full lifecycle of Advanced Persistent Threats (APTs) in Enterprise networks. Divided into three domains: **DevSecOps**, **Offensive Security**, and **DFIR**.

## 🏗️ Repository Architecture
- `/infrastructure/` — IaC, Ansible roles, and defensive baselines.
- `/blue_team/` — IDS signatures (Suricata), YARA rules, and iptables configs.
- `/red_team/` — Offensive Python tooling (Scapy, Raw Sockets, C2).
- `/ir_team/` — Automated DFIR parsers, Log analyzers, SOAR integrations.
- `/logs/` — PCAP dumps and raw logs (Gitignored).

🔗 **[View Full Project Development Log (Changelog)](CHANGELOG.md)**