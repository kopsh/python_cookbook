"""
11.3 创建UDP服务器
"""
import socketserver


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        print("Get connection from: {}", self.client_address)
        msg, sock = self.request
        print(msg)
        sock.sendto(msg, self.client_address)


class EchoHandler(socketserver.DatagramRequestHandler):

    def handle(self) -> None:
        print("Get connection from: {}", self.client_address)
        line = self.rfile.read(8192)
        print(line)
        self.wfile.write(line)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # server = socketserver.UDPServer(("localhost", 20000), EchoRequestHandler)
    server = socketserver.ThreadingUDPServer(("localhost", 20000), EchoHandler)
    server.serve_forever()
