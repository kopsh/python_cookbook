import heapq


class PriorityQueue:
    r"""
    实现一个优先级队列
    怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素

    >>> class Item:
    ...     def __init__(self, val):
    ...         self.v = val
    ...     def __repr__(self):
    ...         return 'Item({!r})'.format(self.v)
    >>> q = PriorityQueue()
    >>> q.push(Item('a'), 4)
    >>> q.push(Item('b'), 4)
    >>> q.push(Item('c'), 3)
    >>> q.push(Item('a'), 1)
    >>> q.pop()
    Item('a')
    >>> q.pop()
    Item('b')
    >>> q.pop()
    Item('c')
    """
    def __init__(self):
        self.heap = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()