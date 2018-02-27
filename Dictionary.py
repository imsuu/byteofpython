d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

print('Thomas' in d)

print(d.get('Tom'))
print(d.get('Tom',-2))

d.pop('Bob')
print(d)

'''dict的key必须是不可变对象
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：'''

print('---------------------------------')
'''set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。'''
s=set([1,2,3])
print(s)

s.add(4)
print(s)
s.add(1)
print(s)

s.remove(2)

print('---------------------------------')
s1=set([1,2,3,'s'])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)

print('----------------------------------')
'''str是不变对象，而list是可变对象'''
a=['c','b','a']
a.sort()
print(a)

st='abc'
print(st.replace('a','A'))
print(st)
