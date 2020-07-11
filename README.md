# python_cookbook

[《Python Cookbook》3rd Edition](https://python3-cookbook.readthedocs.io/zh_CN/latest/copyright.html)
代码示例
### 1 数据结构与算法
### 2 字符串与文本
### 3 数字与日期
### 4 迭代器与生成器
* 4.1 手动遍历迭代器（next）
* 4.2 代理迭代（对象中含有可迭代的属性）
* 4.3 使用生成器创建迭代（yield）
* 4.4 实现迭代器协议（\_\_iter\_\_）
* 4.7 迭代器切片（itertools.islice）
* 4.8 跳过可迭代对象的开始部分（itertools.dropwhile）
* 4.9 排列组合的迭代（itertools.permutation/combinations）
* 4.10 序列上索引值迭代（enumerate）
* 4.11 同时迭代多个序列（zip）
* 4.12 不同集合上元素的迭代（itertools.chain）
* 4.14 展开嵌套的序列（yield from）
* 4.15 顺序迭代合并后的排序迭代对象（heapq.merge）
* 4.16 迭代器代替while无限循环（iter(_iter, sentinal)）
### 5 文件与IO
* 5.3 使用其他分隔符或行终止符打印 (print(*arg, sep=',', end='!'))
* 5.6 字符串的I/O操作（io.String/ByteIO，模拟文件对象）
* 5.8 固定大小记录的文件迭代（iter(functools.partial(f.read, SIZE), b'')）
* 5.10 内存映射的二进制文件（mmap）
* 5.19 创建临时文件和文件夹（tempfile）
* 5.21 序列化Python对象（pickle）
### 6 数据的编码与处理
* 6.11 读写二进制数组数据（struct）
### 7 函数
* 7.2 只接受关键字参数的函数（关键字参数放到某个\*参数或者单个\*后面）
* 7.3 给函数参数增加元信息（\_\_annotations__，主要用于文档）
* 7.6 定义匿名或内联函数（lambda）
* 7.8 减少可调用对象的参数个数（functools.partial）
* 7.12 访问闭包中定义的变量
### 8 类与对象
* 8.1 改变对象的字符串显示（\_\_repr__和\_\_str__）
* 8.3 让对象支持上下文管理协议（\_\_enter__和\_\_exit__、contextmanager）
* 8.4 创建大量对象时节省内存方法（\_\_slots__）
* 8.6 创建可管理的属性（property）
* 8.7 调用父类的方法（super）
* 8.9 创建新的实例属性（描述器类，例如类型检查）
* 8.13 实现数据模型的类型约束（描述器，元类，或者使用装饰器）
* 8.14 实现自定义容器（collections中的抽象类）
* 8.15 属性的代理访问（代理模式）
* 8.18 利用Mixins扩展类功能（多继承的使用）
* 8.19 实现状态对象或者状态机（状态模式）
* 8.20 通过字符串调用对象方法（getattr）
* 8.21 实现访问者模式（python递归限制 sys.getrecursionlimit）
* 8.22 不用递归实现访问者模式（利用栈和生成器消除递归）
* 8.23 循环引用数据结构的内存管理（创建weakref消除循环引用）
* 8.24 让类支持比较操作（functools.total_ordering，只需定义lt与ge即可实现全部比较）
* 8.25 创建缓存实例（weakref.WeakValueDictionary）
### 9 元编程
* 9.1 在函数上添加包装器（装饰器）
* 9.2 创建装饰器时保留函数元信息（functools.wrap）
* 9.3 解除一个装饰器（__wrapper)
* 9.5 可自定义属性的装饰器（nolocal）
* 9.6 带可选参数的装饰器
* 9.7 利用装饰器强制函数上的类型检查（inspect.signature 以及 bind_partial）
* 9.9 将装饰器定义为类
* 9.13 使用元类控制实例的创建
### 11 web与网络编程
* 11.2 创建TCP服务器
* 11.3 创建UDP服务器
* 11.8 实现远程方法调用
* 11.12 理解事件驱动的IO