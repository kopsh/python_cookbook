import functools
import time


def timeit(ns=True):
    r"""
    9.1 在函数上添加包装器
    你想在函数上添加一个包装器，增加额外的操作处理(比如日志、计时等)

    >>> count_down.__name__
    'count_down'
    """
    if ns:
        _get_time = time.time_ns
        unit = 'ns'
    else:
        _get_time = time.time
        unit = 's'

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            start = _get_time()
            result = func(*args, **kwargs)
            end = _get_time()
            print("cost time: {}{}".format(end-start, unit))
            return result
        return inner
    return wrapper


@timeit()
def count_down(n):
    i = 0
    while i < n:
        i += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # count_down(10000000)
    count_down(10)
