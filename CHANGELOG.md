# 📓 Project Development Log

This document tracks the development of my supplemental cybersecurity engineering lab.

The repository is focused on defensive security, detection engineering, incident response automation, infrastructure hardening, security automation, and controlled lab-based adversary emulation in isolated environments.

---

<details>
<summary><strong>2026-06-02 — Portfolio refactor and public safety cleanup</strong></summary>

### Repository structure refactor

Reorganized the repository from an experimental lab layout into a clearer cybersecurity engineering structure:

- `blue_team/` → `detection-engineering/`
- `ir_team/` → `incident-response-automation/`
- `infrastructure/` → `infrastructure-security/`
- `red_team/` → `controlled-adversary-emulation/`
- `logs/` → `sample-data/`

### Public safety improvements

Improved public-facing repository hygiene:

- removed raw intercepted-output style files from the public tree
- replaced risky-looking outputs with sanitized sample documentation
- removed outdated `docker-compose.yml`
- removed old aggressive changelog wording
- replaced hardcoded lab secrets with placeholders or environment variables
- added `.env.example`
- added `docs/safety_and_scope.md`
- added `docs/portfolio_overview.md`
- added `controlled-adversary-emulation/docs/lab_scenarios.md`

### Controlled adversary emulation reframing

Renamed lab-only scripts to make their defensive purpose clearer.

These files are used to generate controlled telemetry, understand artifacts, validate detection logic, test incident-response automation, and improve hardening controls in isolated lab environments.

Examples:

- ARP spoofing lab generator
- DHCP exhaustion lab generator
- ICMP covert-channel lab
- HSRP failover-abuse lab
- reverse-shell detection test generator
- Linux and Windows persistence artifact labs

</details>

---

<details>
<summary><strong>Infrastructure Security Track</strong></summary>

### Linux hardening

Added Ansible-based Linux hardening practice.

Current areas:

- SSH configuration hardening
- audit rule deployment
- network hardening notes
- egress filtering practice
- basic infrastructure security automation

### Windows hardening

Added Windows hardening practice.

Current areas:

- Windows security configuration
- host hardening logic
- PowerShell-based administrative checks
- Windows-focused investigation helpers

### Network hardening

Added network security notes and configuration practice.

Current areas:

- L2/L3 defensive notes
- routing and segmentation concepts
- email anti-spoofing notes
- network security documentation

</details>

---

<details>
<summary><strong>Detection Engineering Track</strong></summary>

Added detection engineering experiments and Suricata rule practice.

Current examples:

- ICMP covert-channel detection
- reverse-shell indicator detection
- routing attack indicators

Future improvements:

- add rule explanations
- add false-positive notes
- add safe test data references
- add Sigma examples
- add YARA examples

</details>

---

<details>
<summary><strong>Incident Response Automation Track</strong></summary>

Added Python utilities for SOC/DFIR-style workflows.

Current areas:

- Linux log analysis
- Windows EVTX parsing
- PCAP parsing
- DHCP traffic analysis
- HSRP traffic analysis
- SSH audit helpers
- persistence artifact analysis
- network incident-response helpers

Goal:

- automate repetitive investigation tasks
- practice Python security engineering
- connect telemetry to detection and response logic

</details>

---

<details>
<summary><strong>Controlled Lab Emulation Track</strong></summary>

Added lab-only telemetry and artifact simulation scripts.

Purpose:

- generate controlled lab traffic
- understand what appears in logs and PCAP files
- validate detection logic
- test incident-response parsers
- improve hardening controls

Important:

These materials are not intended for unauthorized access, third-party testing, production execution, persistence on real systems, or evasion against security controls.

Detailed explanation:

- `controlled-adversary-emulation/docs/lab_scenarios.md`

</details>

---

<details>
<summary><strong>Sample Data and Artifact Hygiene</strong></summary>

Reorganized public-safe sample data.

Current contents:

- sanitized lab notes
- redacted example documentation
- reviewed lab PCAP sample

Repository rule:

Do not publish real credentials, tokens, private keys, personal data, production logs, or real intercepted traffic.

Unsafe raw lab outputs should be replaced with:

- sanitized examples
- markdown explanations
- defensive runbooks
- safe test samples
- detection rules
- parser scripts

</details>

---

## Current repository areas

| Area | Directory | Purpose |
|---|---|---|
| Detection Engineering | `detection-engineering/` | Suricata rules and detection logic |
| Incident Response Automation | `incident-response-automation/` | Python parsers and SOC/DFIR automation |
| Infrastructure Security | `infrastructure-security/` | Linux, Windows, and network hardening |
| Controlled Lab Emulation | `controlled-adversary-emulation/` | Lab-only telemetry and artifact simulation |
| Sample Data | `sample-data/` | Sanitized lab samples |
| Documentation | `docs/` | Safety scope and portfolio overview |

## Public repository rules

This repository must not contain:

- real credentials
- private keys
- API tokens
- production logs
- production traffic captures
- personal data
- real intercepted data
- unauthorized access tooling
