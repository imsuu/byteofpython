from functools import reduce
'''高阶函数'''
f=abs
print(f)
print(f(-19))
print()
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

print('-----------------------------map/reduce')
'''map()传入的第一个参数是f1，即函数对象本身'''
def f1(x):
    return x*x
r=map(f1,[1,2,3])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def add(x,y):
    return x+y
print(reduce(add,[1,3,5])) #求和

def f2(x,y):
    return x*10+y
print(reduce(f2,[1,2,3]))  #变整数

def char2num(s):
    digits={'0':0,'1':1,'2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(f2,map(char2num,'231')))

'''
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
'''
'''lambda函数进一步简化
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
'''
print('------------')
def normalize(name):
    name=name[:1].upper()+name[1:].lower()
    return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x, y: x * y, L)
print(prod([1, 3, 5, 7, 9]))

def str2float(s):
    def add_two(x, y):
        return x * 10 + y
    s_list = s.split('.')  #划分
    s1, s2 = list(map(int, s_list[0])), list(map(int, s_list[1]))
    f1, f2 = reduce(add_two, s1), reduce(add_two, s2)/10**len(s2)
    return f1 + f2
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


print('-----------------------------filter筛选')
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
'''filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。'''
print('用filter求素数')
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
print('用filter确定回文数')
def is_palindrome(n):
    return str(n) == str(n)[::-1]
    #return lambda str(n)==str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
