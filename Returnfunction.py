from functools import reduce
'''返回函数'''
'''
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum


f=lazy_sum(1,3,5)
print(f)  #调用lazy_sum()时，返回的并不是求和结果，而是求和函数
print(f())  #调用函数f时，才真正计算求和的结果

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)  #调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
'''
def f():
    print('call f()...')
    # 定义函数g:
    def g():
        print('call g()...')
    # 返回函数g:
    return g
x=f()  #call f()...
print(x)
x()  #call g()...

def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum

'''请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。 '''
'''思想:先定义能计算乘积的函数，再将这个函数返回'''
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod

f = calc_prod([1, 2, 3, 4])
print(f())


def createCounter():
    def g():
        n = 0
        while True:
            n = n + 1
            yield n
    it = g()
    def counter():
        return next(it)
    return counter


def createCounter2():
    s=[0]
    def counter():
        s[0]=s[0]+1
        return s[0]
    return counter
