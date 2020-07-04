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
* 5.8 固定大小记录的文件迭代（iter(functools.patial(f.read, SIZE), b'')）
* 5.10 内存映射的二进制文件（mmap）
 