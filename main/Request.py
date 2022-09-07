import urllib.request

from pip._vendor import requests, urllib3


def request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.175.400 QQBrowser/11.1.5155.400"}
    response = requests.get(url,headers = headers)
    html = response.content.decode('utf-8')
    #print(html)
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
    #print(html)
    return html

def Urllib3(url):
    proxy = urllib3.PoolManager()
    res = proxy.request('GET', url)
    print(res.data)
    return res.data

def main():
    url = 'https://www.hao123.com/'
    # url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='
    _ = request(url)
    #_ = Urllib(url)
    #_ = Urllib3(url)

if __name__ == '__main__':
    main()