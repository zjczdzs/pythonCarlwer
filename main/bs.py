from bs4 import BeautifulSoup
import Request
import re

findlink = re.compile('<a href="(.*?)"')
findlink2 = re.compile('>(.*?)<')
replacelable = re.compile("<[^>]+>")


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

    # data = soup.find(class_='review-content clearfix')
    # movieList = soup.select('div .movie-content > a')
    # print(data)


def main():
    url = 'https://movie.douban.com/subject/1291546/'
    html = Request.request(url)
    beautifulSoup(html)

    # print(html)


if __name__ == '__main__':
    main()