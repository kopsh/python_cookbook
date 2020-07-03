class Solution:
    r"""
    1.13 通过某个关键字排序一个字典列表

    使用operater模块的itemgetter方法
    >>> l = [{"id": 1, "name": "c"}, {"id": 2, "name": "b"}, {"id": 3, "name": "a"}]
    >>> Solution.solve(l)
    [{'id': 3, 'name': 'a'}, {'id': 2, 'name': 'b'}, {'id': 1, 'name': 'c'}]
    """
    @staticmethod
    def solve(l):
        from operator import itemgetter
        return sorted(l, key=itemgetter('name'))


if __name__ == '__main__':
    import doctest
    doctest.testmod()