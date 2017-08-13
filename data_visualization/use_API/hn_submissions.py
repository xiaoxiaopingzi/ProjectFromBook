# -*- coding: UTF-8 -*-
"""执行一个API调用，返回Hacker News上当前热门文章的ID，再查看每篇排名靠前的文章"""
import requests

from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# 这个API调用返回一个List列表，这个列表包含Hacker News上当前最热门的500篇文章的ID。
r = requests.get(url)
print("Status code:", r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # 这个字典存储文章的标题、文章的链接以及文章的评论数
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        # descendants表示文章被评论的次数,如果文章还没有评论，响应字典中将没有键'descendants',
        # 这时可以通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
        'comments': response_dict.get('descendants', 0)
    }

    submission_dicts.append(submission_dict)

# 根据评论数对字典进行排序,reverse=True表示降序排序,
# key=itemgetter('comments')表示以字典中与'comments'相关联的值作为关键字进行排序
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])