age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age>=6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')

print('--------------------------')
'''input 输入为字符串'''
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

print('--------------------------')
height = 1.75
weight = 80.5

bmi=weight/(height*height)
if bmi<18.5:
    print("过轻")
elif bmi<25:
    print("正常")
elif bmi<28:
    print("过重")
elif bmi<32:
    print("肥胖")
else:
    print("严重肥胖")
