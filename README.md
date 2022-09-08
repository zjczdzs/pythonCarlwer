# 一、什么是爬虫

## 1.1 一个情景

话说有一天，孙陈同学偷偷选修了一门叫恋爱心理学的公共选修课。但是这个课跟他想的完全不一样，不仅讲的都是心理学没有恋爱技巧而且想要结课还很难。老师要求每个同学去看100部爱情电影并且每个都写1000字的影评。孙陈就想：傻子才自己一个个去看再去写影评，我就是抄100份影评老师也不会一个个去看我是不是自己写的。于是孙陈就打开了自己的小网站去找爱情电影的影评，但是100份超过3000字的影评不好找，孙陈还得把每个影评放word里去统计字数。还没搞完40份孙陈就苦不堪言，这也太麻烦了太耗时间了。呜呜呜。于是孙陈向他的好室友求助，室友教孙陈写了个爬虫，结果1分钟就给搞完了。虽然笨笨的孙陈写爬虫写了3个小时。

爬虫是一个自动提取网页的程序，与其称为爬虫我更愿称他为”网页爬取机器人“，因为它主要的特性是“自动”和“拟人”。

孙陈正常去一个个上网找影评的流程是这样的，先打开一个爱情电影分类

![image-20220903211055138](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903211055138.png)

然后一个个点开电影的具体页面去找影评，再把它复制到自己的word文件里![image-20220903211303976](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903211303976.png)

这是我们上网的宏观表现，作为一个网上冲浪的浪人我们只需要感知到这种地步就行了。但是想要会爬虫可不能只会这些。

## 1.2 爬虫的原理

**首先我们要知道访问一个网页的流程。**

1. 我们通过浏览器去访问的网页是bs架构的，就是 浏览器/服务器 的架构。当浏览器同过url的路径访问网页时，服务器的这边会接收到url的请求并且返回所请求的数据还给浏览器。（url 叫统一资源定位符）

   ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE3LmNuYmxvZ3MuY29tL2Jsb2cvNjY3MjM4LzIwMTcxMi82NjcyMzgtMjAxNzEyMjkxNjA2MjUwMDctMTQ3NzY3NzM3NC5wbmc?x-oss-process=image/format,png)

![image-20220903212353641](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903212353641.png)

## 3.2 贯穿爬虫过程的检查

返回数据的具体步骤我们可以从检查里看见，在页面上右键  检查

![image-20220903212545242](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903212545242.png)

可以看到右侧的部分，映入眼帘的是elements,也就是网页的html文件。我们可以用鼠标扫过标签去看到标签对应的页面模块，

![image-20220903213030382](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903213030382.png)

点击always下边的第一个图表也可以点击页面模块观察对应的html代码。这点很重要。

下面我们点击elements旁边的network

![image-20220903213147107](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903213147107.png)

可以看见什么都没有，这是正常的，因为网页已经加载好了，暂时并没有发送什么网络请求，所以才是空白。所以我们要刷新一下页面，重新向服务器来请求资源。刷新后点击那个红色图标一下暂停。我们就可以看到网页刚加载的时候他给了我们什么数据。

![image-20220903213516210](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903213516210.png)

点开这个资源可以看到具体资源，因为它是按http网络协议进行数据传输的，所以这里并不是一下就能看到返回的数据，这里是按照http的一个数据格式封装返回的。

![image-20220903213826870](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903213826870.png)

现在看到的是返回数据的Response,也就是请求头，他里面主要包含了，请求信息，浏览器信息，和用户信息。方便服务器返回能够正确显示的内容。

preview是返回数据的预览。我们要看的数据在Response里，也就是服务器的回应。

![image-20220903214504871](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903214504871.png)

![image-20220903214431865](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903214431865.png)

可以看到最终返回给了我们一个页面。

再来找找我们所需要的影评在哪里

![image-20220903215332130](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903215332130.png)

这里我们需要影评在![image-20220903215619806](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220903215619806.png)下面的第一个<div>里的<p>标签里。然后我们差不多就可以写爬虫了。

# 二、爬虫流程

其实把网络爬虫抽象开来看，它无外乎包含如下几个步骤

1. 模拟请求网页。模拟浏览器，打开目标网站。
2. 获取数据。打开网站之后，就可以自动化的获取我们所需要的网站数据。
3. 保存数据。拿到数据之后，需要持久化到本地文件或者数据库等存储设备中。

## 2.1 模拟请求

下面开始准备第一个步骤，模拟请求，打开目标网站

https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=。

这一步在python可以有三个库来实现，我们随便选一个就行

### 2.1.1 **requests**

使用 requests 需要先安装它，安装 requests，只要在你的终端中运行下列命令即可。

```
pip install requests
```

推荐使用`request()`来进行访问的，因为使用`request()`来进行访问有两点好处，

1. 可以直接进行post请求，**不需要将** `data`**参数转换成JSON格式**
2. 直接进行GET请求，**不需要自己拼接url参数**

### 2.1.2 **urllib**

使用 urllib不需要安装它，因为urllib是Python中请求url连接的官方标准库，在Python2中主要为urllib和urllib2，在Python3中整合成了urllib。urllib中一共有四个模块，分别如下：

	- request：主要负责构造和发起网络请求,定义了适用于在各种复杂情况下打开 URL (主要为 HTTP) 的函数和类	
	
	- error：处理异常
	主要包含URLError和HTTPError
	URLError：是error异常模块的基类，由request模块产生的异常都可以用这个类来处理
	HTTPError：是URLError的子类，主要包含三个属性：
	Code:请求的状态码
	reason：错误的原因
	headers：响应的报头
	
	- parse：解析各种数据格式
	
	- robotparser：解析robot.txt文件
	Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。

### 2.1.3 **urllib3**

通过urllib3访问一个网页，那么必须首先构造一个PoolManager对象，然后通过PoolMagent中的request方法或者 `urlopen()`方法来访问一个网页，两者几乎没有任何区别。它的优点在于它有线程安全和连接池自动连接等特性

同样，使用 urllib3需要先安装它，安装 urlli3，只要在你的终端中运行下列命令即可。

```
pip install urllib3
```

### 2.1.4 模拟请求实例

先获取hao123网站 https://www.hao123.com/，为什么不直接进入上面的网站呢，接下来会说原因

```python
import urllib.request
from pip._vendor import requests, urllib3

def request(url):
    response = requests.get(url)
    html = response.content.decode('utf-8')
    print(html)
    return html

def Urllib(url):
    html = ''
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    print(html)
    return html

def Urllib3(url):
    proxy = urllib3.PoolManager()
    res = proxy.request('GET', url)
    print(res.data)
    return res.data

def main():
    url = 'https://www.hao123.com/'
    #_ = request(url)
    #_ = Urllib(url)
    _ = Urllib3(url)

if __name__ == '__main__':
    main()
```

 

下面我们可以试试用request爬https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=。

![image-20220904234730665](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220904234730665.png)

运行这段代码你会发现没有任何结果

我们再尝试输出 `res` 这个变量：

![image-20220904234807501](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220904234807501.png)

可以看到状态码418

出现这个结果的原因是豆瓣网识别到了我们的程序是一个爬虫，而豆瓣网不允许爬虫访问，所以使用爬虫访问豆瓣网就会出现这个结果。

但是现在我们还是想使用爬虫来获取豆瓣网的数据该怎么办呢？

很简单——**伪装成普通用户**。这点就是爬虫的**拟人**

要伪装成普通用户可以设置一个 `headers` 参数。

```python
def request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    response = requests.get(url,headers = headers)
    html = response.content.decode('utf-8')
    print(html)
    return html
```

你也可以用你自己的，在之前检查的network里打开一个翻到最下面有User-Agent

![image-20220904235145928](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220904235145928.png)

## 2.2 获取所需要的数据

### 2.2.1 beautifulsoup

上面我们只是获取了网站html的全部数据，但是我们想要的只是其中的一点数据。所以我们要对其中的数据进行一些操作来获取我们想要的数据。这里用到一个叫美丽汤的包，BeautifulSoup。它是一种网页的解析器，可以把爬下来的杂乱的html或者xml格式化并且封装起来，让我们以比较简单的操作来找到我们想要的内容。官方的解释

```
Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。

Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。
```

|      解析器      | 用法                                | 优点                                                         |
| :--------------: | ----------------------------------- | ------------------------------------------------------------ |
|   python标准库   | BeautifulSoup(markup,‘html.parser’) | python标准库，执行速度适中	(在python2.7.3或3.2.2之前的版本中)文档容错能力差 |
| lxml的HTML解析器 | BeautifulSoup(markup,‘lxml’)        | 速度快，文档容错能力强	需要安装c语言库                    |
| lxml的XML解析器  | BeautifulSoup(markup,‘xml’)         | 速度快，唯一支持XML的解析器	需要安装c语言库               |

安装lxml, bs4

```
pip install lxml

pip install bs4
```

​	使用

```
from bs4 import BeautifulSoup
```

它的许多性质我就不多说了，我只说下能用到的部分，具体性质可以看

https://blog.csdn.net/qq_21933615/article/details/81171951?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166254540816800182135521%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166254540816800182135521&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-81171951-null-null.142

### 2.2.2 **find_all**

find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

```
find_all( name , attrs , recursive , text , **kwargs )
#参数都是可选的
```

一般使用

```
soup.find_all('b')
#找到所有的b标签

soup.find_all(re.compile("^b"))
#用正则表达式找到所有b开头的标签

soup.find_all(["a", "b"])
#找到所有的a标签和b标签

soup.find_all(id='link2')
#找到所有id="link2"的标签

soup.find_all('div',class_="sister")
#找到所有class="sister"的div标签返回列表（class 是 python 的关键词，这怎么办？加个下划线）

soup.find_all('a',id= "item")
#找到所有id="item"的a标签

soup.find_all("a", limit=2)
#限制找到两个a标签	

soup.find_all(text="Elsie")
#找到文档字符串内容
```

### 2.2.3 find

find和find_all没什么区别，find只返回找到的第一个标签，find_all返回所有的列表

### 2.2.4 select

我比较喜欢使用select,他是一种css选择器，即可以通过css的语法进行查找标签

```
soup.select('title')
#通过标签名字寻找

soup.select('.sister')
soup.select('a[class="sister"]')
#通过类名寻找相当于find_all(class_="sister")

soup.select('#link1')
#通过id寻找相当于find_all(id="link1")

soup.select('p #link1')
#查找id="link1"的p标签

soup.select("head > title")
#查找head的子标签title

select('a[href="http://example.com/elsie"]')

soup.select('div .feed > a')
#大部分是这样来用的
```

### 2.2.5 正则表达式库re

还有一个库搭配着用效果更好，就是正则表达式的re库

使用re库

```
import re
```

用法

```
findlink = re.compile('<a href="(.*?)"')
#构造表达式

re.findall(findlink,str)
#在str里匹配表达式findlink的内容

re.sub(findlink,"",data)
#在data里匹配到表达式relpacelable并替换成""
```

正则表达式不熟的推荐看这个网站，比较基础但是很香。用来联系正则表达式够了。

https://codejiaonang.com/#/course/regex_chapter1/0/0

### 2.2.6 BeautifulSoup获取数据实例

下面我们来试试获取 《霸王别姬》的第一个长篇影评

先用![image-20220907200332056](https://github.com/zjczdzs/pythonCarlwer/blob/master/img/img.png)来点击第一个长篇影评找到其在html里面的位置

<img src="https://github.com/zjczdzs/pythonCarlwer/blob/master/img/img.png" alt="image-20220907200555873"/>

展开可以看到长评内容在class="review-content clearfix"的div标签里面

下面我们直接使用find或者select来获取数据

```
soup.find(class_='movie-content')
或者
soup.select('div .movie-content > a')
```

打印一下查找结果数组

![image-20220907201127529](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907201127529.png)

给返回了None,我数据呢？给我吞了？别急我们先打印一下获取的html数据

![image-20220907201821637](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907201821637.png)

这里根本就没有class="review-content clearfix的div标签。为什么呢？因为我们点展开之前页面clss='full-content'的div标签里是什么都没有的。

![image-20220907205419534](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907205419534.png)

也就是说我们爬取的原始页面是没有class="review-content clearfix的div标签

点展开后，页面会再次发送请求获取full的内容，并且改造页面。即增加class="review-content clearfix的div标签

这里我们刷新一下页面，等一会再打开检查里的network，再点展开。可以观察到空白的network出现了一个新的请求。里面返回的就是全部长评内容

![image-20220907210052953](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907210052953.png)

但是短评的a标签里是有一个url的，它是作者页面的链接

![image-20220907210408223](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907210408223.png)

我们可以利用这个链接进去作者的影评页面去继续获取数据，虽然有些麻烦，但是现在也只能这样了。

### 2.2.7 找到第二层页面

我们在第二层页面里找到我们要的数据的尾汁

![image-20220907210720199](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907210720199.png)

这里就是class="review-content clearfix"的div里面了。至于里面的<br\>标签我们需要replace一下成” “还有div标签用re.sub给他匹配到后再删除掉就获取到我们要的数据了

- 这里附上beautifulsoup函数

```
def beautifulSoup(html):
    soup = BeautifulSoup(html,"html.parser")
    # content = soup.prettify()
    # print(content)

    data = soup.select('div .main-bd > h2 > a')
    # print(data)
    try:
        datalink = re.findall(findlink,str(data[0]))[0]
    except Exception:
        print("cant find page")
        return ''
    # print(data)
    # print(datalink)

    # 第二层页面
    html3 = Request.request(datalink)
    soup3 = BeautifulSoup(html3,'html.parser')
    realdata = soup3.select('div[class="review-content clearfix"]')
    realdata = str(realdata).replace("<br/>","\n")
    realdata = realdata.replace("]","")
    realdata = realdata.replace("[","")
    realdata = realdata.replace("\xa0","")
    returndate = re.sub(replacelable,"",realdata)
    # print(returndate)
    return returndate
```

## 2.3保存数据

这一步就比其他的简单多了，因为孙陈急着交作业就不要存入数据库了，直接打开io把列表里每一个数据都写一个word文件输出就好。

这样的数据可能不合适放在mysql里，可以放在文件系统里像hdfs这类的，有兴趣的同学可以自己尝试连接数据库持久化爬到的数据

# 三、爬取多个甚至全站的数据

我们目前爬的是一个网站的数据。但是如果只是爬一个网站的数据我们就不需要再写程序了，直接手动复制就好。要爬取许多网站的数据我们需要一个”母站“。就是通过这一个网站我们能够获取其他同类网站的链接并且自动爬取了。

## 3.1一般网站爬取规律

一般的网站是很简单的，他会把数据以一面固定多少个数据为一个类去展示出来。像阿里巴巴的矢量图标网站。

![image-20220907215902403](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907215902403.png)

可以看到他是直接一个网站显示出来的。底部有页数

![image-20220907215940728](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907215940728.png)

我们如果要爬第二个网站就进入第二面就行了。可以把第二面第三面的url都列出来

```
https://www.iconfont.cn/search/index?searchType=icon&q=&fromCollection=-1&page=1&tag=&fills=

https://www.iconfont.cn/search/index?searchType=icon&q=&fromCollection=-1&page=2&tag=&fills=

https://www.iconfont.cn/search/index?searchType=icon&q=&fromCollection=-1&page=3&tag=&fills=

https://www.iconfont.cn/search/index?searchType=icon&q=&fromCollection=-1&page=4&tag=&fills=

https://www.iconfont.cn/search/index?searchType=icon&q=&fromCollection=-1&page=5&tag=&fills=
```

可以观察到，这些网站都是差不多的，只有page这个数据不一样。

那么我们可以把URL拆解成

"https://www.iconfont.cn/search/index?searchType=icon&q=&fromCollection=-1&page="+ str(i) +"&tag=&fills="

在一个循环里不断构造url就能不断爬到许多页面的数据了

## 3.2 反爬机制

但是算我倒霉，随便挑一个豆瓣的爱情电影网站做爬虫就遇到反爬机制

![image-20220907220537700](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907220537700.png)

这个页面往下翻他是翻不到底的。。。因为它采用了”懒加载“数据。即在你将要翻到该数据时才加载该数据。加载后就将数据加入页面。这点和Android滚动数据的很像。但是这里懒加载的原理是ajax异步请求。当要要翻到该数据时想服务器请求该数据。这一点我还是挺兴奋的。先不说为啥兴奋。

先看一下直接爬这个网站我们能爬到什么

刷新一下立刻点红点停止网络请求，可以能够看到爬取到的页面

![image-20220907233931011](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907233931011.png)

看一下当前页面的preview

![image-20220907234007481](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907234007481.png)

只有一个开头数据一个都没有。

我们刷新页面重新打开检查并且一边往下翻等发送ajax时观察他的network。

![image-20220907225950390](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907225950390.png)

可以看到这个请求的路径是

https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=20&limit=20

问号后面都是参数实际请求路径是https://movie.douban.com/j/chart/top_list?

往下翻到最低有参数列表 看一看到请求了20条数据

![image-20220907230422065](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907230422065.png)

再看看它的response返回的是啥

![image-20220907230526563](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907230526563.png)

这样看不太明显，我们把这段数据放在json转换网站里看一看

![image-20220907230819950](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907230819950.png)

里面有20条数据，每个里面的url就是对应的电影链接。

那么我们直接向这个接口发出请求获取json就可以直接获取所有电影的url了，也不用再去用beautifulsoup去一个个找标签了再正则去除标签了。所以这样你还不兴奋？但是大部分页面初始化的时候就生成了数据了，这样异步请求懒加载的还是少数，大部分时间我们还是得用bs去解析网页。下面代码是从母站获取所有子站链接。要获取200个电影就在直接把params的limit改成200就行了

```
import Request
import bs
from pip._vendor import requests
import time

def askallurl():
    url = 'https://movie.douban.com/j/chart/top_list?'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.175.400 QQBrowser/11.1.5155.400"}
    params = {
        'type': '13',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    try:
        response = requests.get(url,params = params,headers = headers)
    except:
        print(response)
        return ""
    return response.json()

def main():
    start = time.time()
    datalist = []
    movielist = askallurl()
    for movie in movielist:
        #输出爬取子站网址
        print(movie['url'])
        html = Request.request(movie['url'])
        # print('html'+html)
        data = bs.beautifulSoup(html)
        if(data != ''):
            datalist.append(data)
    end = time.time()
    print("爬虫耗时：{} s".format(end - start))
    #print(datalist)
    return datalist

if __name__ == '__main__':
    main()
```

## 3.2 其他的反爬机制

很多人在爬网站的时候，写的好好的突然爬不到数据了，报错会显示413网站拒绝返回数据。这是访问的太频繁被网站认定爬虫被禁止一定时间内爬取网站了。有两个方法可以解决。

1. 配置一个代理ip。
2. 直接换网络，可以用自己的热点或者其他无线网。

还有很多反爬机制有兴趣的可以继续学习。

# 四、多线程爬虫

## 4.1 单线程爬虫的速度

这样虽然已经能爬到数据了，但是速度取决于我们的网速，爬取的很慢很慢

可以看到只是爬20个网站花的时间，其中还有一个链接失效的

![image-20220907232209897](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907232209897.png)

要爬200个更得等好久，所以要想利用我们多核的资源充分去并行爬取我们就得写多线程爬虫。

## 4.2 多线程爬虫工具queue

我是不喜欢写多线程的，因为容易线程出错，还要加锁什么的。但是python提供了一个线程队列queue。他是一个线程安全的自动的队列。每个线程可以轮流从中获取网站链接，而且不会重复和缺少。以代码来理解

```
import threading
import time
import queue
import GetALLSpider
import Request
import bs
import save

DataList = []

# 为线程定义一个函数
class myThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                html = crawl(self.name, self.q)
                if (html != ''):
                    DataList.append(bs.beautifulSoup(html))
            except:
                break
        print("Exiting " + self.name)

def crawl(threadNmae, q):
    url = q.get(timeout=2)
    try:
        html = Request.request(url)
        return html
    except Exception as e:
        print(threadNmae, "Error: ", e)

def quickspider():
    start = time.time()
    movielist = GetALLSpider.askallurl()
    # 填充队列
    workQueue = queue.Queue(len(movielist))
    for movie in movielist:
        workQueue.put(movie['url'])
    threads = []
    for i in range(1, 6):
        # 创建4个新线程
        thread = myThread("Thread-" + str(i), q=workQueue)
        # 开启新线程
        thread.start()
        # 添加新线程到线程列表
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    save.savedata(DataList)
    end = time.time()
    print("Queue多线程爬虫耗时：{} s".format(end - start))
    print("Exiting Main Thread")

if __name__ == '__main__':
    quickspider()
```

这里我开了5个线程。可以看一下多线程有多快。

![image-20220907235734569](C:\Users\ZHAI\AppData\Roaming\Typora\typora-user-images\image-20220907235734569.png)

## 4.3 想要更快？

我们已经充分利用多核计算机的资源进行并行爬虫了。要想更快就得用分布式爬虫，一个集群的机器同时去并行爬取。可以非常快速的完成一个大数据量的爬虫任务。go是个非常智能、完备、简洁、快速的语言。天生就适合做云原生、区块链这种分布式的程序。并且速度非常之快。有兴趣的可以用go写一个爬虫，他里面也有自己的爬虫框架。

