# -*- coding: UTF-8 -*-
"""
执行API调用并存储响应,分析GitHub上的数据

大多数API都存在速率限制，即你在特定时间内可执行的请求数存在限制:
    https://api.github.com/rate_limit页面中的search项
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print(response_dict.keys())
print("Total repositories:", response_dict["total_count"])

# 探索有关仓库的信息
repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    description = repo_dict['description']
    # description可能为None,此时需要直接赋值为'None'
    if not description:
        description = "None"
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']  # 将图表中的每个条形用作网站的链接
    }
    plot_dicts.append(plot_dict)

# print(plot_dicts)
# 可视化
# 使用LightenStyle类（别名LS）定义了一种样式，并将其基色设置为深蓝色
my_style = LS('#336699', base_style=LCS)  # 定义样式

my_config = pygal.Config()
my_config.x_label_rotation = 45  # 让标签绕x轴旋转45度（x_label_rotation=45）
my_config.show_legend = False    # 隐藏了图例（show_legend=False）
my_config.title_font_size = 24   # 设置图表标题的大小
my_config.label_font_size = 14   # 设置标签的大小
# 主标签是y轴上为5000整数倍的刻度；这些标签应更大，以与副标签区分开来
my_config.major_label_font_size = 22
my_config.truncate_label = 15  # truncate_label将较长的项目名缩短为15个字符
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starrde Python Projects on GitHub"
chart.x_labels = names  # 设定x轴为names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')




