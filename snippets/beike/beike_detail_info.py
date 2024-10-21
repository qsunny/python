import requests
from lxml import etree
import json
import random
import pymysql
import time
import traceback
import re

def check_url_prefix(url, prefix):
    return url.startswith(prefix)

def detail_info_handle(detail_url, primary_key):
    response = requests.get(detail_url)
    html_content = response.text
    html = etree.HTML(html_content)
    data = html.xpath("//span[@class='xiaoquInfoContent']")
    price_obj = html.xpath("//span[@class='xiaoquUnitPrice']/text()")
    # print(price_obj)

    position ='无位置信息'
    price ='没有参考价格'
    if len(price_obj) >0:
        price = price_obj[0]
    # print(data)
    detail = []
    prefix = "https://"
    if check_url_prefix(detail_url, prefix):
        detail.append("未知")
    for d in data:
        detail.append(re.sub(r'\s+', '', d.xpath("text()")[0]))
        # print(d.xpath("text()"))
        xiaoqu = d.xpath("./span/@xiaoqu")
        if len(xiaoqu) > 0:
            # print(xiaoqu[0])
            position = xiaoqu[0]
    detail.append(position)
    print(price)
    detail.append(price)
    sql_handle(detail, primary_key)

def sql_handle(detail,primary_key):
    print(detail)
    sql = "update tdg_bk_xiaoqu_2375 set build_year='%s',build_type='%s', property_fees='%s', property_company='%s', dev_company='%s',building_amount='%s',households_amount='%s',shop_address='%s',latitude_and_longitude='%s', single_price='%s' where xiaoqu_id = '%d'" % (detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], detail[6], detail[7], detail[8], detail[9], primary_key)
    print(sql)
    try:
        save_mysql(sql)
        pass
    except Exception:
        pass


#写入数据库
def save_mysql(sql):
    #db = pymysql.connect("127.0.0.1", "root", "tulang@751751", "tudgo_temp", charset='utf8')
    db = pymysql.connect(host="127.0.0.1", user="root", password="751", database="tudgo_temp", charset='utf8')
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        print("============"+time.strftime('%Y-%m-%d %H:%M:%S')+"=====update success=====")
        return cursor.fetchone()
    except Exception as e:
        # 发生错误时回滚
        e.print_exc()
        # db.rollback()
    # 关闭数据库连接
    cursor.close()
    db.close()

def page_select_table():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="51751", database="tudgo_temp", charset='utf8')
    cur = conn.cursor()
    # 设置每页的大小和起始偏移量
    page_size = 10  # 每页的记录数
    offset = 27976  # 起始偏移量
    while True:
        # 执行分页查询
        cur.execute("SELECT * FROM tdg_bk_xiaoqu_2375 LIMIT %s OFFSET %s", (page_size, offset))

        # 获取当前页的结果集
        result = cur.fetchall()

        # 如果结果集为空，则表示查询结束
        if not result:
            break

        # 处理当前页的结果集
        for row in result:
            # 对每一行数据进行处理，例如打印输出
            # print(row)
            # a = random.randint(1, 3)
            # print("==============反反爬间歇性睡眠 %d 秒==============" % a)
            # time.sleep(a)
            try:
                detail_info_handle(row[2], row[0])
                pass
            except Exception as e:
                print("发生异常:", str(e))
                continue
        ''' if offset > 50:
            break '''
        # 增加偏移量，准备下一页的查询
        offset += page_size
        print("============"+time.strftime('%Y-%m-%d %H:%M:%S')+"=====select success=====" + str(offset))

    # 关闭游标和连接
    cur.close()
    conn.close()

if __name__ == "__main__":
    # url = 'https://sz.lianjia.com/xiaoqu/2411048675615/'
    # sql = 'select count(*) from tdg_xiaoqu where 1=1'
    page_select_table()
    # detail_info_handle('https://sz.ke.com/xiaoqu/2411063100394/', 5147)
    # get_from_second_page_data(url, 1)
    print('……………………执行结束…………………………')
