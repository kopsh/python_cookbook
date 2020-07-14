import time
from threading import Thread


class CountDown(Thread):
    r"""
    12.1 启动与停止线程

    """
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            self.n -= 1
            print(self.n)
            time.sleep(2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    c = CountDown(10)
    c.start()
    c.join(timeout=10)
    print("End!")
