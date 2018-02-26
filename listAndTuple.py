
classmates=['Anne','Bob','Tracy']
print(classmates)
print(len(classmates))

print(classmates[1])
print(classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.insert(1,'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']

'''元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改'''
t = (1, 2)
t1=(1)
t2=(1,)

t3=('a','b',['A','B'])
t3[2][0]='X'
t3[2][1]='Y'

print('---------------------------------------')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
