# 创建一个类： 狗

class Dog():
	"""docstring for Dog"""

	def __init__(self, name,age):
		self.name = name
		self.age = age

	def sit(self):
		"""坐下指令"""
		print(self.name,'is sitting')

"""创建实例"""
MyDog = Dog('xiaohong','15')
print(MyDog.name,MyDog.age)
MyDog.sit()


# 创建一个子类：小狗,并定义属性和方法
class LittleDog(Dog):
	""" 小狗作为狗的子类 """
	
	def __init__(self, name, age):
		super().__init__(name, age)
		self.speed = '0'

	def speedone(self,speednumber):
		self.speed = speednumber

MyLittleDog = LittleDog('xiaozhang','2')
print(MyLittleDog.name)
MyLittleDog.speedone('5')
print(MyLittleDog.speed)

