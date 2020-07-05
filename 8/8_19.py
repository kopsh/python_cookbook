class Solution:
    r"""
    8.19 实现状态对象或者状态机

    状态模式
    >>> c = Connection()
    >>> c.open()
    >>> c.read()
    reading
    >>> c.write()
    writing
    >>> c.close()
    >>> c.close()
    Traceback (most recent call last):
    ...
    RuntimeError: Already Closed
    """
    def __init__(self):
        pass


class Connection:

    def __init__(self):
        self._state = CloseConnectionState

    def new_state(self, state):
        self._state = state

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)

    def read(self):
        return self._state.read(self)

    def write(self):
        return self._state.write(self)


class ConnectionState:
    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn):
        raise NotImplementedError()


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print("reading")

    @staticmethod
    def write(conn):
        print("writing")

    @staticmethod
    def open(conn):
        raise RuntimeError("Already Open")

    @staticmethod
    def close(conn):
        conn.new_state(CloseConnectionState)


class CloseConnectionState(ConnectionState):

    @staticmethod
    def read(conn):
        RuntimeError("Already Closed")

    @staticmethod
    def write(conn):
        RuntimeError("Already Closed")

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError("Already Closed")


if __name__ == '__main__':
    import doctest
    doctest.testmod()