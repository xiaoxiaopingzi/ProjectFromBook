# -*- coding: UTF-8 -*-
"""使用 scatter() 绘制散点图并设置其样式"""
import matplotlib.pyplot as plt
# 使用实参 s 设置了绘制图形时使用的点的尺寸
x_values = list(range(1, 1001))
y_values = [x*x for x in x_values]
# plt.scatter(x_values, y_values, c="blue", edgecolor="none", s=30)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=30)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Number", fontsize=16)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 保存文件，第二个参数表示将图标多余的空白区域剪裁掉
plt.savefig("squares_plot.png", bbox_inches="tight")
