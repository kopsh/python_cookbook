# coding=utf-8

import threading
import time


class Solution:
    r"""
    12.2 判断线程是否已经启动

    Event 和 Condition
    event对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程，condition可以每次唤醒一个线程
    """

    def __init__(self):
        pass

    def solve(self):
        pass


def count_down(n, evt: threading.Event):
    print("counting down begin!")
    evt.set()
    while n > 0:
        n -= 1
        print(n)
        time.sleep(1)


class PeriodicTimer:

    def __init__(self, interval):
        self._interval = interval
        self._cv = threading.Condition()

    def cv(self):
        return self._cv

    def run(self):
        while True:
            with self._cv:
                self._cv.notify()
            time.sleep(self._interval)


def countdown(n, cv: threading.Condition):
    while n > 0:
        with cv:
            cv.wait()
            n -= 1
            print("countdown: ", n)


def countup(n, cv: threading.Condition):
    i = 0
    while i < n:
        with cv:
            cv.wait()
            i += 1
            print("countup: ", i)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # evt = threading.Event()
    # t = threading.Thread(target=count_down, args=(5, evt))
    # t.start()
    # evt.wait()
    # print("counting down is running!")

    p = PeriodicTimer(1)
    threading.Thread(target=p.run).start()
    threading.Thread(target=countdown, args=(5, p.cv())).start()
    threading.Thread(target=countup, args=(5, p.cv())).start()
