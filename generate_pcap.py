# =======================================
# generate_pcap.py
# Creates a sample PCAP file for testing
# Packet sniffing (capturing network traffic)
# =======================================
from scapy.all import IP, TCP, UDP, ICMP, wrpcap


def create_sample_pcap(output_file="test.pcap"):
    packets = []
    
    # =======================================
    # Create sample TCP packets
    # =======================================
    for i in range(100):
        pkt = IP(src="192.168.1.10", dst="192.168.1.20") / TCP(dport=80, sport=1000 + i)
        packets.append(pkt)
    
    # =======================================
    # Create sample UDP packets
    # =======================================
    for i in range(5):
        pkt = IP(src="192.168.1.30", dst="8.8.8.8") / UDP(dport=53, sport=2000 + i)
        packets.append(pkt)
    
    # =======================================
    # Create sample ICMP packets
    # =======================================
    for i in range(3):
        pkt = IP(src="192.168.1.40", dst="1.1.1.1") / ICMP()
        packets.append(pkt)
    
    # =======================================
    # Save packets into a PCAP file
    # =======================================
    wrpcap(output_file, packets)
    print(f"Sample PCAP created successfully: {output_file}")


create_sample_pcap()
