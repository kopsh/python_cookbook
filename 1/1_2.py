def slove():
    r"""
    1.2 解压可迭代对象赋值给多个变量

    >>> l = [1, 2, 3, 4, 5]
    >>> a, b, *c = l
    >>> c
    [3, 4, 5]
    >>> a
    1
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()