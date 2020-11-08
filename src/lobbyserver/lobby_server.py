import asyncio
from gem_python.packets.ver_check_packet import VerCheckResponse

class LobbyServerProtocol(asyncio.Protocol):
    def __init__(self, authed_accounts: dict):
        self.authed_accounts = authed_accounts
        self.peername        = ()
        self.transport       = None  # type: asyncio.transports.BaseTransport

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.peername = transport.get_extra_info('peername')
        print('Lobby connection from {}'.format(self.peername))
        self.transport = transport
        # self.transport.write(int(0x01).to_bytes(5, byteorder="big"))
        # print(int(0x01).to_bytes(5, byteorder="big"))

    def data_received(self, data: bytes) -> None:
        print("lobby:")

        if data[8] == 0x26:
            print("sending response")
            response = VerCheckResponse()

            self.transport.write(response.to_bytes())
