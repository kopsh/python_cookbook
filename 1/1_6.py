class Solution:
    r"""
    1.6 字典中的键映射多个值

    使用collections.defaultdict

    >>> s = Solution()
    >>> s.solve()
    defaultdict(<class 'list'>, {'a': [1, 2], 'b': [1]})
    """
    def __init__(self):
        import collections
        self.d = collections.defaultdict(list)

    def solve(self):
        self.d['a'].append(1)
        self.d['a'].append(2)
        self.d['b'].append(1)
        return self.d


if __name__ == '__main__':
    import doctest
    doctest.testmod()