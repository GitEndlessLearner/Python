import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 绘制一个点
plt.scatter(input_values, squares, s=400)

# 自动生成数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
print(y_values)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)


plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()