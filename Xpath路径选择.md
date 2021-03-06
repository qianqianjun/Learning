[toc]
# 什么是xpath
1. XML路径语言,拥有在数据结构树中查找节点的能力
1. 被开发者当作小型查询语言来使用
1. XPath通过元素和属性进行导航
 
---   
# 为什么学习xpath
1. 支持html
1. 比正则表达式简单
1. 比正则表达式强大
1. scrapy
 
---   
# xpath的基本概念
#### 节点
    父（Parent）
    子（Children）
    同胞（Sibling）
    先辈（Ancestor）
    后代（Descendant）
 
 
#### 路径表达式
> XPath 使用路径表达式在 XML 文档中选取节点
 
    /
        从根节点选取。
    //
        从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
    @
        选取属性。
#### 谓语（Predicates）
> 备注/补充说明
 
    /bookstore/book[1]
        选取属于 bookstore 子元素的第一个 book 元素。
    /bookstore/book[last()]
        选取属于 bookstore 子元素的最后一个 book 元素。
    /bookstore/book[last()-1]
        选取属于 bookstore 子元素的倒数第二个 book 元素。
    /bookstore/book[position()<3]
        选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
    //title[@lang]
        选取所有拥有名为 lang 的属性的 title 元素。
    //title[@lang='eng']
        选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
#### 使用通配符
    *
        匹配任何元素节点。
    @*
        匹配任何属性节点。
#### 选取若干路径
    //book/title | //book/price
        选取 book 元素的所有 title 和 price 元素。
    //title | //price
        选取文档中的所有 title 和 price 元素。
    /bookstore/book/title | //price
        选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。
 
---           
# xpath的使用
#### 安装lxml
> `pip install lxml`
#### 实例
> 1. 获取所有的 `<li>` 标签
> 1. 获取 `<li>` 标签的所有 class
> 1. 获取 `<li>` 标签下 href 为 link1.html 的 `<a>` 标签
> 1. 获取 `<li>` 标签下的所有 `<span>` 标签
> 1. 获取 `<li>` 标签下的所有 class，不包括 `<li>`
> 1. 获取最后一个 `<li>` 的 `<a>` 的 href
> 1. 获取`倒数第二个元素`的内容
> 1. 获取 `class` 为 `bold` 的标签名


#### 代码演示：

```python
from lxml import etree
#创建一个etree对象
html=etree.parse('hello.html')
#查找文档li标签下所有的a标签或者div标签：
result=html.xpath('//li//a|//li//div')
#print(len(result))
#查找所有的li标签：
result=html.xpath('//li')
#print(len(result))
#print(type(result))
#print(result[0])
#查找所有li的属性：
result=html.xpath('//li/@class')
#print(result)
#获取li中所有href属性为"link1.html"的a标签
result=html.xpath('//li//a[@href="link1.html"]')
# print(result[0].text)
#获取li标签下的所有span标签
result=html.xpath("//li//span")
'''for i in result:
    print(i.text)'''
# 获取所有li标签下的class属性，不包括li的class属性
result=html.xpath('//li//*/@class')
# print(result)
# 获取最后一个li标签下的a标签的href
result=html.xpath('//li[last()]/a/@href')
# print(result)
# 获取倒数第二个li标签中a标签的内容
result=html.xpath("//li[last()-1]/a")
# print(result[0].text)
# 获取class为bold的所有标签名,循环输出所有标签名
result=html.xpath('//*[@class="bold"]')
for i in result:
    print(i.tag)
```
