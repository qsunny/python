import requests
from bs4 import BeautifulSoup
import time
import random

'''
conda install -c conda-forge beautifulsoup4
'''



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def get_html(url):
    resp = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(resp.text, features="html.parser")
    return soup


def get_next_page(soup):
    next_page = soup.find(class_='previous-comment-page')
    next_page_href = next_page.get('href')
    return f'http:{next_page_href}'


def get_img_url(soup):
    a_list = soup.find_all(class_ = 'view_img_link')
    urls = []
    for a in a_list:
        href = 'http:' + a.get('href')
        urls.append(href)
    return urls


def save_image(urls):
    for item in urls:
        name = item.split('/')[-1]
        resp = requests.get(url=item, headers = headers)
        with open('D:/temp/images/' + name, 'wb') as f:
            f.write(resp.content)
        time.sleep(random.randint(2,5))


if __name__ == "__main__":
    soup = get_html("http://jandan.net/zoo")
    urls = get_img_url(soup)

    save_image(urls)
    urls = get_next_page(soup)
    save_image(urls)