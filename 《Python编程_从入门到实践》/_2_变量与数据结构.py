# 本篇主要练习第二章代码内容

# 多次修改变量并打印
name = 'li long'
print(name)
name = 'omg no'
print(name)

# 利用title()方法，让首字母大写
print(name.title())

# 利用upper()方法和lower()方法让字母全部大写或者小写
print(name.upper())
print(name.lower())

# 拼接多个字符串
print(name.upper()+" "+name.lower())

# 在字符串里使用制表符或者换行符来则更加空白
print('hello \t  boy')

# 在字符串里添加换行符，自动换行,'\n\t'表示换行并自动空格
print('hello \n boy')

# 删除尾部的字符，rstrip()默认空格，可在括号里指定内容；
test = '   hahaha   '
print(len(test))
print(len(test.rstrip()))

