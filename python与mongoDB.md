[toc]
# NoSQL简介
1. not only sql
1. 非关系型数据库产品是传统关系型数据库的功能阉割版本, 通过减少用不到或很少用的功能, 来大幅度提高产品性能
1. NOSQL是基于键值对的, 而且不需要经过SQL层的解析, 所以性能非常高。
1. 同样也是因为基于键值对, 数据之间没有耦合性, 所以非常容易水平扩展。
1. 目前基本上大部分主流的非关系型数据库都是免费的。而比较有名气的关系型数据库, 比如Oracle、DB2、MSSQL是收费的
1. 实际开发中, 有很多业务需求, 其实并不需要完整的关系型数据库功能, 非关系型数据库的功能就足够使用了。这种情况下, 使用性能更高、成本更低的非关系型数据库当然是更明智的选择
 
---
# 安装
 
#### MongoDB的安装
> 官网: https://www.mongodb.com/download-center#community
> 把mongodb加入系统路径: `E:\MongoDB\Server\3.6\bin`
> 配置数据库路径: `mongod -dbpath E:\mongodb\data\db`
 
|参数|含义|
|--|:--:|
|`--bind_ip`|绑定ip|
|`--logpath`|指定存放log的路径|
|`--logappend`|使用追加方式写日志|
|`--dbpath`|指定mongodb的存储路径|
|`--port`|指定端口号,默认`27017`|
|`--serviceName`|指定服务名称|
|`--install`|作为一个windows服务安装|
 
> 启动数据库: `mongo`
#### Pymongo第三方库的安装
> `pip install pymongo`
#### 可视化管理工具Robomongo的安装
> 官网: https://robomongo.org/download
 
---
# MongoDB的使用
##### MongoDB中文档、集合、数据库的概念
|SQL概念|MongoDB概念|说明|
|:-:|:-:|:-:|
|database|database|数据库|
|table|collection|数据库表/集合|
|row|document|数据行/文档|
|column|field|数据字段列/域|
|index|index|索引|
|primary_key|primary_key|主键/MongoDB自动将_id字段设置为主键|
 
文档1：
```json
{
    "name": "xujunhao",
    "age": 18,
    "email": ["qq_email", "163_email", "gmail"],
    "chat": {
        "qq": "11111",
        "weixin": "11111"
    }
}
```
文档2：
```json
{
    "Name": "xujunhao",
    "Age": 18,
    "email": ["qq_email", "163_email", "gmail"],
    "chat": {
        "qq": "11111",
        "weixin": "11111"
    }
}
```
文档3：
```json
{
    "name": "xujunhao",
    "email": ["qq_email", "163_email", "gmail"],
    "age": 18,
    "chat": {
        "qq": "11111",
        "weixin": "11111"
    }
}
```
文档的注意事项:
1. 文档的键值对是有序的, 顺序不同文档亦不同
1. 文档区分大小写以及值类型
    * `{"name":"xujunhao","age":24}`
    * `{"Name":"xujunhao","Age":24}`
    * `{"name":"xujunhao","age":"24"}`
1. 文档的键是用双引号标识的字符串
1. 除个别例外, 可用任意UTF-8字符
    * 键不能含有"\0"（空字符）, 这个字符用来标识键的结尾
    * "."和"$"被保留, 存在特别含义, 最好不要用来命名键名
    * 以"_"开头的键是保留的, 建议不要使用。
 
集合的注意事项:
1. 集合名不能是空字符串
1. 集合名不能含有"\0"（空字符）, 这个字符用来标识集合的结尾
1. 集合名不能以"system."开头, 这是为系统集合保留的前缀
1. "$"被保留, 存在特别含义, 最好不要用来命名集合
 
##### MongoDB常见数据类型
 
|数据类型|描述|
|:-|:-|
|String|字符串。存储数据常用的数据类型。在 MongoDB 中, UTF-8 编码的字符串才是合法的。|
|Integer|整型数值。用于存储数值。根据你所采用的服务器, 可分为 32 位或 64 位。|
|Boolean|布尔值。用于存储布尔值（真/假）。|
|Double|双精度浮点值。用于存储浮点值。|
|Array|用于将数组或列表或多个值存储为一个键。|
|Timestamp|时间戳。记录文档修改或添加的具体时间。|
|Object|用于内嵌文档。|
|Null|用于创建空值。|
|Date|日期时间。用 UNIX 时间格式来存储当前日期或时间。你可以指定自己的日期时间：创建 Date 对象, 传入年月日信息。|
|Binary Data|二进制数据。用于存储二进制数据。|
 
##### 创建/删除数据库
1. 创建数据库
    > `use database_name`  # 切换到指定数据库, 没有则创建
1. 查询数据库
    > `show dbs`  # 显示有数据的数据库
1. 删除数据库
    > `db.dropDatabase()`
##### 集合中文档的增删改查
插入文档
> db.collection_name.insert(document)
 
    > db.user.insert({
        name: "xujunhao",
        age: 18,
        sex: "male"
    })
 
查询文档
> db.collection_name.find().pretty()
 
    db.user.find()
    db.user.find().pretty()
 
条件查询
1. 等于`{<key>:<value>}`
 
        # 从user集合中找到age等于18的文档
        db.user.find({"age": 18}).pretty()
 
1. 不等于`{<key>:{$ne:<value>}}`
 
        # 从user集合中找到age不等于18的文档
        db.user.find({"age": {$ne:18}}).pretty()
 
1. 小于`{<key>:{$lt:<value>}}`
 
        # 从user集合中找到age小于18的文档
        db.user.find({"age": {$lt:18}).pretty()
 
1. 小于或等于`{<key>:{$lte:<value>}}`
 
        # 从user集合中找到age小于或等于18的文档
        db.user.find({"age": {$lte:18}).pretty()
 
1. 大于`{<key>:{$gt:<value>}}`
 
        # 从user集合中找到age大于18的文档
        db.user.find({"age": {$gt:18}).pretty()
 
1. 大于或等于`{<key>:{$gte:<value>}}`
 
        # 从user集合中找到age大于或等于18的文档
        db.user.find({"age": {$gte:18}).pretty()
 
and查询
> db.collection_name.find(`{key1:value1,key2:value2}`).pretty()
 
    # 查询name为xujunhao, 同时age大于18的文档
    db.user.find({"age":{$gt:18},"name":"xujunhao"}).pretty()
 
or查询
> db.collection_name.find({`$or:[{<key1>:<value1>},{<key2>:<value2>}]`}).pretty()
 
    db.user.find({
        $or:[
            {"age":{$gt:18}},
            {"name":"xujunhao"}
        ]
    }).pretty()
 
and和or联合使用
 
    db.user.find({
        "age":{$gt:50},
        $or:[
            {
                "sex":"female"
            },
            {
                "name":"xujunhao"
            }
        ]
    }).pretty()
 
更新文档
1. update()
 
        db.collection_name.update(
            query, # 查询条件
            update, # 更新数据
            {
                upsert: boolean, # 如果没有是否插入新行, 默认false
                multi: boolean, # 如果找到多条需要更新的数据, 是否全部更新, 默认false
                writeConcern: document # 设置抛出异常的级别
            }
        )
 
    > 把name为xujunhao的文档, 改成mike
 
        db.user.update(
            {
                "name":"xujunhao"
            },
            {
                $set:{
                    "name":"mike"
                }
            },
            {
                multi:true
            }
        )
1. save()
    > 通过传入的文档替换已有文档
 
        db.collection_name.save(
            document, # 准备写入数据库的数据
            {
                writeConcern: document # 报错级别
            }
        )
 
        # 根据主键找到数据并修改
        db.python.save({
            "_id":ObjectId(),
            "name":"lily",
            "description":"this is a pretty girl !!!",
            "age":18
        })
 
删除文档
 
    db.collection_name.remove(
        query, # 删除之前先查询, 如果没有查询条件, 则删除所有
        {
            justOne: boolean, # 只删除一个文档, 默认为false
            writeConcern: document # 异常抛出级别
        }
    )
 
> 删除name为xujunhao的文档
 
    db.user.remove({
        "name": "xujunhao"
    })
 
---
# 使用python操作MongoDB
##### 安装mongodb第三方库
> pip install pymongo
##### 导入pymongo
> from pymongo import MongoClient
##### 建立连接
1. `client = MongoClient()`
1. `client = MongoClient('localhost', 27017)`
1. `client = MongoClient('mongodb://localhost:27017/')`
##### 获取数据库
1. `db = client.xujunhao_db`
1. `db = client['xujunhao_db']`
##### 获取一个集合
1. `user_collection = db.user`
1. `user_collection = db['user']`
##### 插入文档
1. 插入一行
    ```python
    user = {
        "name": "xujunhao",
        "age": 18,
        "sex": "male"
    }
    user_id = user_collection.insert(user)
    ```
1. 插入多行
    ```python
    users = [
        {
            "name": "xujunhao1",
            "age": 18,
            "sex": "male"
        },{
            "name": "xujunhao2",
            "age": 28,
            "sex": "female"
        },{
            "name": "xujunhao3",
            "age": 38,
            "sex": "male"
        },{
            "name": "xujunhao4",
            "age": 48,
            "sex": "female"
        }
    ]
    user_id = user_collection.insert(users)
    ```
##### 查询文档
> `collection.find_one()` 返回一条或者none
```python
res = user_collection.find_one({"name":"xujunhao"})
print(res)
```
> `collection.find()` 返回多条或者none
```python
res = user_collection.find({"name":"xujunhao"})
for i in res:
    print(i)
```
> `collection.find().count()` 返回条数
```python
num = user_collection.find({"name":"xujunhao"}).count()
print(num)
```
##### 修改文档
```python
res = user_collection.update({"name":"xujunhao"},{"$set":{"name":"mike"}})
```
##### 删除文档
```python
res = user_collection.remove({"name":"xujunhao"})
print(res)
```
