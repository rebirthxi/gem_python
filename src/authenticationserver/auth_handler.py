import asyncore
from authenticationserver.auth_enum import AuthCode, AccountStatus, LoginResult
from dataserver.interfaces.data_handle import DataHandle


class AuthHandler(asyncore.dispatcher_with_send):
    def __init__(self, sock, ip_port, account_authenticator, authed_accounts):
        """
        :type account_authenticator: DataHandle
        :type authed_accounts: dict
        :param sock:
        :param ip_port:
        :param account_authenticator:
        """
        super(AuthHandler, self).__init__(sock)
        self.authenticator   = account_authenticator
        self.authed_accounts = authed_accounts
        self.ip_port         = ip_port

    def handle_read(self):
        request = self.recv(33)
        print("Request received...")
        if len(request) == 33:
            name   = request[0:15].decode("utf-8").strip("\x00")
            passwd = request[16:31].decode("utf-8").strip("\x00")
            code   = request[32]

            if code == AuthCode.LOGIN_ATTEMPT:
                response = self.login_attempt(name, passwd)
            else:
                response = None

            if response is not None:
                self.send(response)
                print("Authentication complete, closing auth socket!")
            self.close()

        else:
            self.close()

    def login_attempt(self, name, passwd) -> bytearray:
        response = None

        # if authenticated
        accid, status = self.authenticator.AuthenticateAccount(name, passwd)

        if status == AccountStatus.ACCOUNT_NORMAL:
            # send MSG_LOGIN to msg server for all chars... not sure why it does this
            self.authed_accounts[accid] = self.ip_port
            response = status.to_bytes(1, byteorder="big") + accid.to_bytes(4, byteorder="big")

        return response
