class Solution:
    r"""
    1.10 删除序列相同元素并保持顺序

    >>> l = [1, 1, 2, 3, 3, 1, 2, 4]
    >>> for i in Solution.solve(l):
    ...     print(i)
    1
    2
    3
    4
    """
    @staticmethod
    def solve(items):
        seen = set()
        for i in items:
            if i not in seen:
                yield i
                seen.add(i)


if __name__ == '__main__':
    import doctest
    doctest.testmod()