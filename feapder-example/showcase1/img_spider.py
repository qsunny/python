import datetime
import os
import random
import string

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 配置请求头，模拟浏览器行为
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


# 爬取图片的函数
def download_images(url, output_folder):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for img in img_tags:
        img_url = img.attrs.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            img_data = requests.get(img_url, headers=headers, timeout=5).content
            file_name = os.path.join(output_folder, generate_file_name(img_url))
            with open(file_name, 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded image: {file_name}")
        except Exception as e:
            print(f"Error downloading image: {img_url}. Error: {e}")


def generate_file_name(img_url):
    now = datetime.datetime.now()
    # "%Y-%m-%d %H:%M:%S"
    formatted_time = now.strftime("%Y%m%d")
    # print(formatted_time)

    random_num_list = random.sample(string.digits, 6)
    random_num_str = ''.join(random_num_list)
    # co103711420240717816509
    file_name = '{0}{1}'.format(formatted_time, random_num_str)

    if img_url.find(".jpg") != -1:
        file_name = '{0}.{1}'.format(file_name, 'jpg')
    elif img_url.find(".jpeg") != -1:
        file_name = '{0}.{1}'.format(file_name, 'jpeg')
    else:
        file_name = '{0}.{1}'.format(file_name, 'png')

    print(img_url)
    print(file_name)
    return file_name


if __name__ == '__main__':
    target_url = 'https://588ku.com/ycbeijing/7331353.html'  # 替换为你要爬取的网站URL
    output_folder = 'C:\\Users\\Administrator\\Desktop\\images'  # 图片保存的文件夹名称
    download_images(target_url, output_folder)