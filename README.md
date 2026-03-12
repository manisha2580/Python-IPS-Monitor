# Python-IPS-Monitor
Description: A Python-based tool that monitors Windows for brute-force attacks and automatically blocks malicious IPs.

Prerequisites: Windows 11, Python 3.x, and Audit Policies enabled via secpol.msc.

How it works: 1. Monitors Security Logs for Event ID 4625.
2. Extracts the Source Network Address.
3. Executes a netsh command to create a block rule.

Disclaimer: "For educational/lab purposes only."
