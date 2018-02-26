print("I\'m \"ok\"!")

print("I\'m learning \npython")

print("\\\n\\")

print('\\\t\\')

print(r'\\\t\\')

print('''line1
line2
line3''')

print(r'''hello,\n
world''')

print("-------------------------")

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
'''理解变量在计算机内存中的表示也非常重要。当我们写：
a = 'ABC'时，Python解释器干了两件事情：
在内存中创建了一个'ABC'的字符串；
在内存中创建了一个名为a的变量，并把它指向'ABC'。'''
a = 'ABC'
b = a
a = 'XYZ'
print('b=',b)

print("-------------------------")
'''Python中，通常用全部大写的变量名表示常量,用r''表示''内部的字符串默认不转义'''
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
