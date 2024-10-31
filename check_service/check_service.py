# -*- encoding=utf-8 -*-
import os
import sys
import time
import subprocess
import datetime
import pprint
from subprocess import CalledProcessError, STDOUT, check_output
import requests
import json
import socket
import subprocess
import requests
from bs4 import BeautifulSoup

"检查服务器服务是否正常运行"
'''
pip3 install requests beautifulsoup4
'''

def send_feishu_msg(content=None):
    """推送飞书消息"""
    try:
        # 目标URL
        url = 'https://open.feishu.cn/open-apis/bot/v2/hook/'

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
        # print(response_data)

    except requests.exceptions.RequestException as e:
        print(f"发送飞书消息请求失败: {e}")


def check_nginx_process():
    try:
        # 检查 Nginx 进程是否存在
        result = subprocess.run(['pgrep', 'nginx'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("Nginx 进程正在运行")
            return True
        else:
            print("Nginx 进程未运行")
            return False
    except Exception as e:
        msg = f"检查 Nginx 进程时出错: {e}"
        print(msg)
        send_feishu_msg(msg)
        return False


def get_nginx_status():
    try:
        # 读取 Nginx 状态页面
        response = requests.get('http://127.0.0.1/nginx_status', auth=('username', 'password'))  # 替换为实际的用户名和密码
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        status_text = soup.get_text()

        print("Nginx 状态:")
        print(status_text)
        # send_feishu_msg(f"Nginx 状态:\n{status_text}")

        # 你可以在这里解析状态文本以提取具体的信息，例如活动连接数、接收到的请求数等
    except requests.RequestException as e:
        print(f"无法访问 Nginx 状态页面: {e}")


def check_nginx_service(source_host='127.0.0.1'):
    if check_nginx_process():
        msg = "Nginx 进程正在运行"
        print(msg)
        # send_feishu_msg(msg)
        # get_nginx_status()
    else:
        msg = f"{source_host} Nginx 未运行，无法获取状态"
        print(msg)
        send_feishu_msg(msg)


def is_docker_running():
    try:
        # 运行 'docker info' 命令
        result = subprocess.run(['docker', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        # 如果命令成功执行，说明 Docker daemon 在运行
        return True
    except Exception as e:
        # 如果命令执行失败（比如因为 Docker daemon 没有运行），则捕获异常
        msg = f"检查 docker daemon 进程时出错: {e}"
        print(msg)
        send_feishu_msg(msg)
        return False


def check_docker_service(source_host='127.0.0.1'):
    if is_docker_running():
        msg = "Docker daemon 进程正在运行."
        print(msg)
        # send_feishu_msg(msg)
    else:
        msg = f"{source_host} Docker daemon 进程未运行."
        print(msg)
        send_feishu_msg(msg)


def check_port(host, port, timeout=1):
    """
    检查指定主机和端口是否开放。

    :param host: 主机名或IP地址
    :param port: 端口号
    :param timeout: 连接超时时间（秒）
    :return: 如果端口开放则返回True，否则返回False
    """
    try:
        socket.create_connection((host, port), timeout)
        return True
    except Exception as e:
        print(f"检查服务端口出错: {e}")
        return False


def check_port_service(source_host='127.0.0.1', host='127.0.0.1', port=80, port_service_name='端口对应服务的名称'):
    """
    host = '127.0.0.1'  # 替换为你要检查的主机
    port = 8080  # 替换为你要检查的端口号

    """
    if check_port(host, port):
        msg = f"{port_service_name} Service Port {port} on {source_host} is open."
        print(msg)
        # send_feishu_msg(msg)
    else:
        msg = f"{port_service_name} Service Port {port} on {source_host} is closed or unreachable."
        print(msg)
        send_feishu_msg(msg)


if __name__ == "__main__":
    """
    30 0 * * * nohup python3 /data/workspace/shell/python/check_service.py 2>&1 1>>/data/logs/python/py.log &
    */10 * * * * nohup python3 /data/workspace/shell/python/check_service.py 2>&1 1>>/data/logs/python/py.log &

    """

    # 旅游
    check_nginx_service('47.106.')
    check_docker_service('47.106.')
    check_port_service('47.106', '127.0.0.1', 3306, 'Mysql')
    check_port_service('47.106', '127.0.0.1', 7379, 'Redis')




