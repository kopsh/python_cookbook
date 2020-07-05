class Solution:
    r"""
    8.25 创建缓存实例

    >>> from weakref import WeakValueDictionary
    >>> class Spam:
    ...     def __init__(self, name):
    ...         self.name = name
    >>> import weakref
    >>> _spam_cache = weakref.WeakValueDictionary()
    >>> def get_spam(name):
    ...     if name not in _spam_cache:
    ...         s = Spam(name)
    ...         _spam_cache[name] = s
    ...     else:
    ...         s = _spam_cache[name]
    ...     return s
    >>> a = get_spam('foo')
    >>> b = get_spam('foo')
    >>> a is b
    True
    """
    def __init__(self):
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()