"""
pip install requests playwright
playwright install chromium
"""

import re
import requests
from playwright.sync_api import sync_playwright
import urllib.parse


def get_video_url(share_url: str) -> str:
    """通过分享链接解析视频真实地址"""
    # 自动跳转获取原始链接
    resp = requests.head(share_url, allow_redirects=True)
    original_url = resp.url

    # 提取视频ID（适用于网页版链接）
    # video_id_match = re.search(r"/video/(\d+)/", original_url)
    # if video_id_match:
    #     video_id = video_id_match.group(1)
    # else:
    #     raise ValueError("无法解析视频ID，请检查链接格式")

    video_id = 'toZZa2wd03w'
    # 构造视频信息API接口（需根据抖音更新调整）
    api_url = f"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={video_id}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(api_url, headers=headers)
    data = response.json()

    # 提取无水印视频地址
    video_url = data['item_list'][0]['video']['play_addr']['url_list'][0]
    video_url = video_url.replace("playwm", "play")  # 去除水印关键步骤
    return video_url


def download_video(url: str, filename: str = "video.mp4"):
    """下载视频到本地"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(f"视频已保存至 {filename}")


def main(share_url):
    # 示例：粘贴抖音分享链接（短链接需先展开）
    # share_url = input("请输入抖音分享链接：").strip()

    # 使用Playwright自动化获取真实链接（应对复杂跳转）
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(share_url)
        page.wait_for_timeout(3000)  # 等待页面加载
        current_url = page.url
        browser.close()

    # 获取并下载视频
    try:
        video_url = get_video_url(current_url)
        print("解析到的视频地址：", video_url)
        download_video(video_url, "douyin_video.mp4")
    except Exception as e:
        print("下载失败：", str(e))





if __name__ == "__main__":
    # 使用示例（需替换为实际分享链接）
    main('https://v.douyin.com/toZZa2wd03w')