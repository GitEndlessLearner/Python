# 创建一个字典，包含熟人信息
friend = {
	'first_name': 'john',
	'last_name': 'hank',
	'age': '18',
	'city': 'Hubei'
}
print(friend)

# 遍历所有键'值和键值对
for key, value in friend.items():
	print(key,value)
for key in friend.keys():
	print(key)
for value in friend.values():
	print(value)

# 按顺序遍历
for key in sorted(friend.keys()):
	print(key)

