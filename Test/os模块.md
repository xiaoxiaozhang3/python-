---
title: os模块
date: 2019-07-21 10:38:30
tags: python基础
---

# os模块
os模块是一个python内置的文件模块
## os模块的使用

`import os`

`os.getcwd()`
功能：获取当前目录的绝对路径

绝对路径：
window：以盘符开头，或者以\开头
linux：以/开头或者以~开头
相对路径：
window：以文件开头，以./开头 或者../开头
linux：与window相同

<!--more-->

`os.listdir(path)`
功能：显示指定路径下所有的文件名以及目录名，若path不指定，默认当前目录下。

`os.path.abspath(path)`
功能：将指定的路径拼接到当前所在所在的路径下

`os.path.split(path)`
功能：返回指定路径目录部分以及文件部分
本质：以最后一个/来进行切分，返回两个值，前面的就是目录部分，后面的就是文件部分
若是"."切分到文件部分去

`os.path.dirname(path)`
功能：返回指定路径的目录部分

`os.path.basename(path)`
功能：返回指定路径的文件部分

`os.path.join(path,paths)`
功能:对路径进行拼接处理
paths：可以接收多个路径
若paths存在绝对路径，前面路径则不保留。

`os.path.getsize(path)`
功能:获取指定路径文件的大小【目录的大小获取不到】

`os.path.exists(path)`
功能：判断指定的路径是否存在，若存在则返回True，否则返回False

`os.path.isdir(path)`
功能：判断该路径是否为目录，若是返回True，否则返回False

`os.path.isfile(path)`
功能：判断指定的路径是否为文件，若是则返回True，否则返回False

`os.remove(path)`
功能:删除指定的路径的文件

`os.mkdir(path)`
功能：创建指定的目录

`os.makedirs(path)`
功能：递归创建多个目录

`os.rmdir(path)`
功能：删除指定的空目录

`os.removedirs(path)`
功能：递归删除目录

`os.chdir(path)`
功能：切换目录
