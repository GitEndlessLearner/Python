# 打开一个文件
with open ('test.txt') as test1:
	contents = test1.read()
	print(contents)
	"""逐行读取,因为原文本有换行符所以这里多出一行"""
	for line in test1.read():
		print(line.rstrip())

# 写入空文件
filename = 'test2.txt'

with open('test2.txt','w') as test2:
	test2.write('hello world')

# 使用try- except来抛出异常
try:
	print(5/0)
except ZeroDivisionError:
	print('There is something wrong')
else:
	print('You are right')
finally:
	pass

# 分析文本-提取文本
try:
	with open('test.txt') as test:
		contents = test.read()
except FileExistsError:
	print('wrong')
else:
	words = contents.split()
	print(words)

import json
number = [1,2,3,4,5,6,7,8]
filename = 'test3.json'
with open('test3.json','w') as test3:
	json.dump(number,test3)
with open(filename) as test3:
	number = json.load(test3)
	print(number)

# 提示用户输入喜欢的数字，保存到json格式文件，再读取打印；
FavNum = input('Which number do you like?')
filename = 'test4.json'
with open(filename,'w') as test4:
	json.dump(FavNum,test4)
with open(filename) as test5:
	Numbers = test5.read()
	print(Numbers,'hello')


