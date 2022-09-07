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