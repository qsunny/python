import requests
from lxml import etree

# 假设这是您从网页获取的HTML内容
html_content = """  
<html>  
<head><title>示例页面</title></head>  
<body>  
    <header>  
        <h1>这是页面的标题</h1>  
        <p>一些额外的信息...</p>  
    </header>  
    <main>页面主要内容...</main>  
</body>  
</html>  
"""

# 构造网页内容获取函数
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def etreeHtml():
    # 解析HTML内容
    tree = etree.HTML(html_content)

    # 使用XPath定位<header>元素
    header_elements = tree.xpath('//header')

    # 遍历所有<header>元素（在这个例子中只有一个）
    for header in header_elements:
        # 打印<header>元素的整个HTML内容
        print(etree.tostring(header, pretty_print=True).decode())

        # 或者，如果你只想获取<header>元素内的文本（不包括子元素的标签）
        # 注意：这将合并所有文本节点，忽略HTML标签
        text_content = header.xpath('string()')
        print("Header的文本内容:", text_content)


def get_data_api():

    url = 'https://odin.sohu.com/odin/api/blockdata'  # Ajax请求的URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    # 可能还需要添加其他请求头，如'Authorization', 'Cookie'等
    json_data = {"pvId":"1722242808065_Crcq3Aq","pageId":"1722243124644_1722235356345odi_CNm","mainContent":{"productType":"13","productId":"324","secureScore":"5","categoryId":"47","adTags":"11111111","authorId":121135924},"resourceList":[{"tplCompKey":"FeedSlideloadAuthor_2_0_pc_1655965929143_data2","isServerRender":False,"isSingleAd":False,"configSource":"mp","content":{"productId":"325","productType":"13","size":20,"pro":"0,1,3,4,5","feedType":"XTOPIC_SYNTHETICAL","view":"operateFeedMode","innerTag":"work","spm":"smpc.channel_248.block3_308_hHsK47_2_fd","page":1,"requestId":"1722242864604S4BP8jN_324"},"adInfo":{},"context":{"mkey":"115584"}}]}
    response = requests.post(url, json=json_data, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打印响应的内容
        print('请求成功:', response.text)
        data = response.json()  # 假设响应是JSON格式的
        print(data)
        content_list = data['data']['FeedSlideloadAuthor_2_0_pc_1655965929143_data2']['list'];
        for content_json in  content_list:
            # print(content_json)
            print(content_json['title'])
            print(content_json['brief'])

    else:
        # 如果请求不成功，打印状态码
        print('请求失败:', response.status_code)



if __name__ == "__main__":
    # html = get_html("https://www.sohu.com/media/115584")
    get_data_api()