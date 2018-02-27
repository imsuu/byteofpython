from collections import Iterable
print('-----------------------------------切片')
'''L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[1:3])
print(L[0:2])
print(L[-2:-1])

L2 = list(range(100))
print(L2[:10:2])
print(L2[::5])


def trim(s):
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]==' ':
        s=s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

print('-----------------------------------迭代')
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k,v)

'''通过collections模块的Iterable类型判断是否可以迭代'''
#from collections import Iterable
print(isinstance('abc', Iterable))# str是否可迭代
print( isinstance([1,2,3], Iterable))# list是否可迭代
print(isinstance(123, Iterable))# 整数是否可迭代

'''Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身'''
for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinAndMax(L):
    if L:
        max = min = L[0]
        for x in L:
            if x > max:
                max = x
            if x < min:
                min = x
        return (min, max)
    else:
        return (None, None)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

print('-----------------------------------列表生成式')
print(list(range(1, 11)))
print(list([x * x for x in range(1, 11)]))
print(list([x * x for x in range(1,11) if x % 2 == 0]))
print(list(m + n for m in 'ABC' for n in 'XYZ'))

import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录
