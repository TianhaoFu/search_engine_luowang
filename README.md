# search_engine_luowang
一款针对音乐网站落网的简单垂直领域搜索引擎

主要通过ES及python 完成程序的编写

## 1.语言
python java jdk

## 2.python版本
python38

## 3.依赖库
<1>. bs4  
<2>.requests
<3>.lxml
<4>.re
<5>.elasticsearch
## 4. 运行前期准备
<1>.下载所需库

<2>.运行music_spider.py文件，爬得所需数据data_content文件

<3>.将数据转换为json格式。http://www.bejson.com/，得到data_json2.txt文件

<4>.安装elasticsearch。在elasticsearch-7.4.2\bin目录下使用命令elasticsearch启动elasticsearch

通过浏览器地址栏输入http://localhost:9200/查看是否启动成功
## 5. 运行使用说明
### <1>.启动elasticsearch
在elasticsearch-7.4.2\bin目录下使用命令elasticsearch启动elasticsearch

通过浏览器地址栏输入http://localhost:9200/查看是否启动成功

### <2>.可视化es-head插件

#### 运行node-v12.13.0-x64.exe安装node.js

#### 用命令npm install -g grunt-cli安装grunt到node.js的目录下

#### 在elasticsearch-head-master目录下使用命令grunt server

#### 通过浏览器地址栏输入http://localhost:9100/查看

### <3>打开搜索引擎

#### 在名为web的文件夹的目录下

python -m http.server

#### 得到域名

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

#### 根据地址打开搜索引擎http://localhost:8000/

（使用的是python3.7自带的本地web服务器）

#### 现在你可以尽情使用这个搜索引擎了
