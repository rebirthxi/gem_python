import asyncore
from authenticationserver.auth_server import AuthServer
from dataserver.interfaces.data_handle import DataHandle


class FakeDatahandle(DataHandle):
    def AuthenticateAccount(self, account_name, passwd):
        if account_name == "test" and passwd == "test":
            print("Authentication good")
            return 1000, 0x01
        return 0, 0x99


def main():
    authed_accounts = {}
    datahandle      = FakeDatahandle()
    server          = AuthServer('192.168.81.129', 54231, datahandle, authed_accounts)
    asyncore.loop()


if __name__ == "__main__":
    main()
