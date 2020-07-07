import functools


def after_func(func=None, *, print_str="end"):
    r"""
    9.6 带可选参数的装饰器

    我们使用装饰器时，习惯是
    @deco
    def f()
    =>
    f = f(deco)

    而不是
    @deco()
    def f()
    =>
    f = deco()(f)

    所以需要装饰器支持可选参数没，用partial实现，这里需要把将函数对象作为第一个参数传进来，其余参数强制为关键字参数，
    若为func=None，也就是@deco(print_str="hello")的情况，则通过functools.partial返回一个固定了其余参数的函数对象

    @deco(a=1)
    def func:
    =>
    func = deco(1)(f) => func = _partial(f)


    >>> @after_func
    ... def print_1(a, b, c):
    ...     print(a, b, c)

    >>> @after_func(print_str="hello")
    ... def print_2(a, b, c):
    ...     print(a, b, c)

    >>> print_1(1, 2, 3)
    1 2 3
    end

    >>> print_2(1, 2, 3)
    1 2 3
    hello
    """
    if func is None:
        return functools.partial(after_func, print_str=print_str)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(print_str)
        return result
    return wrapper


if __name__ == '__main__':
    import doctest
    doctest.testmod()
