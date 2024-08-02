import requests
from lxml import etree

# 构造网页内容获取函数
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 构造获取大学排名信息列表 使用xpath解析网页
def parse_html(ulist, html):
    html_doc = etree.HTML(html)
    for box in html_doc.xpath('//tbody/tr'):
        num = box.xpath('./td[1]/div/text()')[0]
        name = box.xpath('./td[2]//span/text()')[0]
        area = box.xpath('./td[3]/text()')[0]
        rank_country = box.xpath('./td[4]/text()')[0]
        score = box.xpath('./td[5]/text()')[0]
        schoolmate_score = box.xpath('./td[5]/text()')[0]

        univ = {
            'num': str(num).strip(),
            'name': str(name).strip(),
            'area': str(area).strip(),
            'rank_country': str(rank_country).strip(),
            'score': str(score).strip(),
            'schoolmate_score': str(schoolmate_score).strip()
             }

        ulist.append(univ)


# 构造输出函数
def print_univlist(ulist):
    #格式化输出 chr(12288)，中文填充
    x = chr(12288)
    tplt = "{0:<10}\t{1:<25}\t{2:{6}<10}\t{3:<15}\t{4:<10}\t{5:<10}"
    print(tplt.format('排名', '学校名称', '地区', '国家/地区排名', '总分', '校友获奖', chr(12288)))
    for i in ulist:
        print(tplt.format(i['num'], i['name'], i['area'], i['rank_country'], i['score'], i['schoolmate_score'], chr(12288)))



if __name__ == "__main__":
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/arwu/2023"
    html = get_html(url)
    parse_html(uinfo, html)
    # print(uinfo)
    print_univlist(uinfo)