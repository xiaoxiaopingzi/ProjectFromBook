# -*- coding: UTF-8 -*-
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']
plot_dicts = [
    {'value': 37351, 'label': 'A curated list of awesome Python frameworks, libraries, software and resources',
     'xlink': 'https://github.com/vinta/awesome-python'},
    {'value': 30951, 'label': 'Modern command line HTTP client – user-friendly curl alternative with intuitive UI, JSON support, syntax highlighting, wget-like downloads, extensions, etc.  https://httpie.org',
     'xlink': 'https://github.com/jakubroztocil/httpie'},
    {'value': 29518, 'label': 'Magnificent app which corrects your previous console command.',
     'xlink': 'https://github.com/nvbn/thefuck'},
    {'value': 28953, 'label': 'A microframework based on Werkzeug, Jinja2 and good intentions',
     'xlink': 'https://github.com/pallets/flask'},
    {'value': 28175, 'label': 'Command-line program to download videos from YouTube.com and other video sites',
     'xlink': 'https://github.com/rg3/youtube-dl'},
    {'value': 27455, 'label': 'The Web framework for perfectionists with deadlines.',
     'xlink': 'https://github.com/django/django'},
    {'value': 26809, 'label': 'Python HTTP Requests for Humans™ ✨🍰✨', 'xlink': 'https://github.com/requests/requests'},
    {'value': 24948, 'label': 'A curated list of awesome Machine Learning frameworks, libraries and software.',
     'xlink': 'https://github.com/josephmisiti/awesome-machine-learning'},
    {'value': 24751, 'label': 'Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy. Avoid writing scripts or custom code to deploy and update your applications— automate in a language that approaches plain English, using SSH, with no agents to install on remote systems.',
     'xlink': 'https://github.com/ansible/ansible'},
    {'value': 22078, 'label': 'Scrapy, a fast high-level web crawling & scraping framework for Python.',
     'xlink': 'https://github.com/scrapy/scrapy'},
    {'value': 21384, 'label': 'The Big List of Naughty Strings is a list of strings which have a high probability of causing issues when used as user-input data.',
     'xlink': 'https://github.com/minimaxir/big-list-of-naughty-strings'},
    {'value': 20524, 'label': 'scikit-learn: machine learning in Python',
     'xlink': 'https://github.com/scikit-learn/scikit-learn'},
    {'value': 19802, 'label': 'Models built with TensorFlow', 'xlink': 'https://github.com/tensorflow/models'},
    {'value': 19371, 'label': None, 'xlink': 'https://github.com/shadowsocks/shadowsocks'},
    {'value': 19256, 'label': "Certbot, previously the Let's Encrypt Client, is EFF's tool to obtain certs from Let's Encrypt, and (optionally) auto-enable HTTPS on your server.  It can also act as a client for any other CA that uses the ACME protocol.",
     'xlink': 'https://github.com/certbot/certbot'},
    {'value': 18705,
     'label': 'Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.',
     'xlink': 'https://github.com/donnemartin/system-design-primer'},
    {'value': 18553, 'label': 'Deep Learning library for Python. Runs on TensorFlow, Theano, or CNTK.',
     'xlink': 'https://github.com/fchollet/keras'},
    {'value': 15979, 'label': 'a web proxy tool', 'xlink': 'https://github.com/XX-net/XX-Net'},
    {'value': 15301, 'label': 'Apache Superset (incubating) is a modern, enterprise-ready business intelligence web application',
     'xlink': 'https://github.com/apache/incubator-superset'},
    {'value': 14553,
     'label': 'The C++ Core Guidelines are a set of tried-and-true guidelines, rules, and best practices about coding in C++',
     'xlink': 'https://github.com/isocpp/CppCoreGuidelines'},
    {'value': 14405, 'label': 'A code-completion engine for Vim', 'xlink': 'https://github.com/Valloric/YouCompleteMe'},
    {'value': 14140, 'label': ':arrow_double_down: Dumb downloader that scrapes the web',
     'xlink': 'https://github.com/soimort/you-get'},
    {'value': 14065, 'label': 'Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.',
     'xlink': 'https://github.com/tornadoweb/tornado'},
    {'value': 13656, 'label': 'the code that powers reddit.com', 'xlink': 'https://github.com/reddit/reddit'},
    {'value': 13488, 'label': 'Sentry is a cross-platform crash reporting and aggregation platform.',
     'xlink': 'https://github.com/getsentry/sentry'},
    {'value': 13008, 'label': 'Deep Learning papers reading roadmap for anyone who are eager to learn this amazing tech!',
     'xlink': 'https://github.com/songrotek/Deep-Learning-Papers-Reading-Roadmap'},
    {'value': 12270, 'label': 'The Python programming language', 'xlink': 'https://github.com/python/cpython'},
    {'value': 12196, 'label': 'A collection of design patterns/idioms in Python',
     'xlink': 'https://github.com/faif/python-patterns'},
    {'value': 11789, 'label': 'Official repository for IPython itself. Other repos in the IPython organization contain things like the website, documentation builds, etc.',
     'xlink': 'https://github.com/ipython/ipython'},
    {'value': 11695, 'label': 'A practical guide to securing macOS.',
     'xlink': 'https://github.com/drduh/macOS-Security-and-Privacy-Guide'}]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
