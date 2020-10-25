from src.AuthenticationServer.AuthEnum import AuthCode, AccountStatus, LoginResult


class AuthHandler(asyncore.dispatcher_with_send):
    def __init__(self, sock, addr, server):
        super(AuthHandler, self).__init__(sock)
        self.ip_addr = addr
        self.server = server  # type: AuthServer
        self.login = ""  # type: str

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
                self.close()
                print("Authentication complete, closing auth socket!")

        else:
            self.close()

    def login_attempt(self, name, passwd) -> bytearray:
        response = None

        # if authenticated
        accid, status = self.server.authenticate(name, passwd)

        if status == AccountStatus.ACCOUNT_NORMAL:
            # send MSG_LOGIN to msg server for all chars... not sure why it does this
            response = status.to_bytes(1, byteorder="big") + accid.to_bytes(4, byteorder="big")
            print(response)

        return response

    def handle_close(self):
        self.close()
        self.server.remove_auth_connection(self)
