import pickle
from multiprocessing import connection
import datetime
import threading


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv().encode())
                try:
                    result = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(result))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


class RPCServer:
    def __init__(self, handler, address, authkey=b"rpc"):
        self.handler = handler
        self.address = address
        self.authkey = authkey

    def serve_forever(self):
        sock = connection.Listener(address=self.address, authkey=self.authkey)
        while True:
            client = sock.accept()
            t = threading.Thread(target=self.handler.handle_connection, args=(client,))
            t.daemon = True
            t.start()


def add(x, y):
    return x + y


def now():
    return datetime.datetime.now()


class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result

        return do_rpc


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('mod', type=str, help="server or proxy")
    args = parser.parse_args()

    mod = args.mod

    if mod == 'server':
        handler = RPCHandler()
        handler.register(add)
        handler.register(now)
        server = RPCServer(handler, ("", 20001), b"rpc")
        server.serve_forever()
    elif mod == 'proxy':
        client = connection.Client(address=("localhost", 20001), authkey=b"rpc")
        proxy = RPCProxy(client)
        print(proxy.add(1, 2))
        print(proxy.now())
