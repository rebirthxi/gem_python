import hashlib
from gem_python.packets.basic_packet import BasicPacket


class VerCheckRequest(BasicPacket):
    def __init__(self, data: bytes):
        self.version = data[116:122].decode("utf-8") + "xx_x"

    def to_bytes(self) -> bytes:
        pass


class VerCheckResponseGood(BasicPacket):
    def __init__(self):
        self.expansion_mask = 0xFFE
        self.feature_mask = 0xD

    def to_bytes(self) -> bytes:
        data = bytearray(
            [0x28, 0x00, 0x00, 0x00, 0x49, 0x58, 0x46, 0x46, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4f, 0xe0, 0x5d, 0xad,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        )

        data[32:34] = int(self.expansion_mask).to_bytes(2, byteorder="little")
        data[36:38] = int(self.feature_mask).to_bytes(2, byteorder="little")

        # md5 checksum
        data[12:28] = hashlib.md5(data).digest()

        return data

    def from_bytes(self, data: bytes) -> None:
        pass


class VerCheckResponseBad(BasicPacket):
    def to_bytes(self) -> bytes:
        data = bytearray(
            [0x24, 0x00, 0x00, 0x00, 0x49, 0x58, 0x46, 0x46, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00]
        )

        data[32:34] = int(331).to_bytes(2, byteorder="little")

        # md5 checksum
        data[12:28] = hashlib.md5(data).digest()

        return data
