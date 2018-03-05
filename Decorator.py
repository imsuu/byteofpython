'''装饰器'''
'''
def now():
    print('2018-3-5')

f=now
f()
'''
#函数对象有一个__name__属性，可以拿到函数的名字
'''print(now.__name__)
print(f.__name__)
'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-3-5')

f=now
f()

'''把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)'''

'''后面不想管了。。。。。。'''
