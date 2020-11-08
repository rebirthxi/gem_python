import asyncio
from authenticationserver.auth_enum import AuthCode, AccountStatus
from gem_python.packets.auth_packet import AuthRequestPacket, AuthResponsePacket, AuthRequestSizeError
from dataserver.interfaces.data_handle import DataHandle


class AuthServerProtocol(asyncio.Protocol):
    def __init__(self, authenticator: DataHandle, authed_accounts: dict):
        # super(self, AuthServerProtocol).__init__()
        self.authenticator   = authenticator
        self.authed_accounts = authed_accounts
        self.peername        = ()
        self.transport       = None  # type: asyncio.transports.BaseTransport

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.peername = transport.get_extra_info('peername')
        print('Auth connection from {}'.format(self.peername))
        self.transport = transport

    def data_received(self, data: bytes) -> None:
        try:
            request = AuthRequestPacket(data)

            if request.code == AuthCode.LOGIN_ATTEMPT:
                response = self.login_attempt(request.name, request.passwd)

                if response.status == AccountStatus.NORMAL:
                    print("Authentication complete, closing auth socket!")
                else:
                    print("Authentication failed.")
                self.transport.write(response.to_bytes())
                self.transport.close()
            else:
                print("Unknown request code")
                self.transport.close()

        except AuthRequestSizeError as e:
            print("When doing {} encountered the following error {}".format(e.expression, e.message))
            self.transport.close()

    def login_attempt(self, name: str, passwd: str) -> AuthResponsePacket:
        response = AuthResponsePacket()

        # if authenticated
        accid, status = self.authenticator.AuthenticateAccount(name, passwd)

        if status == AccountStatus.NORMAL:
            account_info = {"acct_name": name, "acct_id": accid}
            ip           = self.peername[0]

            if self.peername in self.authed_accounts.keys():
                self.authed_accounts[ip].append(account_info)
            else:
                self.authed_accounts[ip] = [account_info]

            response.status = status
            response.accid  = accid

        elif status == AccountStatus.BANNED:
            response.status = AccountStatus.BANNED
            response.accid  = 0

        else:
            response.status = AccountStatus.NOACCT
            response.accid  = 0

        return response
