

# Beautiful Soup的简介
1. Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。
1. Beautiful Soup是一个工具箱，通过解析文档为用户提供需要抓取的数据，
1. Beautiful Soup简单，不需要多少代码就可以写出一个完整的应用程序。
1. Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。不需要考虑编码方式
1. Beautiful Soup灵活地提供不同的解析策略或强劲的速度
 
---
# Beautiful Soup 安装
 
> *`cmd.exe`*
```
pip install beautifulsoup4
pip install lxml
```
 
---
# 创建 Beautiful Soup 对象
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
#### 导入 bs4 库
```python
from bs4 import BeautifulSoup
```
#### 创建一个字符串，用来演示时使用
```python
html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p>
'''
```
 
#### 创建 beautifulsoup 对象
```python
soup = BeautifulSoup(html, 'lxml')
```
#### 打印 soup 对象的内容，格式化输出
```python
print(soup.prettify())
```
> 运行结果: *`cmd.exe`*
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
<html>
<head>
  <title id='id_title' class='class_title1 class_title2'>
   The Dormouse's story
  </title>
</head>
<body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <div>
   <!-- comment test -->
  </div>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
</body>
</html>
 
[Done] exited with code=0 in 0.845 seconds
```
---
# 四大对象种类
#### Tag
> 通俗点讲就是 HTML 中的一个个标签，像上面的 div，p。每个 Tag 有两个重要的属性 name 和 attrs，
> name 指标签的名字或者 tag 本身的 name，attrs 通常指一个标签的 class。
 
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')
print('title type:',type(soup.title))
print('title name:',soup.title.name)
print('title attrs:',soup.title.attrs)
```
> 运行结果: *`cmd.exe`*
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
title type: <class 'bs4.element.Tag'>
title name: title
title attrs: {'id': 'id_title', 'class': ['class_title1', 'class_title2']}
 
[Done] exited with code=0 in 0.635 seconds
```
#### NavigableString
> 获取标签内部的文字，如，soup.p.string。
 
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')
print('soup.p.string type:',type(soup.p.string))
print('soup.p.string contents:',soup.p.string)
```
> 运行结果: *`cmd.exe`*
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.string type: <class 'bs4.element.NavigableString'>
soup.p.string contents: The Dormouse's story
 
[Done] exited with code=0 in 0.807 seconds
```
#### BeautifulSoup
> 表示一个文档的全部内容。
 
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
 
 
```python
from bs4 import BeautifulSoup
 
html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')
print('soup type:', type(soup))
print('soup.name:', soup.name)
print('soup.attrs:', soup.attrs)
```
> 运行结果: *`cmd.exe`*
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup type: <class 'bs4.BeautifulSoup'>
soup.name: [document]
soup.attrs: {}
 
[Done] exited with code=0 in 0.628 seconds
```
#### Comment
> Comment对象是一个特殊类型的 NavigableString对象，其输出的内容不包括注释符号
 
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')
print('soup.div.string:', soup.div.string)
print('soup.div.string type:', type(soup.div.string))
print('soup.p.string type:', type(soup.p.string))
```
> 运行结果: *`cmd.exe`*
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.div.string:  comment test
soup.div.string type: <class 'bs4.element.Comment'>
soup.p.string type: <class 'bs4.element.NavigableString'>
 
[Done] exited with code=0 in 0.693 seconds
```
---
# 遍历文档树
#### 节点内容
.string 属性
> 获取tag的文本内容
> 如果tag只有一个 NavigableString类型子节点,那么这个tag可以使用 .string 得到子节点内容
> 如果超过一个, 返回None
 
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.p.string:',soup.p.string)
print('soup.div.string:',soup.div.string)
```
> 运行结果: *`cmd.exe`*
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.string: p-content
soup.div.string: None
 
[Done] exited with code=0 in 0.623 seconds
```
 
#### 多个内容
.strings 属性 `获取所有内容, 返回一个generator`(包括空白字符)
.stripped_strings 属性 `获取所有内容, 返回一个generator`(去除空白字符)
 
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.p.strings:',soup.p.strings)
print('soup.p.strings list:',list(soup.p.strings))
print('----------------------------------------')
print('soup.div.strings:', soup.div.strings)
print('soup.div.strings list:', list(soup.div.strings))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.strings: <generator object _all_strings at 0x000001E70CFE8308>
soup.p.strings list: ['p-content']
----------------------------------------
soup.div.strings: <generator object _all_strings at 0x000001E70CFE8308>
soup.div.strings list: ['div-content', 'span-content']
 
[Done] exited with code=0 in 0.774 seconds
```
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>
p-content
</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.p.strings:',soup.p.strings)
print('soup.p.strings list:', list(soup.p.strings))
print('----------------------------------------')
print('soup.p.stripped_strings:', soup.p.stripped_strings)
print('soup.p.stripped_strings list:', list(soup.p.stripped_strings))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.strings: <generator object _all_strings at 0x0000017F1E7D8308>
soup.p.strings list: ['\np-content\n']
----------------------------------------
soup.p.stripped_strings: <generator object stripped_strings at 0x0000017F1E7D8308>
soup.p.stripped_strings list: ['p-content']
 
[Done] exited with code=0 in 0.632 seconds
```
 
 
#### 直接子节点
.contents 属性 `将tag的子节点以列表的方式输出`
.children 属性 `将tag的子节点以list_iterator的方式输出`
 
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.div.contents:',soup.div.contents)
print('soup.div.contents list:', list(soup.div.contents))
print('----------------------------------------')
print('soup.div.children:', soup.div.children)
print('soup.div.children list:', list(soup.div.children))
```
 
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.div.contents: ['div-content', <span>span-content</span>]
soup.div.contents list: ['div-content', <span>span-content</span>]
----------------------------------------
soup.div.children: <list_iterator object at 0x000002D89126DC50>
soup.div.children list: ['div-content', <span>span-content</span>]
 
[Done] exited with code=0 in 0.647 seconds
```
 
 
#### 所有子孙节点
.descendants 属性 `对所有子节点递归`
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.div.contents:',soup.div.contents)
print('soup.div.contents list:', list(soup.div.contents))
print('----------------------------------------')
print('soup.div.descendants:', soup.div.descendants)
print('soup.div.descendants list:', list(soup.div.descendants))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.div.contents: ['div-content', <span>span-content</span>]
soup.div.contents list: ['div-content', <span>span-content</span>]
----------------------------------------
soup.div.descendants: <generator object descendants at 0x000001ECDAAF8308>
soup.div.descendants list: ['div-content', <span>span-content</span>, 'span-content']
 
[Done] exited with code=0 in 0.63 seconds
```
 
#### 父节点
.parent 属性 `获取父节点`
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.b.parent:',soup.b.parent)
print('soup.b.parent type:',type(soup.b.parent))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.b.parent: <p><b>p-content</b></p>
soup.b.parent type: <class 'bs4.element.Tag'>
 
[Done] exited with code=0 in 0.825 seconds
```
 
#### 全部父节点
.parents 属性 `获取全部父节点`
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.b.parents:',soup.b.parents)
print('soup.b.parents type:',type(soup.b.parents))
print('-------------------------------------------')
for i in soup.b.parents:
    print('parent name:',i.name)
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.b.parents: <generator object parents at 0x0000021E1B278308>
soup.b.parents type: <class 'generator'>
-------------------------------------------
parent name: p
parent name: body
parent name: html
parent name: [document]
 
[Done] exited with code=0 in 0.651 seconds
```
 
#### 兄弟节点
.next_sibling 属性 `下一个兄弟节点`
.previous_sibling 属性 `上一个兄弟节点`
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.p.next_sibling:',repr(soup.p.next_sibling))
print('soup.p.next_sibling type:', type(soup.p.next_sibling))
print('------------------------------------------------------------------------')
print('soup.p.next_sibling.next_sibling:', soup.p.next_sibling.next_sibling)
print('soup.p.next_sibling.next_sibling type:', type(soup.p.next_sibling.next_sibling))
print('------------------------------------------------------------------------')
print('soup.p.previous_sibling:',repr(soup.p.previous_sibling))
print('soup.p.previous_sibling type:', type(soup.p.previous_sibling))
print('------------------------------------------------------------------------')
print('soup.p.previous_sibling.previous_sibling:', soup.p.previous_sibling.previous_sibling)
print('soup.p.previous_sibling.previous_sibling type:', type(soup.p.previous_sibling.previous_sibling))
```
> 运行结果
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.next_sibling: '\n'
soup.p.next_sibling type: <class 'bs4.element.NavigableString'>
------------------------------------------------------------------------
soup.p.next_sibling.next_sibling: <div>div-content<span>span-content</span></div>
soup.p.next_sibling.next_sibling type: <class 'bs4.element.Tag'>
------------------------------------------------------------------------
soup.p.previous_sibling: '\n'
soup.p.previous_sibling type: <class 'bs4.element.NavigableString'>
------------------------------------------------------------------------
soup.p.previous_sibling.previous_sibling: None
soup.p.previous_sibling.previous_sibling type: <class 'NoneType'>
 
[Done] exited with code=0 in 0.639 seconds
```
 
 
#### 全部兄弟节点
.next_siblings 属性 `全部的弟弟`
.previous_siblings 属性 `全部的哥哥`
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.p.next_siblings type:', type(soup.p.next_siblings))
print('soup.p.next_siblings list:', list(soup.p.next_siblings))
print('------------------------------------------------------------------------')
print('soup.p.previous_siblings type:', type(soup.p.previous_siblings))
print('soup.p.previous_siblings list:', list(soup.p.previous_siblings))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.next_siblings type: <class 'generator'>
soup.p.next_siblings list: ['\n', <div>div-content<span>span-content</span></div>, '\n']
------------------------------------------------------------------------
soup.p.previous_siblings type: <class 'generator'>
soup.p.previous_siblings list: ['\n']
 
[Done] exited with code=0 in 0.515 seconds
```
 
#### 前后节点
.next_element 属性 `后节点`
.previous_element 属性 `前节点`
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.p.next_element :', repr(soup.p.next_element))
print('soup.p.next_element.next_element :', repr(soup.p.next_element.next_element))
print('soup.p.next_element.next_element.next_element :', repr(soup.p.next_element.next_element.next_element))
print('soup.p.next_element.next_element.next_element.next_element :', repr(soup.p.next_element.next_element.next_element.next_element))
print('------------------------------------------------------------------------')
print('soup.p.previous_element :', repr(soup.p.previous_element))
print('soup.p.previous_element.previous_element :', repr(soup.p.previous_element.previous_element))
print('soup.p.previous_element.previous_element.previous_element :', repr(soup.p.previous_element.previous_element.previous_element))
print('soup.p.previous_element.previous_element.previous_element.previous_element :', repr(soup.p.previous_element.previous_element.previous_element.previous_element))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.next_element : <b>p-content</b>
soup.p.next_element.next_element : 'p-content'
soup.p.next_element.next_element.next_element : '\n'
soup.p.next_element.next_element.next_element.next_element : <div>div-content<span>span-content</span></div>
------------------------------------------------------------------------
soup.p.previous_element : '\n'
soup.p.previous_element.previous_element : <body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
</body>
soup.p.previous_element.previous_element.previous_element : '\n'
soup.p.previous_element.previous_element.previous_element.previous_element : <head></head>
 
[Done] exited with code=0 in 0.85 seconds
```
 
#### 所有前后节点
.next_elements 属性
.previous_elements 属性
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print('soup.p.next_elements :', type(soup.p.next_elements))
for i in  soup.p.next_elements:
    print('soup.p.next_element:',repr(i))
print('---------------------------------------------------------')
print('soup.p.previous_elements :', type(soup.p.previous_elements))
for i in  soup.p.previous_elements:
    print('soup.p.previous_element:',repr(i))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
soup.p.next_elements : <class 'generator'>
soup.p.next_element: <b>p-content</b>
soup.p.next_element: 'p-content'
soup.p.next_element: '\n'
soup.p.next_element: <div>div-content<span>span-content</span></div>
soup.p.next_element: 'div-content'
soup.p.next_element: <span>span-content</span>
soup.p.next_element: 'span-content'
soup.p.next_element: '\n'
---------------------------------------------------------
soup.p.previous_elements : <class 'generator'>
soup.p.previous_element: '\n'
soup.p.previous_element: <body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
</body>
soup.p.previous_element: '\n'
soup.p.previous_element: <head></head>
soup.p.previous_element: <html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
</body></html>
 
[Done] exited with code=0 in 0.775 seconds
```
 
---
# 搜索文档树
#### find_all() `当前标签的所有子节点`
通过标签名查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('p'))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<p><b>p-content1</b></p>, <p>p-content2</p>]
 
[Done] exited with code=0 in 0.786 seconds
```
 
通过正则查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(re.compile('^p')))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<p><b>p-content1</b></p>, <p>p-content2</p>, <panda>panda-content</panda>]
 
[Done] exited with code=0 in 0.721 seconds
```
通过列表查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(['p', 'div']))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<p><b>p-content1</b></p>, <p>p-content2</p>, <div>div-content<span>span-content</span></div>]
 
[Done] exited with code=0 in 0.862 seconds
```
 
通过正则配合内容查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('content$')))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
['panda-content', 'div-content', 'span-content']
 
[Done] exited with code=0 in 0.994 seconds
```
 
通过属性查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(id='panda'))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<panda id="panda">panda-content</panda>]
 
[Done] exited with code=0 in 0.692 seconds
```
 
限制个数
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<p>p-content3</p>
<p>p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('p'))
print('-----------------------------------')
print(soup.find_all('p',limit=3))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py\test_bs.py"
[<p><b>p-content1</b></p>, <p>p-content2</p>, <p>p-content3</p>, <p>p-content4</p>, <p>p-content5</p>, <p>p-content6</p>, <p>p-content7</p>]
-----------------------------------
[<p><b>p-content1</b></p>, <p>p-content2</p>, <p>p-content3</p>]
 
[Done] exited with code=0 in 0.547 seconds
```
 
#### find()
> find_all()返回一个列表
> find()返回第一个结果
#### find_parent()
> 在当前元素的父节点中查找,返回第一个
#### find_parents()
> 在当前元素的父节点中查找,返回list
#### find_next_sibling()
> 在当前元素的兄弟节点中查找(弟弟),返回第一个
#### find_next_siblings()
> 在当前元素的兄弟节点中查找(弟弟),返回list
#### find_previous_sibling()
> 在当前元素的兄弟节点中查找(哥哥),返回第一个
#### find_previous_siblings()
> 在当前元素的兄弟节点中查找(哥哥),返回list
#### find_next()
> 在当前元素的相邻节点中查找(向下),返回第一个
#### find_all_next()
> 在当前元素的相邻节点中查找(向下),返回list
#### find_previous()
> 在当前元素的相邻节点中查找(向上),返回第一个
#### find_all_previous()
> 在当前元素的相邻节点中查找(向上),返回list
 
 
---
# CSS选择器
#### 通过标签名查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<p>p-content3</p>
<p>p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('p'))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<p><b>p-content1</b></p>, <p>p-content2</p>, <p>p-content3</p>, <p>p-content4</p>, <p>p-content5</p>, <p>p-content6</p>, <p>p-content7</p>]
 
[Done] exited with code=0 in 0.789 seconds
```
 
 
#### 通过类名查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p class="p-class">p-content2</p>
<p class="p-class">p-content3</p>
<p class="p-class">p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.p-class'))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<p class="p-class">p-content2</p>, <p class="p-class">p-content3</p>, <p class="p-class">p-content4</p>]
 
[Done] exited with code=0 in 0.821 seconds
```
 
 
#### 通过 id 名查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p class="p-class">p-content2</p>
<p class="p-class">p-content3</p>
<p class="p-class">p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('#panda'))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<panda id="panda">panda-content</panda>]
 
[Done] exited with code=0 in 0.718 seconds
```
 
 
#### 组合查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<div>
<p><b>p-content1</b></p>
<p class="p-class">p-content2</p>
<p class="p-class">p-content3</p>
<p class="p-class">p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('p #panda'))
print(soup.select('div #panda'))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[]
[<panda id="panda">panda-content</panda>]
 
[Done] exited with code=0 in 0.689 seconds
```
 
 
#### 属性查找
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
from bs4 import BeautifulSoup
import re
 
html='''
<html><head></head>
<body>
<div>
<p><b>p-content1</b></p>
<p class="p-class">p-content2</p>
<p class="p-class">p-content3</p>
<p class="p-class">p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('p[class="p-class"]'))
```
> 运行结果:
```
[Running] python "f:\WWW\test_py2\test_bs4.py"
[<p class="p-class">p-content2</p>, <p class="p-class">p-content3</p>, <p class="p-class">p-content4</p>]
 
[Done] exited with code=0 in 0.683 seconds
```
