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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
# 指定 ChromeDriver 的路径
options = webdriver.ChromeOptions()
# 设置一些选项（如果需要的话）
# options.add_argument(...)
# browser = webdriver.Chrome(executable_path ="D:\download\chromedriver-win64\chromedriver.exe", options=options)
# service = Service(executable_path='D:\download\chromedriver-win64\chromedriver.exe')
service = Service(executable_path='C:\Users\Administrator\Downloads\chrome-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)
# 等待页面加载完成（如果需要）
browser.implicitly_wait(10)

# 执行一些JavaScript（如果需要）
# browser.execute_script("some_javascript_code")

def open_sohu():
    website_URL ="https://www.sohu.com/media/115584"
    browser.get(website_URL)

    # 提取数据（例如，从某个元素的属性或文本中）
    data_parent = browser.find_element(By.CLASS_NAME, 'recommend-content-wrap')

    children = data_parent.find_elements(By.XPATH, '//div[@data-spm="block3_308_NDdFbm_1_fd"]')
    print(children)
    for child_ele in children:
        content_ele = child_ele.find_element(By.CLASS_NAME, 'item-text-content-title').text
        content_desc_ele = child_ele.find_element(By.CLASS_NAME, 'item-text-content-description').text
        print(content_ele)
        print(content_desc_ele)

    WebDriverWait(browser, 30)
    time.sleep(10)





if  __name__ == "__main__":
    open_sohu()
    browser.quit()