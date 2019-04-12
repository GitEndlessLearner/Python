# 第四章的代码练习

# 把三种水果放到一个列表里，循环打印
'''
FrultList = []
while len(FrultList) <3:
	frult_name = input("What frult do you like?\n")
	FrultList.append(frult_name)

for frult in FrultList:
	print('You like',frult)
'''

# 创建数值列表
print(list(range(4)))

# 创建10以内的偶数列表
print(list(range(0,11,2)))

# 数字列表中的最大最小和总和
NumList = range(0,11,2)
print(min(NumList),max(NumList),sum(NumList))

# 利用列表解析，快速生成一行列表
List = [number**2 for number in range(0,11,2)] 
print(List)

# 列表切片
print(list(range(4))[2:4])

# 复制列表
ListDouble = List[:]
print(ListDouble)

'''
	有一家自助式餐馆，只提供五种简单的食物，存储在一个元祖里
	遍历打印
'''
FoodList = ('apple','banana','chicken')
for food in FoodList:
	print(food)