import hashlib
from gem_python.packets.basic_packet import BasicPacket


class VerCheckResponse(BasicPacket):
    def __init__(self):
        self.version = ""
        self.expansion_mask = 0xFFE
        self.feature_mask = 0xD
        # self.expansion_mask = 0
        # self.feature_mask = 0

    def to_bytes(self) -> bytes:
        data = bytearray(
            [0x28, 0x00, 0x00, 0x00, 0x49, 0x58, 0x46, 0x46, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4f, 0xe0, 0x5d, 0xad,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        )

        data[32:34] = int(self.expansion_mask).to_bytes(2, byteorder="little")
        data[36:38] = int(self.feature_mask).to_bytes(2, byteorder="little")

        for x in range(len(data)):
            print("{} {}".format(x, hex(data[x])))

        # md5 checksum
        data[12:28] = hashlib.md5(data).digest()
        for x in hashlib.md5(data).digest():
            print(hex(x))
        for x in range(len(data)):
            print("{} {}".format(x, hex(data[x])))
        return data

    def from_bytes(self, data: bytes) -> None:
        pass
