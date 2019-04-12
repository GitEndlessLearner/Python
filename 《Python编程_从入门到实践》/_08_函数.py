# 创建包含一个形参的函数
def display_message(title):
	print('I like reading',title)
display_message('books')

# 创建一个宠物狗的关键字函数，名称和年龄,赋予一个默认值,返回一个字典
def Cat(age, name='', color='black'):
	print('I have a ',age,'year-old',color,'dog named',name)
	MyCat = {'name': name, 'age': age, 'color': color}
	return MyCat
Cats = Cat(age='13', name='john')
print(Cats)

# 向函数传递列表
def users(name):
	for names in name:
		print(names)
name = [1,2,3,4,5]
users(name)

# 传递任意数量的实参
def make_pizza(*fillings):
	print(fillings)
make_pizza(1,2,3,4,5)

'''
导入模块 import
导入特定函数 from [模块] import [函数1],[函数2]
指定别名 import [模块] as [别名]
导入所有函数 import *

'''
