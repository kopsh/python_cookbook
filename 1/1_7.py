class Solution:
    r"""
    1.7 字典排序
    你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

    >>> s = Solution()
    >>> print(s.solve())
    {"1": 1, "2": 2, "3": 3, "4": 4}
    """
    def __init__(self):
        import collections
        self.d = collections.OrderedDict()

    def solve(self):
        self.d[1] = 1
        self.d[2] = 2
        self.d[3] = 3
        self.d[4] = 4

        import json
        return json.dumps(self.d)


if __name__ == '__main__':
    import doctest
    doctest.testmod()