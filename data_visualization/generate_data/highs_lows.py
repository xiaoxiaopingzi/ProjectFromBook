# -*- coding: UTF-8 -*-
"""分析csv文件"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"
# 从文件中获取最高气温
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)  # ,号表示用空格隔开

    dates, highs, lows = [], [], []
    for row in reader:
        # 使用try-except-else来跳过错误数据
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "miss data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print("highs", highs)
    # print(dates)

# 根据数据绘图
# 设置绘图窗口的尺寸,默认1英寸为80像素，可以使用dpi=80来调整分辨率
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, linewidth=1, c="red")  # x轴默认从0开始取值
plt.plot(dates, lows, linewidth=1, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=16)
plt.xlabel("", fontsize=14)
# 调用了fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()


