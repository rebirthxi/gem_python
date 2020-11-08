import asyncio
from authenticationserver.auth_server import AuthServerProtocol
from authenticationserver.auth_enum import AccountStatus
from dataserver.interfaces.data_handle import DataHandle


class FakeDatahandle(DataHandle):
    def AuthenticateAccount(self, account_name, passwd):
        if account_name == "test" and passwd == "test":
            print("Authentication good")
            return 1000, AccountStatus.NORMAL
        return 0, AccountStatus.BANNED


async def main():
    authed_accounts = {}
    datahandle      = FakeDatahandle()

    loop = asyncio.get_running_loop()
    server = await loop.create_server(
        lambda: AuthServerProtocol(datahandle, authed_accounts),
        '192.168.81.131', 54231
    )

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
