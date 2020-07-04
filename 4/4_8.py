class Solution:
    r"""
    4.8 跳过可迭代对象的开始部分

    使用itertools.dropwhile
    >>> from itertools import dropwhile
    >>> l = ['a', 'b', 'c', '1', '2', '3']
    >>> for i in dropwhile(lambda i: i.isalpha(), l):
    ...     print(i)
    1
    2
    3
    """
    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()