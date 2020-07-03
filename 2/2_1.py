class Solution:
    r"""
    2.1 使用多个界定符分割字符串

    >>> s = '1!2@3#4$$5%6'
    >>> pattern = '[!@#\$%]+'
    >>> Solution.solve(s, pattern)
    ['1', '2', '3', '4', '5', '6']
    """
    @staticmethod
    def solve(s, pattern):
        import re
        return re.split(pattern, s)


if __name__ == '__main__':
    import doctest
    doctest.testmod()