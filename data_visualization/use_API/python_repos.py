# -*- coding: UTF-8 -*-
"""执行API调用并存储响应"""
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

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print("\nName:", repo_dict["name"])
#     print("Owner", repo_dict["owner"]["login"])
#     print("Stars:", repo_dict["stargazers_count"])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

# 可视化
# 使用LightenStyle类（别名LS）定义了一种样式，并将其基色设置为深蓝色
my_style = LS('#336699', base_style=LCS)  # 定义样式
# 让标签绕x轴旋转45度（x_label_rotation=45），并隐藏了图例（show_legend=False）
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starrde Python Projects on GitHub"
chart.x_labels = names  # 设定x轴为names

chart.add("", stars)
chart.render_to_file("python_repos.svg")




