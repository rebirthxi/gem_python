import asyncio
from authenticationserver.auth_server import AuthServerProtocol
from authenticationserver.auth_enum import AccountStatus
from gatewayserver.gateway_server import GatewayServerProtocol
from lobbyserver.lobby_server import LobbyServerProtocol
from dataserver.interfaces.data_handle import DataHandle


class FakeDataHandle(DataHandle):
    def AuthenticateAccount(self, account_name, passwd):
        if account_name == "test" and passwd == "test":
            print("Authentication good")
            return 1000, AccountStatus.NORMAL
        return 0, AccountStatus.BANNED


async def main():
    authed_accounts = {}
    data_handle     = FakeDataHandle()

    loop = asyncio.get_running_loop()
    auth_server = await loop.create_server(
        lambda: AuthServerProtocol(data_handle, authed_accounts),
        '192.168.81.131', 54231
    )

    gateway_server = await loop.create_server(
        lambda: GatewayServerProtocol(authed_accounts),
        '192.168.81.131', 54230
    )

    lobby_server = await loop.create_server(
        lambda: LobbyServerProtocol(authed_accounts, "302007xx_x"),
        '192.168.81.131', 54001
    )

    async with auth_server, gateway_server, lobby_server:
        await asyncio.gather(
            auth_server.serve_forever(),
            gateway_server.serve_forever(),
            lobby_server.serve_forever()
        )


if __name__ == "__main__":
    asyncio.run(main())
