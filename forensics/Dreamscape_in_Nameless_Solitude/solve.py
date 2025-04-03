from scapy.all import *
from binascii import unhexlify
data = b''

def extract_dns_answers(pcapng_file):
    dns_answers = []
    packets = rdpcap(pcapng_file)
    for packet in packets:
        if DNS in packet and packet[DNS].qr == 1:
            dns_answers.append(packet)
    return dns_answers

def processPacket(dns_packet):
    global data
    query_name = dns_packet[DNS].qd.qname.decode()
    data += unhexlify(query_name[:query_name.index('.')])

def main():
    pcapng_file = "houkaistarrail.pcapng"
    dns_answers = extract_dns_answers(pcapng_file)
    for i, packet in enumerate(dns_answers):
        processPacket(packet)

    with open("output.jpg", "wb") as f:
        f.write(data)

if __name__ == "__main__":
    main()