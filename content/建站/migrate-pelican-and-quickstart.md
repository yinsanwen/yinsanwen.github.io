Title: Pelican的迁移和快速开始
Slug: migrate-pelican-and-quickstart

[TOC]

### 1、安装pelican
使用`pip`命令快速安装
```
sudo pip install pelican
```
如果你计划使用Markdown语法格式，需要安装Markdown库
```bash
pip install Markdown
```
---
(可选) 如果你没有安装pip，请先安装pip(推荐)。否则直接到步骤2。
####安装pip
pip是一个python软件包管理工具。 

1、下载get-pip.py
```bash
sudo curl -O https://bootstrap.pypa.io/get-pip.py
```
2、安装pip
```bash
sudo python get-pip.py
```
---
###2、迁移之前的Pelican博客
我之前使用过pelican写过博客，将output目录里面的内容作为github的master分支。其他目录(pelican配置等)作为source分支。托管在github上面。

我们首先取回source分支 (参考[如何克隆一个单独分支][1])
```bash 
git clone -b source --single-branch  git@github.com:yinsanwen/yinsanwen.github.io.git blog
```
这样，我们就恢复了我们之前的pelican。并继续用此更新我们的博客。

我使用`Fabric`自动构建工具来使用我的pelican。见[Fabric用法][2]。

---
### 3、发布博客

我的博客是托管在github的User Pages之上的。将pelican生成的output目录里面的静态网页放到其`master`分支上面即可。
前面说过，pelican的其他目录也是有必要备份的。我将它们放在了source分支上面。

可以使用`ghp-import`工具方便的将output目录里面的内容推送到github上面。这样我们在本地写博客的时候只需呆在source分支上面即可。而透过ghp-import来进行部署。具体步骤如下：
``` bash
$ fab build
$ ghp-import output
$ git push origin gh-pages:master
```
`ghp-import output`命令会在工作空间创建一个`gh-pages`的分支，并将outout目录里面的内容更新到该分支。  
`git push`命令则将本地gh-pages分支推送到远程master分支。这样就完成了更新。
(我们无需在远程仓库中备份gh-pages分支)。

我们可以新建一个fab命令来一次完成后两个操作。在fabfile.py里面添加:
``` python
def deploy():
    local('ghp-import output && git push origin gh-pages:master')
```

这样，通过步骤
``` bash
fab build
fab deploy
```
就可以快速的更新和发布文章。




  [1]: http://stackoverflow.com/questions/1911109/clone-a-specific-git-branch
  [2]: http://docs.getpelican.com/en/3.4.0/publish.html#fabric
