'''
# 输入名称
name = input('Your name,sir?\n')
print('Hello,',name)
'''

'''
编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨
中添加这种配料。
'''
'''
while True:
	PizzaFilling = input('Which filling do you want?\n')
	if PizzaFilling == 'quit':
		print('Good Bye~')
		break
	elif PizzaFilling == 'no':
		print('ok')
		continue
	print('We will add ',PizzaFilling)
'''