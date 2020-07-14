# coding=utf8
"""
12.11 实现消息发布/订阅模型
"""
import collections
from contextlib import contextmanager


class Exchange:

    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


exchanges = collections.defaultdict(Exchange)


def get_exchange(name):
    return exchanges[name]


class Task:

    def send(self, msg):
        print(msg)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    ex = get_exchange("name")
    task1 = Task()
    task2 = Task()
    with ex.subscribe(task1, task2):
        ex.send("hello")
