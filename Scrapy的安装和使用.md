[toc]
# Scrapy的安装
1. lxml
 
        pip install lxml
 
1. zope.interface
 
        pip install zope.interface
 
1. twisted
    > [https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)
 
        pip install wheel
        pip install ad3-2.1-cp36-cp36m-win_amd64.whl
1. pyOpenSSL
 
        pip install pyOpenSSL
1. pywin32
    > [https://pypi.python.org/pypi/pypiwin32](https://pypi.python.org/pypi/pypiwin32)
 
        pip install ad3-2.1-cp36-cp36m-win_amd64.whl
    注意: 需要把`pythoncom36.dll`和`pywintypes36.dll`拷贝到***C://windows/system32***
    路径:`C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Lib\site-packages\pywin32_system32`
1. scrapy
 
        pip install scrapy
# 创建Scrapy项目
 
    scrapy startproject xiaozhu
 
# Scrapy文件介绍
1. items.py
    > 定义爬取字段
1. piplines.py
    > 爬虫数据处理, 入库
1. settings.py
    > 项目设置
1. xiaozhuspider.py
    > 用户自建文件, 编写爬虫逻辑
 
# Scrapy爬虫编写
> 小猪短租网: [http://www.xiaozhu.com/](http://www.xiaozhu.com/)
 
1. items.py
 
        from scrapy.item import Item,Field
 
 
        class XiaozhuItem(Item):
            title = Field()
            address = Field()
            price = Field()
            lease_type = Field()
            suggestion = Field()
            bed = Field()
1. xiaozhuspider.py
 
        from scrapy.spiders import CrawlSpider
        from scrapy.selector import Selector
        from xiaozhu.items import XiaozhuItem
 
 
        class xiaozhu(CrawlSpider):
            name = 'xiaozhu'
            start_urls = ['http://hz.xiaozhu.com/fangzi/24369296403.html']
 
            def parse(self,response):
                item = XiaozhuItem()
                selector = Selector(response)
                title = selector.xpath('//h4/em/text()').extract()[0]
                address = selector.xpath('//p/span[@class="pr5"]/text()').extract()[0].strip()
                price = selector.xpath('//*[@id="pricePart"]/div[1]/span/text()').extract()[0]
                lease_type = selector.xpath('//*[@id="introduce"]/li[1]/h6/text()').extract()[0]
                suggestion = selector.xpath('//*[@id="introduce"]/li[2]/h6/text()').extract()[0]
                bed = selector.xpath('//*[@id="introduce"]/li[3]/h6/text()').extract()[0]
 
                item['title'] = title
                item['address'] = address
                item['price'] = price
                item['lease_type'] = lease_type
                item['suggestion'] = suggestion
                item['bed'] = bed
 
                yield item
 
1. piplines.py
 
        class XiaozhuPipeline(object):
            def process_item(self, item, spider):
                fp = open('G:/phpStudy/WWW/xiaozhu.txt', 'a+')
                fp.write(item['title']+'\n')
                fp.write(item['address']+'\n')
                fp.write(item['price']+'\n')
                fp.write(item['lease_type']+'\n')
                fp.write(item['suggestion']+'\n')
                fp.write(item['bed']+'\n')
                return item
 
1. settings.py
 
        ITEM_PIPELINES = {
            'xiaozhu.pipelines.XiaozhuPipeline': 300
        }
 
# Scrapy爬虫运行
#### 第一种方式
> `scrapy crawl xiaozhu`
#### 第二种方式
> 路径: `G:\phpStudy\WWW\test_scrapy\xiaozhu\xiaozhu\main.py`
 
    from scrapy import cmdline
 
    cmdline.execute('scrapy crawl xiaozhu'.split())
