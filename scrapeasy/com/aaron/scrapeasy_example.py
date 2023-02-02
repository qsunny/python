# -*- coding: utf-8 -*-

'''
pip install scrapeasy
pip install lxml
'''

from scrapeasy import Website, Page
from pprint import pprint

if __name__ == "__main__":
    # tikocash.com  没有跑通
    web = Website("https://pixabay.com/zh/")
    links = web.getSubpagesLinks()
    pprint(links)
    images = web.getImages()
    pprint(images)
    # links2 = web.getSubpagesLinks()
    # pprint(links2)
    # images = web.getImages()
    # web.download("img", "fahrschule/images")
    # domains = web.getLinks(intern=False, extern=False, domain=True)
    # domains = web.getLinks(intern=False, extern=True, domain=False)
    # w3 = Page("https://699pic.com/video-sousuo-81305410-0-0-0-0-0-1-all-new-0-0-0-0-0-0.html")
    # w3.download("video", "w3/videos")
    # video_links = w3.getVideos()
    # pprint(video_links)

    # calendar_links = Page("https://tikocash.com").get("php")
    # Page("http://mathcourses.ch/mat182.html").download("pdf", "mathcourses/pdf-files")
