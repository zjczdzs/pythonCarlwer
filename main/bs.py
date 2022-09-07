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
    #data = soup.find(class_='review-content clearfix')
    #data = soup.find(class_='feed')
    data = soup.select('div .feed > a')
    try:
        datalink = re.findall(findlink,str(data[0]))[0]
    except Exception:
        print("cant find page")
        return ''

    #print(data)
    #print(datalink)

    #第二层页面
    html2 = Request.request(datalink)
    soup2 = BeautifulSoup(html2,'xml')
    #print(soup2.prettify())
    link = soup2.select('link')
    #print(link[1])

    #第三层页面
    datalink1 = re.findall(findlink2,str(link[1]))[0]
    html3 = Request.request(datalink1)
    soup3 = BeautifulSoup(html3,'html.parser')
    #print(soup3.prettify())
    realdata = soup3.select('div[class="review-content clearfix"]')
    realdata = str(realdata).replace("<br/>","\n")
    realdata = realdata.replace("]","")
    realdata = realdata.replace("[","")
    realdata = realdata.replace("\xa0","")
    #print(realdata)
    returndate = re.sub(replacelable,"",realdata)
    #print(returndate)
    return returndate

    #List = soup.find_all(class_='movie-content')
    #movieList = soup.select('div .movie-content > a')
    #print(List)


def main():
    #url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='
    url = 'https://movie.douban.com/subject/1291546/'
    html = Request.request(url)
    beautifulSoup(html)

    #print(data)
    #beautifulSoup(html)


if __name__ == '__main__':
    main()