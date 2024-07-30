# -*- coding: utf-8 -*-
"""
pip install "feapder[all]"
https://feapder.com/#/README
Created on 2024-07-29 14:33:33
---------
@summary:
---------
@author: Administrator
"""

import feapder


class FirstSpider(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://odin.sohu.com/odin/api/blockdata")

    def parse(self, request, response):
        article_list = response.xpath('//div[@class="block3_308_NDdFbm_1_fd"]')
        print(article_list)
        for article in article_list:
            title = article.xpath('//*[@class="item-text-content-title"]')
            desc = article.xpath("./div[@class='item-text-content-description']")
            print(title, desc)


if __name__ == "__main__":
    FirstSpider().start()