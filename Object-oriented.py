class Student(object):

    def __init__(self, name, score):  #实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
'''
    def __init__(self, name, score):   #第一个参数永远是self，表示创建的实例本身.调用时，不用传递该参数
        self.name = name
        self.score = score
'''
'''变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量'''

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
#print(bart.name, bart.get_grade())
#print(lisa.name, lisa.get_grade())

print('-------------------------------------Student2')
class Student2(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if str.lower(gender)=='female' or str.lower(gender)=='male':
            self.__gender = gender
        else:
            raise ValueError('bad gender')

bart = Student2('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
