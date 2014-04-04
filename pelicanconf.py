#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sanwen'
SITENAME = u'sanwen\'s blog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#theme
THEME = "/home/sanwen/virtualenvs/pelican/blog/pelican-themes/pelican-elegant-1.3"

#DISQUS评论支持
#DISQUS_SITENAME = u"sanween"

#多说评论支持
DUOSHUO_SITENAME = u"sanween"

# 侧边栏设置
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
#RECENT_POST_COUNT = 10
#DISPLAY_CATEGORIES_ON_SIDEBAR = True
#tag_cloud = True
#TAG_CLOUD_MAX_ITEMS = 20

# 设置pygments的样式
PYGMENTS_STYLE = u'emacs'

# 添加百度统计
BAIDU_ANALYTICS = True
