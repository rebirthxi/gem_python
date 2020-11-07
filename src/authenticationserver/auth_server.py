import asyncore
from authenticationserver.auth_handler import AuthHandler
from dataserver.interfaces.data_handle import DataHandle


class AuthServer(asyncore.dispatcher):
    def __init__(self, host, port, account_authenticator, authed_accounts):
        """
        :type authenticator: DataHandle
        :param host:
        :param port:
        :param authenticator:
        """
        asyncore.dispatcher.__init__(self)
        self.authenticator   = account_authenticator
        self.authed_accounts = authed_accounts
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, ip_port):
        handler = AuthHandler(sock, ip_port, self.authenticator, self.authed_accounts)
        print("Connection Created")
