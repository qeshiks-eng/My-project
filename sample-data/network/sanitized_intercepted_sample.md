@'
# Sanitized Intercepted Traffic Sample

This file is a placeholder for lab-only intercepted traffic examples.

Real credentials, tokens, private data, and production traffic must not be stored in this public repository.

Example fields:
- source_ip: 192.0.2.10
- destination_ip: 198.51.100.20
- protocol: HTTP
- finding: clear-text credential pattern detected in a controlled lab
'@ | Set-Content .\sample-data\network\sanitized_intercepted_sample.md -Encoding UTF8