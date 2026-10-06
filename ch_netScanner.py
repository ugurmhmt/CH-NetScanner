import optparse
import os
import sys
from ipaddress import ip_network

import scapy.all as scapy
from colorama import Fore as f
from colorama import init
from tabulate import tabulate

init(autoreset=True)

arguments_in_ip = optparse.OptionParser(description="Help Guide for ARP Scanner")
arguments_in_ip.add_option(
    "-i",
    "--ipaddress",
    help="IP address, single option (Example: 192.168.1.0/24)",
    dest="ip",
)

ip, _ = arguments_in_ip.parse_args()
# ip.ip


def ip_address_controll(ip):
    if not ip:
        print(f.RED + "[!] Please specify an IP or CIDR range using the -i parameter.")
        sys.exit(1)
    try:
        network = ip_network(ip, strict=False)
        return str(network)
    except ValueError:
        print(f.RED + "Invalid IP address")
        sys.exit(1)


def ARPScan(ipaddress):
    Arp_request_pack = scapy.ARP(pdst=ipaddress)
    Broadcast_pack = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    CombinedPack = Broadcast_pack / Arp_request_pack

    answer, _ = scapy.srp(CombinedPack, timeout=2, verbose=False)
    return answer


def Result_Arp_Pack():
    ipaddress = ip_address_controll(ip.ip)
    if os.geteuid() != 0:
        print(f.RED + "Root/sudo privileges are required for this action.")
        print(f.YELLOW + "Example: sudo python3 ch_netScanner.py -i 192.168.1.0/24")
        sys.exit(1)

    print(f.YELLOW + f"[*] Scanning {ipaddress}...")
    datas = ARPScan(ipaddress)

    header = ["No", "Query IP", "Answer IP", "Answer MAC"]

    answerList = list()

    for count, (sent, recevid) in enumerate(datas, start=1):
        answerList.append([count, sent.pdst, recevid.psrc, recevid.hwsrc])
    if answerList:
        print("\n" + f.GREEN + "[+] Packets with Responses:")
        print(tabulate(answerList, headers=header, tablefmt="github"))
    else:
        print("\n" + f.RED + "[-] No devices found.")


if __name__ == "__main__":
    Result_Arp_Pack()
