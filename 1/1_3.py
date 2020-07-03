from collections import deque


class Solution:
    r"""
    1.3 保留最后N个元素，例如读取一个大文本，保留最后N行数据
    方案：使用collections.deque 双端队列，设置maxlen，自动移除元素
    >>> l = [1,234,34,64,1,34,235,23,2,524,3423,42,3,4]
    >>> s = Solution(5)
    >>> for e in l:
    ...     s.solve(e)
    >>> for e in s.last_n():
    ...     print(e)
    524
    3423
    42
    3
    4
    """
    def __init__(self, n):
        self.q = deque(maxlen=n)

    def solve(self, e):
        self.q.append(e)

    def last_n(self):
        for e in self.q:
            yield e

if __name__ == '__main__':
    import doctest
    doctest.testmod()