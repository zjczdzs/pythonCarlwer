import GetALLSpider

def savedata(datelist):
    path = 'C:\\Users\\ZHAI\\Desktop\\spiderresult\\'
    i = 0
    for data in datelist:
        savepath = path + str(i) + ".txt"
        i = i + 1
        with open(savepath, "w") as f:
            f.write(data)  # 自带文件关闭功能，不需要再写f.close()

if __name__ == '__main__':
    savedata(GetALLSpider.main())