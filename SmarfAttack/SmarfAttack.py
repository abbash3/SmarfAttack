from scapy.all import *
a = IP(src = "1.1.1.1",dst ="1.1.1.0/24")/ICMP()
send(a)