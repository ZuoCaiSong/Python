#! usr/bin/env python
# -*- coding:utf-8 -*-

'''
class 后面紧接着是类名，即 Student ，类名通常是大写开头的单词，
紧接着是 (object) ，表示该类是从哪个类继 承下来的，继承的概念我们后面再讲，
通常，如果没有合适的继承类，就使用 object 类，这是所有类最终都会继承 的类。
'''

'''
注意到 __init__ 方法的第一个参数永远是 self ，表示创建的实例本身，
因此，在 __init__ 方法内部，
就可以把各 种属性绑定到 self ，因为 self 就指向创建的实例本身
'''

'''
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量 self ，并且，调用时，不用 传递该参数。
除此之外，类的方法和普通函数没有什么区别，
所以，你仍然可以用默认参数、可变参数和关键字参 数。
'''

'''
和静态语言不同，Python允许对实例变量绑定任何数据，
也就是说，对于两个实例变量，虽然它们都是同一个类的 不同实例，但拥有的变量名称都可能不同(属性名称可能会不同)
'''
class Student(object):
	def __init__(self,name,score):
		self.name = name 
		self.score = score 
	# 类的方法
	def print_score(self): 
		print '%s: %s' %(self.name, self.score)

zuocaisong = Student('zcs', 27)
lisa = Student('lisa', 87)

zuocaisong.print_score()
lisa.print_score()


''' 
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线 __ ，在Python中，实例的变量名如果
以 __ 开头，就变成了一个私有变量(private)，只有内部可以访问，外部不能访问，所以，我们把Student类改一 改:
'''
class Person(object):
	def __init__(self, sex):
		self.__sex = sex

	def print_PerInfo(self):
		print self.__sex

boy = Person("Man")
boy.print_PerInfo()

# print boy.__sex ,会报错：确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

# 给一个get方法，让他去访问

class  Car(object):
	def __init__(self, color):
		self.__color = color

	def get_clolor(self):
		return self.__color

bus = Car("white")
print bus.get_clolor()


# 如果又要允许外部代码修改score怎么办?可以给Student类增加 set_score 方法:

class  Car(object):
	def __init__(self, color):
		self.__color = color

	def set_color(self,color):
		self.__color = color

	def get_clolor(self):
		return self.__color

bus = Car("white")
print bus.get_clolor()

bus.set_color("red")
print bus.get_clolor()


'''
双下划线开头的实例变量是不是一定不能从外部访问呢?其实也不是。不能直接访问 __name 是因为Python解释器对 外把 __name 变量改成了 _Student__name ，所以，仍然可以通过 _Student__name 来访问 __name 变量:
               
外把 __name 变量改成了 _Student__name ，所以，仍然可以通过 _Student__name 来访问 __name 变量:

但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把 __name 改成不同的变量名。
总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
'''

# 继承
'''
继承有什么好处?最大的好处是子类获得了父类的全部功能。由于Animial实现了 run() 方法，因此，Dog和Cat作为
它的子类，什么事也没干，就自动拥有了 run() 方法:

当子类和父类都存在相同的 run() 方法时，我们说，子类的 run() 覆盖了父类的 run() ，
在代码运行的时候，总是 会调用子类的 run() 。这样，我们就获得了继承的另一个好处:多态。
'''
# 讲到多态时，先介绍一下类型的判断
print isinstance(bus, Car) # bus 是car类型

'''
所以，在继承关系中，如果一个实例的数据类型是某个子类，
那它的数据类型也可以被看做是父类。但是，反过来
就不行:
即： a = A("xx") ，a是A这个类生成的对象,A继承于B，则a是A类型，同时a也是B类型
'''


#获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢?

#基本类型都可以用 type() 判断:
print type(123)

#:如果一个变量指向函数或者类，也可以用 type() 判断:

print type(abs)
print type(bus)

'''
但是 type() 函数返回的是什么类型呢?它返回type类型。
如果我们要在 if 语句中判断，就需要比较两个变量的typ e类型是否相同:
'''
print type(123) == type(456)

#但是这种写法太麻烦，Python把每种type类型都定义好了常量，放在 types 模块里，使用之前，需要先导入:
import types
print types.StringType == type("zcs")
type(u'abc')==types.UnicodeType
type([]) == types.ListType
type(str)==types.TypeType #最后注意到有一种类型就叫 TypeType ，所有类型本身的类型就是 TypeType 

'''
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用 isinstance() 函数。
并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode:
'''
print"-------"
print isinstance(123,(str,unicode,int))

# 使用dir()

'''
如果要获得一个对象的所有属性和方法，可以使用 dir() 函数，它返回一个包含字符串的list，比如，获得一个str对
象的所有属性和方法:

类似 __xxx__ 的属性和方法在Python中都是有特殊用途的，比如 __len__ 方法返回长度。
在Python中，如果你调 用 len() 函数试图获取一个对象的长度，实际上，在 len() 函数内部，它自动去调用该对象的 __len__() 方法，
所 以，下面的代码是等价的
'''

print len("abc") 
print "abc".__len__()

#我们自己写的类，如果也想用 len(myObj) 的话，就自己写一个 __len__() 方法:

class  MyObject(object):
	"""docstring for  myObject"""
	def __init__(self, arg):
		self.arg = arg
		
	def __len__(self):
		return 100

obj = MyObject(13)
print len(obj)

'''
配合 getattr() 、 setattr() 以及 hasattr() ，我们可以直接操作一个对象的 状态:
'''

class MyObject1(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x 

obj = MyObject1()
print("hasattr")
print hasattr(obj, "x") #obj有属性'x'吗?

print hasattr(obj, "y") #obj有属性'y'吗?

setattr(obj, 'y', 19) #设置一个属性'y',值为19
print hasattr(obj, "y") #obj有属性'y'吗?

print getattr(obj,"y")

'''
注意： 如果试图获取不存在的属性，会抛出AttributeError的错误:
可以传入一个default参数，如果属性不存在，就返回默认值:
'''

print getattr(obj,'z', 404)

# 也可以获得对象的方法:
print hasattr(obj, 'power')

fn = getattr(obj,'power')
print fn() # 调用fn()与调用obj.power()是一样的

'''
小结: 可以直接访问（obj.x  obj.power()），尽量不要用这种方式访问属性，和方法。
'''


# 动态绑定方法，和属性

class Student(object):
	pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print s.name

# 给实例绑定一个方法
def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student) # 给实例绑定一个方法

s.set_age(25)  # 调用实例方法
print s.age   # 测试结果

'''
但是，给一个实例绑定的方法，对另一个实例是不起作用的:只作用当前实例s。

为了给所有实例都绑定方法，可以给class绑定方法:
给class绑定方法后，所有实例均可调用:
动态绑定允许我们在程序运行的过程中动态给class 加上功能，这在静态语言中很难实现。
'''

def set_Score(self, score):
	self.score = score

Student.set_Score = MethodType(set_Score, None, Student)

s.set_Score(100)
print s.score


'''
只允许对Student实例添加 name 和 age 属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的 __slots__ 变量，来限制该class能添加的属 性:

使用 __slots__ 要注意， __slots__ 定义的属性仅对当前类起作用，对继承的子类是不起作用的:
除非在子类中也定义 __slots__ ，这样，子类允许定义的属性就是自身的 __slots__ 加上父类的 __slots__ 。
'''
class Student(object):
	__slots__ = ('name', 'age') # 用tuple定义只能允许绑定的属性名称

s = Student()
#s.score = 90
# print s.score  : error: Student' object has no attribute 'score'

class GraduateStudent(Student):
	__slots__ = ("score")

g = GraduateStudent()
g.name = "xiaoming"
print g.name


# @property
class Student(object):

 	def get_score(self):
 		return self._score
    # 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了:
 	def set_score(self, value):
 		if not isinstance(value, int):
 			raise ValueError('score must be an integer!')
 		elif value <0 or value> 100:
 			raise ValueError('score must between 0 ~ 100!')
 		else:
 			self.score = value

#此时操作赋值为：
s = Student()
s.set_score(60)

'''
# Python内置 的 @property 装饰器就是负责把一个方法变成属性调用的:
@property 的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上 @property 就可以 了，
此时， @property 本身又创建了另一个装饰器 @score.setter ，负责把一个setter方法变成属性赋值，
于是，我 们就拥有一个可控的属性操作:

注意到这个神奇的 @property ，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过gett er和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性:

'''

class Student(object):

	@property 
	def score(self):
		return self._score 


	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		elif value < 0 or value > 100:
			raise ValueError('score must between 0 ~100!')
		else:
			self._score = value

s = Student()
s.score = 99
print s.score

'''
还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性:
'''
class Student(object):
	@property 
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return  2014 - self._birth
#而 age 就是一个只读属性，因为 age 可以根据 birth 和当前时间计算出来。


# 重新定义打印对象,只需要定义好 __str__() 方法，返回一个好看的字符串就可以了:

'''
因为直接显示变量s 调用的不是 __str__() ，而是 __repr__() ，
两者的区别是 __str__() 返回用户看到的字符 串，
而 __repr__() 返回程序开发者看到的字符串，
也就是说， __repr__() 是为调试服务的。

解决办法是再定义一个 __repr__() 。
但是通常 __str__() 和 __repr__() 代码都是一样的，
所以，有个偷懒的写 法: __repr__ = __str__
'''
class Student(object):
	def  __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__
Student('Michael')
print Student('Michael')



print  "------------  __iter__ -------------"
'''
如果一个类想被用于 for ... in 循环，类似list或tuple那样，就必须实现一个 __iter__() 方法，该方法返回一个迭 代对象，
然后，Python的for循环就会不断调用该迭代对象的 next() 方法拿到循环的下一个值，直到遇到StopIterati on错误时退出循环
'''
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1 # 初始化两个计数器a，b

	def __iter__(self):
		return self #实力本身就是迭代对象，对返回自己

	def next(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值
		if self.a > 1000: #退出循环条件
			raise StopIteration();
		return self.a


for n in Fib():
	print n

print  "------------  __getitem__  -------------"

#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素:
#要表现得像list那样按照下标取出元素，需要实现 __getitem__() 方法:
class Fib(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a
f = Fib()
print f[5]


'''
正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义 Student 类:
 
'''
print  "  __getattr__  "

class Student(object):
	def __init__(self):
		self.name = 'Michael'
s = Student()
print s.name

'''
Python还有另一个机制，那就是写一个 __getattr__() 方
法，动态返回一个属性。修改如下:
'''
class Student100(object):
	def __init__(self):
		self.name = 'Michael'

	def  __getattr__(self, attr):
		if attr == 'score':
			return 99
'''
当调用不存在的属性时，
比如 score ，Python解释器会试图调用 __getattr__(self, 'score') 来尝试获得属性，
这 样，我们就有机会返回 score 的值:

注意：
只有在没有找到属性的情况下，才调用 __getattr__ ，已有的属性，比如 name ，不会在 __getattr__ 中查 找。
此外，注意到任意调用如 s.abc 都会返回 None ，这是因为我们定义的 __getattr__ 默认返回就是 None 。
要让class 只响应特定的几个属性，我们就要按照约定，抛出 AttributeError 的错误
'''

s = Student100()
print s.name
print s.score

print s.shdfs




print "----------------- __call__---------------"
'''
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用 instance.method() 来调用。能不能直接在 实例本身上调用呢?类似 instance() ?在Python中，答案是肯定的。
任何类，只需要定义一个 __call__() 方法，就可以直接对实例进行调用。请看示例:
'''


class StudentCall(object):
	def __init__(self,name):
		self.name = name

	def __call__(self):
		print("my name is %s" % self.name)


s =  StudentCall("jeck")
print s()

'''
怎么判断一个变量是对象还是函数呢


其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用 的对象就是一个 Callable 对象，比如函数和我们上面定义的带有 __call()__ 的类实例:

通过 callable() 函数，我们就可以判断一个对象是否是“可调用”对象。
'''

print callable(s)  # true

print callable('str') #false
