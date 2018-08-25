from scapy.all import *


sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.222.1"))