# Lab Scenario Index

This document explains the purpose of each lab-only adversary-emulation script.

The scripts in this directory are not production tools. They are used as controlled lab scenarios for understanding telemetry, writing detections, and testing incident-response automation.

## Scenario table

| File | Lab scenario | Defensive purpose |
|---|---|---|
| `l2_arp_spoofing_lab_generator.py` | ARP spoofing / L2 abuse simulation | Understand ARP poisoning artifacts and validate L2 detection logic |
| `dhcp_exhaustion_lab_generator.py` | DHCP exhaustion simulation | Learn DHCP starvation indicators and validate DHCP anomaly detection |
| `icmp_test_traffic_generator.py` | ICMP test payload generation | Generate simple ICMP traffic for parser and detection testing |
| `icmp_covert_channel_lab.py` | ICMP covert channel lab | Understand suspicious ICMP payload patterns and validate covert-channel detections |
| `hsrp_failover_abuse_lab.py` | HSRP failover abuse simulation | Understand HSRP attack artifacts and validate HSRP monitoring logic |
| `vlan_misconfiguration_lab.py` | VLAN misconfiguration / hopping lab | Study VLAN segmentation weaknesses and related detection opportunities |
| `smb_test_packet_crafter.py` | SMB packet crafting lab | Generate controlled SMB-like artifacts for parser and detection testing |
| `reverse_shell_detection_test_generator.py` | Reverse shell indicator simulation | Validate reverse-shell detection rules and incident-response logic |
| `linux_persistence_artifact_lab.py` | Linux persistence artifact simulation | Understand cron/system persistence artifacts from a defensive perspective |
| `ssh_authorized_keys_audit_lab.py` | SSH authorized_keys audit scenario | Validate SSH key audit logic and unauthorized key detection |
| `linux_misconfiguration_lab.py` | Linux misconfiguration lab | Study unsafe Linux configurations and related hardening controls |
| `windows_execution_artifact_lab.ps1` | Windows execution artifact simulation | Understand Windows execution traces and detection opportunities |
| `windows_firewall_misconfiguration_lab.ps1` | Windows firewall misconfiguration lab | Study firewall rule changes and validation of host hardening checks |
| `windows_persistence_artifact_lab.ps1` | Windows persistence artifact simulation | Understand persistence-related artifacts and defensive detection logic |

## Usage rules

Use only in:

- local virtual machines
- isolated lab networks
- intentionally created training environments
- owned systems

Do not use for:

- unauthorized access
- third-party testing
- production execution
- persistence on real systems
- credential collection
- evasion against security controls

## Portfolio interpretation

This section exists to demonstrate that offensive techniques are being studied from a defensive engineering perspective: telemetry, detection, incident response, and hardening.
