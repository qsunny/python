import browser_cookie3


def get_chrome_cookies():
    try:
        # 获取所有Chrome cookies
        cookies = browser_cookie3.chrome()

        # 获取特定域名的cookies
        youtube_cookies = browser_cookie3.chrome(domain_name='youtube.com')

        # 转换为requests可用的字典格式
        cookies_dict = {}
        for cookie in youtube_cookies:
            cookies_dict[cookie.name] = cookie.value

        return cookies_dict
    except Exception as e:
        print(f"获取Cookies失败: {e}")
        return {}


# 使用示例
cookies = get_chrome_cookies()
print(f"YouTube Cookies: {cookies}")