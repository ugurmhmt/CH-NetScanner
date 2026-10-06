CH-NetScanner 🔎

CH-NetScanner is a simple ARP-based network scanner written in Python. It uses Scapy to send ARP requests over a specified IP/CIDR range and displays devices that respond, including their IP and MAC addresses.

This project is intended for network administration, local network discovery, and cybersecurity learning purposes.

⚠️ Disclaimer: Only scan networks that you own or have explicit permission to test. Unauthorized network scanning may violate organizational policies or applicable laws.

✨ Features

🔎 ARP-based local network scanning

🌐 Supports IP addresses and CIDR ranges

📡 Sends Ethernet broadcast ARP requests

🖥️ Detects responding devices

📋 Displays results in a formatted table

🎨 Colored terminal output

🛡️ Checks for root/sudo privileges

❌ Validates IP/CIDR input

⚡ Lightweight and simple Python implementation

🛠️ Technologies

The project is built with:

Python 3

Scapy – packet manipulation and network communication

Colorama – colored terminal output

Tabulate – formatted terminal tables

Optparse – command-line argument parsing

📋 Requirements

Make sure Python 3 and pip are installed.

Install the required Python packages:

pip install scapy colorama tabulate


On Kali Linux, you may also use:

sudo apt install python3-scapy python3-colorama python3-tabulate

📥 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/CH-NetScanner.git


Enter the project directory:

cd CH-NetScanner


(Optional) Create a virtual environment:

python3 -m venv myenv


Activate the virtual environment:

Linux / macOS
source myenv/bin/activate


Install dependencies:

pip install -r requirements.txt

🚀 Usage

Because ARP packet transmission generally requires elevated privileges, run the scanner with sudo:

sudo python3 ch_netScanner.py -i 192.168.1.0/24

Example
[*] Scanning 192.168.1.0/24...

[+] Packets with Responses:

╒══════╤═════════════╤════════════╤═══════════════════╕
│   No │ Query IP   │ Answer IP  │ Answer MAC        │
╞══════╪═════════════╪════════════╪═══════════════════╡
│    1 │ 192.168.1.1 │ 192.168.1.1 │ AA:BB:CC:DD:EE:FF │
│    2 │ 192.168.1.5 │ 192.168.1.5 │ 11:22:33:44:55:66 │
╘══════╧═════════════╧════════════╧═══════════════════╛

📌 Command-Line Options
Option	Description
-i	Specify the target IP address or CIDR network
--ipaddress	Specify the target IP address or CIDR network
-h	Display the help message

Example:

python3 ch_netScanner.py --help

🌐 CIDR Examples

The scanner accepts CIDR notation such as:

192.168.1.0/24
192.168.0.0/24
10.0.0.0/24
172.16.0.0/24


For example:

sudo python3 ch_netScanner.py -i 192.168.1.0/24


A /24 network contains 256 addresses, including the network and broadcast addresses.

📊 Output

For every device that responds to the ARP request, the scanner displays:

No – Result number

Query IP – IP address queried by the scanner

Answer IP – IP address returned by the responding device

Answer MAC – MAC address of the responding device

Example:

No   Query IP       Answer IP      Answer MAC
1    192.168.1.1    192.168.1.1    AA:BB:CC:DD:EE:FF
2    192.168.1.10   192.168.1.10   11:22:33:44:55:66

🔍 How It Works

The scanner follows these basic steps:

User Input
    │
    ▼
IP/CIDR Validation
    │
    ▼
Create ARP Request
    │
    ▼
Create Ethernet Broadcast
    │
    ▼
Send Packets with Scapy
    │
    ▼
Receive ARP Responses
    │
    ▼
Extract IP + MAC Addresses
    │
    ▼
Display Results


The core scanning process uses Scapy:

Arp_request_pack = scapy.ARP(pdst=ipaddress)
Broadcast_pack = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
CombinedPack = Broadcast_pack / Arp_request_pack

answer, _ = scapy.srp(
    CombinedPack,
    timeout=2,
    verbose=False
)


The Ethernet frame is broadcast across the local network, allowing devices in the specified network range to respond to the ARP request.

⚠️ Troubleshooting
No devices found

If you receive:

[-] No devices found.


check the following:

Make sure the target CIDR matches your local network.

Make sure you are connected to the target network.

Run the program with sudo.

Check your network interface:

ip addr


Check your routing table:

ip route


For example, if your machine has:

192.168.1.25/24


then:

192.168.1.0/24


is likely the appropriate local network to scan.

🔐 Security & Legal Notice

This tool is designed for authorized network discovery and educational purposes.

Do not use CH-NetScanner to scan networks, systems, or devices without authorization.

You are responsible for complying with all applicable:

Laws and regulations

Network policies

Organizational security policies

Terms of service

The author is not responsible for misuse of this software.

📁 Project Structure
CH-NetScanner/
│
├── ch_netScanner.py
├── requirements.txt
└── README.md

📦 requirements.txt

Create a requirements.txt file containing:

scapy
colorama
tabulate


Then install everything with:

pip install -r requirements.txt

🧪 Example Workflow
git clone https://github.com/YOUR_USERNAME/CH-NetScanner.git

cd CH-NetScanner

pip install -r requirements.txt

sudo python3 ch_netScanner.py -i 192.168.1.0/24

📈 Future Improvements

Possible future improvements include:

 Automatic network/interface detection

 Custom network interface selection

 Export results to CSV

 Export results to JSON

 Vendor lookup from MAC addresses

 Improved error handling

 Configurable timeout

 Configurable packet rate

 IPv6 discovery support

 Better CLI argument handling with argparse

👨‍💻 Author

CH-NetScanner

A lightweight Python project created for learning network scanning, ARP, packet manipulation, and cybersecurity concepts.

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.