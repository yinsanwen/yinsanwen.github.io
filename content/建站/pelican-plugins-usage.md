Title: Pelican插件用法
Slug: pelican-plugins-usage

[TOC]

##安装Pelican插件
下载Pelican插件，放在pelican-plugins目录中。

    :::bash
    git clone https://github.com/getpelican/pelican-plugins

配置pelicanconf.py文件

    :::bash
    PLUGIN_PATHS = ['path/to/pelican-plugins']  # 插件的目录  
    PLUGINS = ['assets', 'sitemap', 'gravatar'] # 启用的插件列表

---
## 使用Pelican插件

### extract_toc
extract_toc插件需要BeautifulSoup的支持

    :::bash
    pip install beautifulsoup4

一、针对markdown编写的博客

首先需要在配置文件里面设置
    
    :::python
    MD_EXTENSIONS = (['toc'])

然后在markdown文件(.md)的开头处添加[TOC]标记。如下所示

    :::bash
    title: My super title
    date: 4-4-2013
    tags: thats, awesome
    
    [TOC]
    
    # Heading 1 #

    Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.

