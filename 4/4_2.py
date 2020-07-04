class Solution:
    r"""
    4.2 代理迭代
    构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。 你想直接在你的这个新容器对象上执行迭代操作。

    使用__iter__
    >>> root = Solution.solve()
    >>> for ch in root:
    ...     print(ch)
    Node(2)
    Node(3)
    """
    @staticmethod
    def solve():

        class Node:
            def __init__(self, val):
                self.val = val
                self.children = []

            def add(self, n):
                self.children.append(n)

            def __repr__(self):
                return 'Node({!r})'.format(self.val)

            def __iter__(self):
                return iter(self.children)

        root = Node(1)
        root.add(Node(2))
        root.add(Node(3))
        return root

if __name__ == '__main__':
    import doctest
    doctest.testmod()