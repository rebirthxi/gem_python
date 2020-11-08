from gem_python.packets.basic_packet import BasicPacket
from authenticationserver.auth_enum import AccountStatus


class AuthRequestSizeError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message    = message


class AuthResponsePacket(BasicPacket):
    def __init__(self):
        self.accid = 0
        self.status = AccountStatus.NORMAL

    def to_bytes(self) -> bytes:
        return self.status.to_bytes(1, byteorder="big") + self.accid.to_bytes(4, byteorder="big")

    def from_bytes(self, data) -> None:
        pass


class AuthRequestPacket(BasicPacket):
    PACKET_SIZE = 33

    def __init__(self):
        self.name   = ""
        self.passwd = ""
        self.code   = None

    def to_bytes(self) -> bytes:
        pass

    def from_bytes(self, data: bytes) -> None:
        if len(data) == self.PACKET_SIZE:
            self.name   = data[0:15].decode("utf-8").strip("\x00")
            self.passwd = data[16:31].decode("utf-8").strip("\x00")
            self.code   = data[32]
        else:
            raise AuthRequestSizeError("len(data) == self.PACKET_SIZE", "Read data not equal to desired packet size.")
