# -*- codiing:utf-8 -*-
"""
Selenium-自动化测试
pip install selenium
chromedriver下载地址 https://googlechromelabs.github.io/chrome-for-testing/
"""

__author__ = "aaron.qiu"


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# 指定 ChromeDriver 的路径
options = webdriver.ChromeOptions()
# 设置一些选项（如果需要的话）
# options.add_argument(...)
# browser = webdriver.Chrome(executable_path ="D:\download\chromedriver-win64\chromedriver.exe", options=options)
service = Service(executable_path='D:\download\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

def open_baidu():
    website_URL ="https://www.baidu.com"
    browser.get(website_URL)

    refreshrate = int(3) #每3秒刷新一次Google主页。
   # 它会一直运行，直到你停掉编译器
    while True:
        time.sleep(refreshrate)
        browser.refresh()


def baidu_home():
    website_URL ="https://www.baidu.com"
    browser.get(website_URL)

    we = browser.find_element(By.ID, "kw")
    we.send_keys("python")
    browser.find_element(By.ID, "su").click()
    time.sleep(5)



if  __name__ == "__main__":
    baidu_home()
    browser.quit()