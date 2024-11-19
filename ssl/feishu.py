import requests
import json


def send_feishu_msg(content=None, at_all=True):
    try:
        # 目标URL
        url = 'https://open.feishu.cn/open-apis/bot/v2/hook/35xxxx'

        if at_all:
            content = f'<at user_id="all">所有人</at>{content}'
        # 要发送的JSON数据
        json_data = {
            'msg_type': 'text',
            'content': {'text': content}
        }

        # 头信息
        headers = {
            'Content-Type': 'application/json'
        }

        # 发送POST请求，并指定数据为JSON格式以及头信息
        response = requests.post(url, json=json_data, headers=headers)

        # 检查响应状态码
        response.raise_for_status()  # 如果响应状态码不是200，会抛出HTTPError异常

        # 解析响应内容（假设服务器返回的是JSON格式）
        response_data = response.json()
        print(response_data)

    except requests.exceptions.RequestException as e:
        print(f"发送飞书消息请求失败: {e}")


if __name__ == "__main__":
    """
    https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot?lang=zh-CN
    curl -X POST -H "Content-Type: application/json" -d "{\"msg_type\":\"text\",\"content\":{\"text\":\"<at user_id=\"all\">所有人</at> request example\"}}" https://open.feishu.cn/open-apis/bot/v2/hook/35xxxxx
    """
    send_feishu_msg("request example")