# -*- coding: UTF-8 -*-
import pygal

try:
    from die import Die
except ImportError:
    raise ImportError('The file is not found. Please check the file name!')
# 创建一个D6
die_1 = Die()
die_2 = Die(10)

# 掷两次骰子，并将两次投掷的结果相加并存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []  # 存储每种结果出现的次数
xList = []       # 存储投掷出现的结果
# 两个D6投掷的结果之和的最大值是12，最小值为2
max_result = die_1.num_sides + die_2.num_sides
# print(list(range(6)))  # range()函数不包括结尾的数字
for value in range(2, max_result + 1):
    xList.append(str(value))
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化，画柱状图
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times"
# 柱状图的x轴
hist.x_labels = xList
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)  # 每一个柱子需要一个标签
hist.render_to_file("die_visual_a D6 and a D10.svg")

print(frequencies)
