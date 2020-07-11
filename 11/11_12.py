# coding=utf8
r"""
11.12 理解事件驱动的IO

事件驱动I/O本质上来讲就是将基本I/O操作（比如读和写）转化为你程序需要处理的事件
"""


class EventHandler:

    def fileno(self):
        """return the associated file descriptor"""
        raise NotImplementedError("must implement")

    def wants_to_receive(self):
        """return True if receving is allowed"""
        return False

    def handle_receive(self):
        pass

    def wants_to_send(self):
        """return True if sending is allowed"""
        return False

    def handle_send(self):
        pass


import select
import time
import socket


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


class UDPServer(EventHandler):

    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def wants_to_receive(self):
        return True

    def fileno(self):
        return self.sock.fileno()


class UDPTimeServer(UDPServer):

    def handle_receive(self):
        _, address = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('utf8'), address)


class UDPEchoServer(UDPServer):

    def handle_receive(self):
        msg, address = self.sock.recvfrom(8192)
        self.sock.sendto(msg, address)


class TCPServer(EventHandler):

    def __init__(self, address, client_handler, handler_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind(address)
        self.sock.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        print("Connection from {}".format(addr))
        self.handler_list.append(self.client_handler(client, self.handler_list))


class TCPClientHandler(EventHandler):

    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        self.handler_list.remove(self)

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoHandler(TCPClientHandler):

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)



if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # handlers = [UDPTimeServer(("", 20001)), UDPEchoServer(("", 20002))]
    handlers = []
    handlers.append(TCPServer(("", 20001), TCPEchoHandler, handlers))
    event_loop(handlers)
