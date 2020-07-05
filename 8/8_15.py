class Solution:
    r"""
    8.15 属性的代理访问

    >>> b = B(1)
    >>> print(b.a)
    val: 1
    """
    def __init__(self):
        pass


class A:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "val: " + str(self.val)


class B:
    def __init__(self, val):
        self.a = A(val)


if __name__ == '__main__':
    import doctest
    doctest.testmod()