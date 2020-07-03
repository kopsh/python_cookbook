import heapq


class Solution:
    r"""
    1.4 最大或最小的N个元素

    使用heapq
    >>> s = Solution()
    >>> l = [6,3,8,2,1,7,9,2]
    >>> s.solve(l, 3)
    [1, 2, 2]
    >>> s.solve(l, 3, True)
    [9, 8, 7]
    """
    def __init__(self):
        pass

    def solve(self, l, n, reverse=False):
        if reverse:
            return heapq.nlargest(n, l)
        else:
            return heapq.nsmallest(n, l)


if __name__ == '__main__':
    import doctest
    doctest.testmod()