import os
import requests
from lxml import etree
import json
import pymysql
import time
import random
import traceback

def get_city_area_urls(url):
    # print(url)
    response = requests.get(url)
    html_content = response.text
    html = etree.HTML(html_content)
    href_items = html.xpath("//div[@data-role='ershoufang']/div/a/@href")
    return href_items


# 发送HTTP请求获取网页内容
def list_main_info(url):
    # url = "https://sz.lianjia.com/xiaoqu/luohuqu/"
    response = requests.get(url)
    html_content = response.text
    print(html_content)
    # 使用lxml库的etree模块将HTML内容转换为可解析的对象
    html = etree.HTML(html_content)
    try:
        total_page = html.xpath("//div[@page-data]/@page-data")[0]
        total_page_json = json.loads(total_page)
        print(total_page_json)
        # totalPage.gettext()
        total_page_amount = int(total_page_json["totalPage"])
        # 使用XPath表达式提取需要的数据
        # data = html.xpath("//div[@class='title']/text()")
        data = html.xpath("//div[@class='info']")
        for d in data:
            items = [d.xpath("div[@class='title']/a/text()")[0], d.xpath("div[@class='title']/a/@href")[0],
                     d.xpath("div/a[@class='district']/text()")[0], d.xpath("div/a[@class='bizcircle']/text()")[0]]
            # print(items)
            str_json(items)
        i = 1
        while i < total_page_amount:
            url_i = remove_trailing_slash(url) + "/pg" + (str(i+1))
            print(url_i)
            get_from_second_page_data(url_i)
            i += 1
    except Exception as e:
        print('extract_info: ', e)
        print("=========发生异常，页面没有小区数据 自动进行下一页=====")


def get_from_second_page_data(page_url):
    a = random.randint(2, 5)
    print("反反爬间歇性睡眠 %d 秒" % a)
    time.sleep(a)
    response = requests.get(page_url)
    html_content = response.text
    html = etree.HTML(html_content)
    #print(html)
    data = html.xpath("//div[@class='info']")
    #print(data)
    for d in data:
        bizcircle_value = ''
        bizcircle = d.xpath("div/a[@class='bizcircle']/text()")
        if len(bizcircle) > 0:
            bizcircle_value = bizcircle[0]
        items = [d.xpath("div[@class='title']/a/text()")[0], d.xpath("div[@class='title']/a/@href")[0],
                 d.xpath("div/a[@class='district']/text()")[0], bizcircle_value]
        # str_json(items)


def str_json(items):
    sql = "insert ignore into tdg_bk_xiaoqu(xiaoqu_name, xiaoqu_url, area, street) values('%s','%s','%s','%s')" %(items[0], items[1], items[2], items[3])
    print(sql)
    rmysql(sql)


#写入数据库
def rmysql(sql):
    #db = pymysql.connect("127.0.0.1", "root", "tulang@751751", "tudgo_temp", charset='utf8')
    db = pymysql.connect(host="127.0.0.1", user="root", password="1751", database="tudgo_temp", charset='utf8')
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        print("============"+time.strftime('%Y-%m-%d %H:%M:%S')+"=====insert success=====")
        return cursor.fetchone()
    except:
        # 发生错误时回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()

def remove_trailing_slash(url):
    if url.endswith('/'):
        url = url[:-1]  # 使用切片去掉最后一个字符
    return url


if __name__ == "__main__":
    # url = "https://zs.ke.com/xiaoqu/xiaolanzhen1"
    # list_main_info(url)
    '''
    # 合并数组
    array1 = [1, 2, 3, 4]
    array2 = [3, 4, 5, 6]
    merged_array = array1 + array2

    # 删除重复项
    unique_array = list(set(merged_array))

    # 打印结果
    print(unique_array) 'https://zs.ke.com', 'https://sz.ke.com', 'https://gz.ke.com', 'https://dg.ke.com', 'https://fs.ke.com', 'https://zh.ke.com'
    '''
    root_url_list = ['https://jieyang.anjuke.com/']
    for root_url in root_url_list:
        xq_path = '/community/p1/'
        # 获取所有区的根URL
        area_urls = get_city_area_urls(root_url + xq_path)
        print(area_urls)
        # 获取街道
        new_urls_array = ['https://jieyang.anjuke.com/community/p1/']
        # 获取所有区街道办的URL
        for url in area_urls:
            street_urls = get_city_area_urls(root_url + url)
            for element in street_urls:
                if element not in area_urls:
                    new_urls_array.append(element)
        if not new_urls_array:
            for url in area_urls:
                list_main_info(root_url + url)
        else:
            for url in new_urls_array:
                print(url)
                list_main_info(root_url + url)

    ''' 
        # 深圳
        urls = ['https://sz.lianjia.com/xiaoqu/luohuqu/',
                'https://sz.lianjia.com/xiaoqu/futianqu/',
                'https://sz.lianjia.com/xiaoqu/nanshanqu/',
                'https://sz.lianjia.com/xiaoqu/yantianqu/',
                'https://sz.lianjia.com/xiaoqu/baoanqu/',
                'https://sz.lianjia.com/xiaoqu/longgangqu/',
                'https://sz.lianjia.com/xiaoqu/longhuaqu/',
                'https://sz.lianjia.com/xiaoqu/guangmingqu/',
                'https://sz.lianjia.com/xiaoqu/pingshanqu/',
                'https://sz.lianjia.com/xiaoqu/dapengxinqu/']
        # 东莞
    '''
    # urls = ['https://dg.lianjia.com/xiaoqu/nanchengqu/','https://dg.lianjia.com/xiaoqu/dongchengqu/','https://dg.lianjia.com/xiaoqu/wanjiangqu/','https://dg.lianjia.com/xiaoqu/wanchengqu/','https://dg.lianjia.com/xiaoqu/liaobuzhen1/','https://dg.lianjia.com/xiaoqu/humenzhen3/','https://dg.lianjia.com/xiaoqu/changanzhen1/','https://dg.lianjia.com/xiaoqu/songshanhugaoxinqu/','https://dg.lianjia.com/xiaoqu/houjiezhen2/','https://dg.lianjia.com/xiaoqu/gaobuzhen1/','https://dg.lianjia.com/xiaoqu/daojiaozhen/','https://dg.lianjia.com/xiaoqu/hongmeizhen/','https://dg.lianjia.com/xiaoqu/shatianzhen/','https://dg.lianjia.com/xiaoqu/dalingshanzhen1/','https://dg.lianjia.com/xiaoqu/changpingzhen/','https://dg.lianjia.com/xiaoqu/dalangzhen/','https://dg.lianjia.com/xiaoqu/huangjiangzhen/','https://dg.lianjia.com/xiaoqu/zhangmutouzhen/','https://dg.lianjia.com/xiaoqu/tangshazhen/','https://dg.lianjia.com/xiaoqu/qingxizhen/','https://dg.lianjia.com/xiaoqu/fenggangzhen/','https://dg.lianjia.com/xiaoqu/dongkengzhen/','https://dg.lianjia.com/xiaoqu/qishizhen/','https://dg.lianjia.com/xiaoqu/shipaizhen/','https://dg.lianjia.com/xiaoqu/chashanzhen/','https://dg.lianjia.com/xiaoqu/machongzhen/','https://dg.lianjia.com/xiaoqu/henglizhen/','https://dg.lianjia.com/xiaoqu/shilongzhen/','https://dg.lianjia.com/xiaoqu/shijiezhen1/','https://dg.lianjia.com/xiaoqu/zhongtangzhen/','https://dg.lianjia.com/xiaoqu/wangniudunzhen/','https://dg.lianjia.com/xiaoqu/qiaotouzhen/','https://dg.lianjia.com/xiaoqu/xiegangzhen/']

    # 惠州
    # urls = ['https://hui.lianjia.com/xiaoqu/huicheng/','https://hui.lianjia.com/xiaoqu/zhongkaigaoxinjishuchanyekaifaqu/','https://hui.lianjia.com/xiaoqu/huiyang/','https://hui.lianjia.com/xiaoqu/dayawan/','https://hui.lianjia.com/xiaoqu/huidong/','https://hui.lianjia.com/xiaoqu/boluo/']
    # 广州
    #urls = ['https://gz.lianjia.com/xiaoqu/tianhe/', 'https://gz.lianjia.com/xiaoqu/yuexiu/', 'https://gz.lianjia.com/xiaoqu/liwan/', 'https://gz.lianjia.com/xiaoqu/haizhu/', 'https://gz.lianjia.com/xiaoqu/panyu/', 'https://gz.lianjia.com/xiaoqu/baiyun/', 'https://gz.lianjia.com/xiaoqu/huangpugz/', 'https://gz.lianjia.com/xiaoqu/conghua/', 'https://gz.lianjia.com/xiaoqu/zengcheng/', 'https://gz.lianjia.com/xiaoqu/huadou/', 'https://gz.lianjia.com/xiaoqu/nansha/', 'https://gz.lianjia.com/xiaoqu/nanhai/']
    # 佛山
    # urls = ['https://fs.lianjia.com/xiaoqu/chancheng/','https://fs.lianjia.com/xiaoqu/nanhai/','https://fs.lianjia.com/xiaoqu/shunde/','https://fs.lianjia.com/xiaoqu/sanshui1/','https://fs.lianjia.com/xiaoqu/gaoming1/','https://fs.lianjia.com/xiaoqu/panyu/','https://fs.lianjia.com/xiaoqu/baiyun/']
    # 中山

    # 珠海
    '''
    urls = ['https://zh.lianjia.com/xiaoqu/gaoxinqu21/','https://zh.lianjia.com/xiaoqu/hengqinqu/','https://zh.lianjia.com/xiaoqu/xiangzhouqu/','https://zh.lianjia.com/xiaoqu/jinwanqu/','https://zh.lianjia.com/xiaoqu/doumenqu/']
    for url in urls:
        main(url)
    '''
    ''' *** url = "https://sz.lianjia.com/xiaoqu/luohuqu/"
    total = 1193
    page_size = 30
    page_total = int(total / page_size)
    remain_der_part = total % page_size
    if remain_der_part > 0:
        page_total = page_total + 1
        print(page_total)
    i = 1
    while i < page_total:
        url_i = url + "pg" + (str(i+1))
        print(url_i)
        i += 1
    '''