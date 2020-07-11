"""
11.2 创建TCP服务器
"""
import socketserver


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        print("Get connection from: {}", self.client_address)
        while True:
            # self.request -> socket obj
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


class EchoHandler(socketserver.StreamRequestHandler):

    def handle(self) -> None:
        print("Get connection from: {}", self.client_address)
        for line in self.rfile:
            print(line)
            self.wfile.write(line)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    socketserver.ThreadingTCPServer.allow_reuse_address = True
    # server = socketserver.TCPServer(("localhost", 20000), EchoRequestHandler)
    server = socketserver.ThreadingTCPServer(("localhost", 20000), EchoHandler)
    server.serve_forever()
