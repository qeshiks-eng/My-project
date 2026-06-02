@'
# Controlled Adversary Emulation

This section contains lab-only adversary-emulation scenarios used to validate defensive controls, detections, and incident-response automation.

## Safety notice

These materials are intended only for isolated lab environments.

They are not intended for unauthorized access, real-world exploitation, persistence, evasion, or use against third-party systems.

## Defensive purpose

The purpose of this section is to:

- generate controlled lab traffic
- understand attack artifacts
- validate Suricata/YARA/Sigma detections
- test incident response automation
- improve hardening controls

## Public repository policy

Any code in this section must be safe, scoped, documented, and clearly tied to defensive validation.
'@ | Set-Content .\controlled-adversary-emulation\README.md -Encoding UTF8