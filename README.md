CH-NetScanner

A simple ARP-based network scanner written in Python using Scapy.

Features

ARP network scanning

IP/CIDR range support

IP and MAC address detection

Colored terminal output

Formatted scan results

Root/sudo privilege check

Installation
git clone https://github.com/YOUR_USERNAME/CH-NetScanner.git
cd CH-NetScanner
pip install -r requirements.txt

Usage

Run the scanner with root privileges:

sudo python3 ch_netScanner.py -i 192.168.1.0/24

Example
[*] Scanning 192.168.1.0/24...

[+] Packets with Responses:

╒══════╤═══════════════╤═══════════════╤═══════════════════╕
│ No   │ Query IP      │ Answer IP     │ Answer MAC        │
╞══════╪═══════════════╪═══════════════╪═══════════════════╡
│ 1    │ 192.168.1.1   │ 192.168.1.1   │ AA:BB:CC:DD:EE:FF │
│ 2    │ 192.168.1.10  │ 192.168.1.10  │ 11:22:33:44:55:66 │
╘══════╧═══════════════╧═══════════════╧═══════════════════╛

Requirements

Python 3

Scapy

Colorama

Tabulate

Linux environment

Root/sudo privileges

Install dependencies:

pip install scapy colorama tabulate

How It Works

CH-NetScanner sends ARP requests to the specified IP range and displays the IP and MAC addresses of devices that respond.

Target Network
      ↓
ARP Request
      ↓
Network Broadcast
      ↓
ARP Response
      ↓
IP + MAC Address
      ↓
Terminal Output

Disclaimer

This project is intended for educational purposes and authorized network testing only.

Do not scan networks or devices without permission.
