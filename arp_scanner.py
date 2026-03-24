from scapy.all import ARP, Ether, srp

target = input("Enter IP range (example: 192.168.1.1/24): ")

# Create ARP request
arp = ARP(pdst=target)

# Create Ethernet frame
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine both
packet = ether / arp

# Send packet and receive response
result = srp(packet, timeout=2, verbose=0)[0]

print("\nDevices found:")

for sent, received in result:
    print("IP:", received.psrc, "  MAC:", received.hwsrc)