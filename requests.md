[toc]
# 简介
1. 用python语言基于urllib编写
1. requests是最简单易用的HTTP库
 
---
# 安装
> *`cmd.exe`*
```
pip install requests
```
 
---
# 引入
> *`test.py`*
```
import requests
```
 
---
# 基本GET请求
#### 无参数
> 代码路径: `F:\WWW\wangyi_py\index.py`
```python
import requests
r = requests.get('http://httpbin.org/get')
print(r.url)
```
> 运行结果: `cmd.exe`
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
http://httpbin.org/get
```
#### 有参数
> 代码路径: `F:\WWW\wangyi_py\index.py`
```python
import requests
payload = {
    'key1': 'value1',
    'key2': 'value2'
}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
```
> 运行结果: `cmd.exe`
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
http://httpbin.org/get?key1=value1&key2=value2
```
#### 设置header
> 代码路径: `F:\WWW\wangyi_py\index.py`
```python
import requests
headers = {
    'hello': 'world'
}
r = requests.get('http://httpbin.org/get', headers=headers)
print(r.text)
```
> 运行结果: `cmd.exe`
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Hello": "world",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.17.3"
  },
  "origin": "61.52.106.18",
  "url": "http://httpbin.org/get"
}
```
 
---
# 基本POST请求
#### 有数据
> 代码路径: `F:\WWW\wangyi_py\index.py`
```python
import requests
payload = {
    'hello': 'world'
}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
```
> 运行结果: `cmd.exe`
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "hello": "world"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "11",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.17.3"
  },
  "json": null,
  "origin": "61.52.106.18",
  "url": "http://httpbin.org/post"
}
```
#### 有数据(json格式)
> 代码路径: `F:\WWW\wangyi_py\index.py`
```python
import requests
import json
payload = {
    'hello': 'world'
}
r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
print(r.text)
```
> 运行结果: `cmd.exe`
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
{
  "args": {},
  "data": "{\"hello\": \"world\"}",
  "files": {},
  "form": {},
  "headers": {
   "Accept": "*/*",
   "Accept-Encoding": "gzip, deflate",
   "Connection": "close",
   "Content-Length": "18",
   "Host": "httpbin.org",
   "User-Agent": "python-requests/2.17.3"
  },
  "json": {
   "hello": "world"
  },
  "origin": "61.52.106.18",
  "url": "http://httpbin.org/post"
}
```
#### 上传文件
> 代码路径: `F:\WWW\wangyi_py\index.py`
```python
import requests
url = 'http://httpbin.org/post'
files = {
    'file': open('test.txt', 'rb')
}
r = requests.post(url, files=files)
print(r.text)
```
> 文件内容: `F:\WWW\wangyi_py\test.txt`
```
hello world !!!!!!!!!!!!!!!!!!
```
> 运行结果: `cmd.exe`
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
{
  "args": {},
  "data": "",
  "files": {
    "file": "hello world !!!!!!!!!!!!!!!!!!"
  },
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "174",
    "Content-Type": "multipart/form-data; boundary=19732374a5934f6598891cef4524bee0",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.17.3"
  },
  "json": null,
  "origin": "61.52.106.18",
  "url": "http://httpbin.org/post"
}
```
 
---
# Cookies
> 代码路径: *`F:\WWW\wangyi_py\index.py`*
```python
import requests
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
```
> 运行结果: *`cmd.exe`*
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
{
  "cookies": {
    "cookies_are": "working"
  }
}
```
---
# 请求超时配置
> 代码路径: *`F:\WWW\wangyi_py\index.py`*
```python
import requests
url = 'http://github.com'
r = requests.get(url, timeout=0.001)
print(r.text)
```
> 运行结果: *`cmd.exe`*
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
Traceback (most recent call last):
  File "C:\Program Files\Python36\lib\site-packages\urllib3\connection.py", line 141, in _new_conn
    (self.host, self.port), self.timeout, **extra_kw)
  File "C:\Program Files\Python36\lib\site-packages\urllib3\util\connection.py", line 83, in create_connection
    raise err
  File "C:\Program Files\Python36\lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
socket.timeout: timed out
```
 
---
# 持久会话
#### 没有持久会话的情况
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
import requests
requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)
```
> 运行结果: *`cmd.exe`*
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
{
  "cookies": {}
}
```
#### 设置持久会话的情况
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
```
> 运行结果: *`cmd.exe`*
```
F:\WWW\wangyi_py>python "f:\WWW\wangyi_py\index.py"
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
```
---
# 代理
> 文件路径: *`F:\WWW\wangyi_py\index.py`*
```python
import requests
proxies = {
    'https': 'http://41.118.132.69:4433'
}
r = requests.post('https://www.baidu.com', proxies=proxies)
print(r.status_code)
```
