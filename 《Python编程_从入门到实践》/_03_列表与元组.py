# 主要练习第三章的相关内容

# 创建列表
classmates = ['li mei', 'wang wu', 'zhang san']

# 访问元素
for name in classmates:
	print(name.title()+' ! How are you,my friend~')

# 修改元素
classmates[0] = 'wang gang'
print(classmates[0])

# 末尾添加元素
classmates.append('zhao si')
print(classmates)

# 插入元素
classmates.insert(0,'li gang')
print(classmates)

# 删除制定索引的元素
del classmates[0]
print(classmates)

# 删除并弹出某处的元素
new_classmates = classmates.pop(2)
print(new_classmates)

# 删除某个指定值
classmates.remove('wang wu')
print(classmates)

# 邀请一群人共进午餐，并对名单进行增删改；
DinnerList = ['a', 'b', 'c']
for name in DinnerList:
	print(name,'come on!')

print('After a while')

NotInList = DinnerList.pop(0)
print('What a pity!',NotInList,"won't come ")
for name in DinnerList:
	print(name,'come on!')

print('We have a bigger table!')
DinnerList.insert(0,'d')
print(DinnerList)

# 使用sort()对列表进行排序
Listname = ['b', 'a', 'c']
Listname.sort()
print(Listname)
Listname.sort(reverse=True)
print(Listname)

# 使用sortd()临时排序
print(sorted(Listname),Listname)
