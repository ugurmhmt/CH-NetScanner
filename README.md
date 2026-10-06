# CH-NetScanner

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux-orange.svg)](https://www.kernel.org/)

A lightweight, high-performance ARP-based network scanner written in Python using Scapy. It discovers active host devices on a local subnet and lists their IP and MAC addresses in a clean terminal table.

---

## 🚀 Features

- **ARP Network Scanning:** Uses fast ARP request broadcasts to identify active network hosts.
- **Flexible Targets:** Supports single IP inputs as well as full CIDR network notation (e.g., `192.168.1.0/24`).
- **Clean Terminal Interface:** Formatted output powered by `tabulate` and colorized alerts using `colorama`.
- **Root Protection:** Automatic check to verify root/sudo privileges before execution.
- **Silent Engine Mode:** Suppresses raw Scapy debug outputs for a cleaner terminal session.

---

## 🛠️ Requirements

- **Operating System:** Linux (Kali Linux, Ubuntu, Debian, etc.)
- **Permissions:** Root / `sudo` privileges (required for raw packet socket access)
- **Python:** Python 3.x

### Dependencies
- `scapy`
- `colorama`
- `tabulate`

---

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ugurmhmt/CH-NetScanner.git
   cd CH-NetScanner
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Or install manually:*
   ```bash
   pip install scapy colorama tabulate
   ```

---

## 💻 Usage

Run the scanner with root privileges and specify the target IP or subnet using the `-i` / `--ipaddress` flag:

```bash
sudo python3 ch_netScanner.py -i 192.168.1.0/24
```

### Options

| Flag | Long Flag | Description | Example |
| :--- | :--- | :--- | :--- |
| `-i` | `--ipaddress` | Target IP address or CIDR range *(Required)* | `-i 192.168.1.0/24` |
| `-h` | `--help` | Display help guide and available parameters | `-h` |

---

## 📊 Example Output

```text
[*] 192.168.1.0/24 taranıyor...

[+] Taramada Yanıt Dönen Cihazlar:

╒══════╤═══════════════╤═══════════════╤═══════════════════╕
│   No │ Query IP      │ Answer IP     │ Answer MAC        │
╞══════╪═══════════════╪═══════════════╪═══════════════════╡
│    1 │ 192.168.1.1   │ 192.168.1.1   │ AA:BB:CC:DD:EE:FF │
│    2 │ 192.168.1.10  │ 192.168.1.10  │ 11:22:33:44:55:66 │
╘══════╧═══════════════╧═══════════════╧═══════════════════╛
```

---

## ⚙️ How It Works

```text
 Target Network (CIDR)
         │
         ▼
 ARP Request Packet (pdst)
         │
         ▼
 Broadcast Frame (ff:ff:ff:ff:ff:ff)
         │
         ▼
 Local Network Broadcast
         │
         ▼
 Active Hosts Send ARP Responses
         │
         ▼
 IP (psrc) + MAC (hwsrc) Extraction
         │
         ▼
 Formatted Terminal Table
```

---

## ⚠️ Disclaimer

This tool is created for **educational purposes and authorized network security testing only**. Do not scan or perform reconnaissance on networks without explicit permission from the network owner/administrator. The author assumes no responsibility for unauthorized or illegal usage.
