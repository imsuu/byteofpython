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

'''for循环可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value'''
d1={'x':'1','y':'2','z':'3'}
for k,v in d1.items():
    print(k,'=',v)

print([k + '=' + v for k, v in d1.items()])

L3=['Hello','World']
print([s.lower() for s in L3])

L4=['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L4 if isinstance(s,str)])

print('-----------------------------------生成器')
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print()
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print()
print(fib(6))
print()
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
print()
def triangles():
    l = [1]
    while 1:
        yield l
        l = [1] + [l[n] + l[n + 1] for n in range(len(l) - 1)] + [1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

print('----------------------------迭代器')
'''凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的'''

for x in [1, 2, 3, 4, 5]:
    pass
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
