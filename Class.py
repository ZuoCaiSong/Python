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


