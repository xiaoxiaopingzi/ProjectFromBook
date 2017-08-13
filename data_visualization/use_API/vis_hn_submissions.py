# -*- coding: UTF-8 -*-
"""执行一个API调用，返回Hacker News上当前热门文章的ID，再查看每篇排名靠前的文章"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# 这个API调用返回一个List列表，这个列表包含Hacker News上当前最热门的500篇文章的ID。
r = requests.get(url)
print("Status code:", r.status_code)

submission_ids = r.json()
submission_dicts, titles = [], []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # 用title作为图表的x轴
    titles.append(response_dict['title'])
    # 这个字典存储文章的标题、文章的链接以及文章的评论数
    submission_dict = {
        'label': response_dict['title'],   # 标题
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        # descendants表示文章被评论的次数,如果文章还没有评论，响应字典中将没有键'descendants',
        # 这时可以通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
        'value': response_dict.get('descendants', 0)  # 评论数
    }

    submission_dicts.append(submission_dict)

# 根据评论数对字典进行排序,reverse=True表示降序排序,
# key=itemgetter('comments')表示以字典中与'comments'相关联的值作为关键字进行排序
submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)

# 可视化
my_style = LS('#336699', base_style=LCS)  # 定义样式
my_config = pygal.Config()
my_config.x_label_rotation = 45  # 让标签绕x轴旋转45度（x_label_rotation=45）
my_config.show_legend = False    # 隐藏了图例（show_legend=False）
my_config.title_font_size = 24   # 设置图表标题的大小
my_config.label_font_size = 14   # 设置标签的大小
my_config.truncate_label = 15  # truncate_label将较长的项目名缩短为15个字符
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Hacker News popular articles"
chart.x_labels = titles  # 设定x轴为names

chart.add('', submission_dicts)
chart.render_to_file('hn_popular_articles.svg')
