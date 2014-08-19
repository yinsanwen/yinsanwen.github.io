#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'sanwen'
SITENAME = u'sanwen的博客'
SITEURL = u'http://yinsanwen.github.io'

PATH = 'content'
#STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

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
# metadata
DEFAULT_DATE = 'fs'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#theme
THEME = "pelican-themes/pelican-elegant-1.3" 

#plugins
PLUGIN_PATHS = ['pelican-plugins']

#set for elegant
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

SITEMAP = {
        'format': 'xml',
        'priorities': {
             'articles': 0.5,
             'indexes': 0.5,
             'pages': 0.5
         },
         'changefreqs': {
             'articles': 'monthly',
             'indexes': 'daily',
             'pages': 'monthly'
         }
}

#DISQUS评论支持
#DISQUS_SITENAME = u"sanween"

#多说评论支持
DUOSHUO_SITENAME = u"sanween"

# 设置pygments的样式
#PYGMENTS_STYLE = u'emacs'
#PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
# 添加百度统计
