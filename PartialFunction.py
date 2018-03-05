import functools
'''偏函数'''
'''int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换'''
print(int('12345', base=8))
print(int('12345',16))

'''定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x, base)
print(int2('100000'))
'''
'''functools.partial帮助我们创建一个偏函数，不需要自己定义int2()，直接使用下面的代码创建一个新的函数int2'''
#import functools
int2=functools.partial(int, base=2)
print(int2('100000'))
print(int2('1000000', base=10)) #可以传入其他值
'''
创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)
实际上会把10作为*args的一部分自动加到左边
max2(1,2,6)
相当于
args = (10, 5, 6, 7)
max(*args)
结果为10
'''
