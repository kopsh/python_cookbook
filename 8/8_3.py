class Solution:
    r"""
    8.4 创建大量对象时节省内存方法

    __slots__其实是一个内存优化工具。当定义__slots__后，Python就会为实例使用一种更加紧凑的内部表示。实例通过固定大小的数组来构建，
    而不是字典的形式。使用slots后，我们将不能再为实例添加新的属性。

    Python官网：
    __slots__ allow us to explicitly declare data members (like properties) and deny the creation of __dict__
     and __weakref__ (unless explicitly declared in __slots__ or available in a parent.)

    __slots__允许我们显示地声明成员，并且拒绝为对象创建__dict__和__weakref__属性（除非它已在父类或自身的__slot__中）

    The space saved over using __dict__ can be significant. Attribute lookup speed can be significantly improved
    as well.

    不使用__dict__让内存使用情况大幅改善，属性查询的效率也有较大的的提升。
    """
    def __init__(self):
        pass

    def solve(self):
        pass


class A:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class B:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    a = [A(i, i, i) for i in range(10000)]
    first_size, first_peak = tracemalloc.get_traced_memory()
    b = [B(i, i, i) for i in range(10000)]
    second_size, second_peak = tracemalloc.get_traced_memory()
    print(first_size, first_peak)
    print(second_size, second_peak)
