CH-NetScanner 🔎

A simple ARP network scanner written in Python using Scapy.

Features

ARP-based network scanning

IP/CIDR support

IP and MAC address detection

Formatted terminal output

Root/sudo privilege check

Installation
git clone https://github.com/YOUR_USERNAME/CH-NetScanner.git
cd CH-NetScanner
pip install -r requirements.txt

Usage

Run the scanner with sudo:

sudo python3 ch_netScanner.py -i 192.168.1.0/24


Example:

[*] Scanning 192.168.1.0/24...

[+] Packets with Responses:

No   Query IP       Answer IP       Answer MAC
1    192.168.1.1    192.168.1.1     AA:BB:CC:DD:EE:FF
2    192.168.1.10   192.168.1.10    11:22:33:44:55:66

Requirements
scapy
colorama
tabulate

Disclaimer

This tool is intended for educational purposes and authorized network testing only.

Do not scan networks or devices without permission.
