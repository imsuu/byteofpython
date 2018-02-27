import math
'''调用函数'''
print(abs(-1.1))
print(max(1,-1,3,2))

print('-----------------------------')
'''数据类型转换'''
print(int('132'))
print(int(12.54))
#print(int('12.54')) 不可以
print(float('12.6'))
print(str(1.23))
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(''))
print(hex(255))

print('-----------------------------')
'''函数名其实就是指向一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”'''
aa=abs
print(aa(-11))

print('-----------------------------')
'''定义函数'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-1.2))

'''空函数'''
def nop():
    pass

print('-----------------------------')
'''参数检查'''
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#print(my_abs2('1.2'))

print('-----------------------------')
'''返回多个值'''
'''函数可以同时返回多个值，但其实就是一个tuple'''
#import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

def quadratic(a,b,c):
    if not isinstance(a,(int,float))&isinstance(b,(int,float))&isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    if a==0:
        return -c/b
    else:
        t=b*b-4*a*c
        if t>=0:
            x1=(-b+math.sqrt(t))/(2*a)
            x2=(-b-math.sqrt(t))/(2*a)
            return x1,x2
        else:
             print('你输入的一元二次方程无实数解')
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

print('-----------------------------')
'''函数的参数'''
'''
def power(x):
    return x * x
'''
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

'''默认参数必须指向不变对象'''

print('----------------------------可变参数')
'''可变参数'''
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

print(calc((1, 3, 5, 7)))
print(calc([1, 2, 3]))
print('----------------------------')
def calc1(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc1(1,2,3))
nums=[1,2,3]
print(calc1(*nums))

print('----------------------------555')
def product(*numbers):
    if numbers:
        mul=1
        for n in numbers:
            mul=mul*n
        return mul
    else:
        raise TypeError

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

print('----------------------------递归函数')
'''递归函数'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(1))
print(fact(5))

print('----------------------------汉诺塔')
def move(n,a,b,c):
    if n==1:                #当n==1时，直接从a移动到c
        print(a,"-->",c)    #直接输出a到c
    else:
        move(n-1,a,c,b)     #先将a上除了最大底盘外的所有圆盘(n-1个)移动到b
        move(1,a,b,c)       #再将a上的最大底盘移动到c
        move(n-1,b,a,c)     #最后将b上的所有圆盘(n-1个)移动到c

move(4, 'A', 'B', 'C')
