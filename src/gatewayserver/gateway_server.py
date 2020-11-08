import asyncio


class GatewayServerProtocol(asyncio.Protocol):
    def __init__(self, authed_accounts: dict):
        self.authed_accounts = authed_accounts
        self.peername        = ()
        self.transport       = None  # type: asyncio.transports.BaseTransport

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.peername = transport.get_extra_info('peername')
        print('Gateway connection from {}'.format(self.peername))
        self.transport = transport
        # self.transport.write(int(0x01).to_bytes(5, byteorder="big"))
        # print(int(0x01).to_bytes(5, byteorder="big"))

    def data_received(self, data: bytes) -> None:
        print("gateway:")
        print(data)


