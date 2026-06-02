@'
# Controlled Adversary Emulation

This section contains lab-only adversary-emulation scenarios used to validate defensive controls, detection rules, and incident-response automation.

## Important safety notice

These materials are intended only for isolated lab environments.

They are not intended for unauthorized access, real-world exploitation, persistence on real systems, evasion in production environments, or use against third-party systems.

## Defensive purpose

The purpose of this section is to:

- generate controlled lab traffic
- understand attack artifacts
- validate Suricata/YARA/Sigma-style detections
- test incident-response automation
- improve hardening controls
- understand what evidence appears in logs, PCAP files, and host artifacts

## Public repository policy

Any code in this section must be:

- scoped to lab use
- documented
- tied to defensive validation
- free of real credentials
- free of real targets
- free of private infrastructure details

## Do not run against

- third-party systems
- public networks
- production environments
- employer infrastructure
- systems without explicit permission