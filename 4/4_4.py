class Node:
    r"""
    4.4 实现迭代器协议
    迭代器协议：一个对象提供next方法，访问迭代中的下一项，直到返回StopIteration异常，终止迭代。（可以利用生成器，已实现了next方法）

    实现一个以深度优先的方式遍历树的生成器
    >>> root = Node(1)
    >>> root.left = Node(2)
    >>> root.right = Node(3)
    >>> root.left.left = Node(4)
    >>> root.left.left.left = Node(5)
    >>> for n in root.depth_first():
    ...     print(n)
    Node(1)
    Node(2)
    Node(4)
    Node(5)
    Node(3)
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({!r})'.format(self.val)

    def __iter__(self):
        children = []
        children.append(self.left) if self.left else None
        children.append(self.right) if self.right else None
        return iter(children)

    def depth_first(self):
        yield self
        for ch in self:
            yield from ch.depth_first()


if __name__ == '__main__':
    import doctest
    doctest.testmod()