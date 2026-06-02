@'
# Lab Traffic Generators

This directory contains controlled lab traffic generators and artifact simulation scripts.

All examples are intended for isolated training networks and defensive validation only.

Use cases:

- detection rule testing
- PCAP generation
- incident response parser validation
- hardening control validation
- understanding security telemetry

Do not run these scripts against third-party systems or production networks.
'@ | Set-Content .\controlled-adversary-emulation\lab-traffic-generators\README.md -Encoding UTF8