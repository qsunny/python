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
def parse_html(ulist,html):
    html_doc = etree.HTML(html)
    for box in  html_doc.xpath('//tbody/tr'):
        num = box.xpath('./td[1]/div/text()')[0]      # 添加[0]输出格式为{'num': '1', 'name': '清华大学（北京）', 'area': '大陆', 'score': '100'}
        name = box.xpath('./td[2]//span[@class="name-cn"]/text()')[0]  # 没有[0]输出格式为{'num': ['1'], 'name': ['清华大学（北京）'], 'area': ['大陆'], 'score': ['100']}
        en_name = box.xpath('./td[2]//span[@class="name-en"]/text()')[0]
        tags = box.xpath('./td[2]//p/text()')[0]
        area = box.xpath('./td[3]/text()')[0]     # 没有[0]输出格式，在format格式中会报错，因为['1']不是字符串格式
        type = box.xpath('./td[4]/text()')[0]     # 没有[0]输出格式，在format格式中会报错，因为['1']不是字符串格式
        score = box.xpath('./td[5]/text()')[0]

        univ = {
            'num': str(num).strip(),
            'name': str(name).strip(),
            'en_name': str(en_name).strip(),
            'tags': str(tags).strip(),
            'area': str(area).strip(),
            'type': str(type).strip(),
            'score': str(score).strip()
             }

        ulist.append(univ)


# 构造输出函数
def print_univlist(ulist):
    #格式化输出 chr(12288)，中文填充
    x = chr(12288)
    tplt = "{0:<10}\t{1:<10}\t{2:<20}\t{3:{7}<10}\t{4:<10}\t{5:<10}\t{6:<45}"
    print(tplt.format('排名', '学校名称', '标签', '地区', '类型', '总分', '学校英文名称', chr(12288)))
    for i in ulist:
        print(tplt.format(i['num'], i['name'], i['tags'], i['area'], i['type'], i['score'], i['en_name'], chr(12288)))



if __name__ == "__main__":
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2024"
    html = get_html(url)
    parse_html(uinfo, html)
    # print(uinfo)
    print_univlist(uinfo)