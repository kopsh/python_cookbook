def solve(l: list):
    r"""
    1.1 将序列分解为单独的变量

    >>> l = [1, '2', "c", "d"]
    >>> a, b, c, d = solve(l)
    >>> a
    1
    >>> b
    '2'
    """
    a, b, c, d = l
    return a, b, c, d


if __name__ == "__main__":
	import doctest
	doctest.testmod()