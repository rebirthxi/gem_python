import asyncio
import gem_python.packets.ver_check_packet as ver_packets


class LobbyServerProtocol(asyncio.Protocol):
    def __init__(self, authed_accounts: dict, client_version: str):
        self.authed_accounts = authed_accounts
        self.peername        = ()
        self.transport       = None  # type: asyncio.transports.BaseTransport
        self.client_version  = client_version

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.peername = transport.get_extra_info('peername')
        print('Lobby connection from {}'.format(self.peername))
        self.transport = transport
        # self.transport.write(int(0x01).to_bytes(5, byteorder="big"))
        # print(int(0x01).to_bytes(5, byteorder="big"))

    def data_received(self, data: bytes) -> None:
        print("lobby:")

        if data[8] == 0x26:
            request = ver_packets.VerCheckRequest(data)

            if self.client_version != request.version:
                print("Client version : {}\nServer requires: {}".format(request.version, self.client_version))
                response = ver_packets.VerCheckResponseBad()
            else:
                response = ver_packets.VerCheckResponseGood()

            self.transport.write(response.to_bytes())
