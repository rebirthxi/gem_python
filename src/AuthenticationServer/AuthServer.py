import asyncore
from src.AuthenticationServer.AuthHandler import AuthHandler


class AuthServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.auth_connections = {}

    def handle_accepted(self, sock, ip_port):
        addr = ip_port[0]
        if addr not in self.auth_connections.keys():
            self.auth_connections[addr] = []
        self.auth_connections[addr].append(AuthHandler(sock, addr, self))
        print("Connection Created")

    def remove_auth_connection(self, connection):
        """
        :type connection: AuthHandler
        :param connection:
        :return:
        """
        self.auth_connections[connection.ip_addr].remove(connection)

        if len(self.auth_connections[connection.ip_addr]) == 0:
            self.auth_connections[connection.ip_addr] = None

    # update when proper data server is available for auth
    def authenticate(self, name, passwd):
        # print("%s." % name)
        print(bytearray(name, encoding="utf-8"))
        print(bytearray("test", encoding="utf-8"))
        # print(type(name))
        # print("%s." % passwd)
        # print(type(passwd))

        if name == "test" and passwd == "test":
            print("Authentication good")
            return 1000, 0x01
        return 0, 0x99


server = AuthServer('192.168.81.129', 54231)
asyncore.loop()
