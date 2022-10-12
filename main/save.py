import pymysql

import GetALLSpider

def savedata(datelist):
    path = 'D:/result/'
    i = 1
    # 打开数据库连接
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='12323245',
                           charset='utf8',
                           database='abcdefg'
                           )

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    for data in datelist:
        savepath = path + str(i) + '.txt'
        sql = "insert into carlwer(url) value('%s')" % (savepath)
        print("save" + savepath + "OK")
        i = i + 1
        if data is not None and data != "":
            with open(savepath, "w", encoding='utf-8') as f:
                f.write(str(data))  # 自带文件关闭功能，不需要再写f.close()
            cursor.execute(sql)
            conn.commit()


if __name__ == '__main__':
    savedata(GetALLSpider.main())