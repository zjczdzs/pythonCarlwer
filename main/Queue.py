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