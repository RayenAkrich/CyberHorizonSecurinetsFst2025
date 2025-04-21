import struct

GTP_HEADER_LENGTH = 8

class GTPHeader: 
    def __init__(self, version, protocol_type, message_type, length, teid):
        self.version = version
        self.protocol_type = protocol_type
        self.message_type = message_type
        self.length = length
        self.teid = teid

    def pack(self):
        flags = (self.version << 5) | self.protocol_type
        return struct.pack("!BBHI", flags, self.message_type, self.length, self.teid)

    @staticmethod
    def unpack(data):
        header_byte, message_type, length, teid = struct.unpack("!BBHI", data[:GTP_HEADER_LENGTH])
        version = header_byte >> 5
        protocol_type = header_byte & 0x1F
        return GTPHeader(version, protocol_type, message_type, length, teid)

def print_packet(packet):
    print(f"Packet ({len(packet)} bytes): {' '.join(f'{b:02x}' for b in packet)}")

def decapsulate_gtp(packet, packet_size):
    if packet_size < GTP_HEADER_LENGTH:
        return
    header = GTPHeader.unpack(packet)
    inner_packet = packet[GTP_HEADER_LENGTH:]
    inner_packet_size = header.length
    print(f"Traitement du paquet GTP-U avec TEID {header.teid}")
    print_packet(inner_packet)
    decapsulate_gtp(inner_packet, inner_packet_size)

def handle_upf_packet(packet, packet_size):
    print("=== UPF: réception d’un paquet GTP-U ===")
    print_packet(packet)
    decapsulate_gtp(packet, packet_size)

