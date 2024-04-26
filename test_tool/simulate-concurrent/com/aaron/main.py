import concurrent.futures
import time
import random
import requests

import concurrent.futures
import time
import requests

# 定义要发送的 POST 数据
post_data = {
    "areaId": "440305",
    "areaName": "南山区",
    "cityId": "440300",
    "cityName": "深圳市",
    "detailAddress": "深圳湾一号",
    "mobile": "18897524035",
    "provinceId": "440000",
    "provinceName": "广东省",
    "receiver": "杨初南",
    "orderNumber": "A101211020240426767811"
}

# 定义请求头
headers = {
    'Content-Type': 'application/json',  # 设置内容类型为 JSON
    'token': '550:4:eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1NTAiLCJpYXQiOjE3MTM5MzkwNDF9.M-pJHr4KcOZnp1BxP1qasYBXYuPckuOJR9mIIyWystY'
}

# 定义目标 URL
target_url = 'https://api.yunlang.net.cn/fruit-gift-app/retail-order/receive-gifts'


# 模拟发送POST请求的函数
def send_post_request(url, data, headers):
    start_time = time.time()
    response = requests.post(url, json=data, headers=headers)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return response.status_code, elapsed_time, response.text


# 模拟并发POST请求的主函数
def simulate_concurrent_post_requests(url, data, headers, num_requests, max_workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(send_post_request, url, data, headers) for _ in range(num_requests)]

        results = []
        for future in concurrent.futures.as_completed(futures):
            status_code, elapsed_time, response_text = future.result()
            results.append((status_code, elapsed_time, response_text))

            # 处理结果，例如打印或保存到文件等
    for status_code, elapsed_time, response_text in results:
        print(f"Status Code: {status_code}, Elapsed Time: {elapsed_time:.2f}s, Response: {response_text[:100]}...")

        # 计算成功率和其他统计信息（如果需要）
    success_count = sum(1 for status_code, _, _ in results if status_code == 200)
    success_rate = (success_count / num_requests) * 100
    average_time = sum(elapsed_time for _, elapsed_time, _ in results) / num_requests
    print(f"Success Rate: {success_rate:.2f}%")
    print(f"Average Response Time: {average_time:.2f}s")


# 使用示例
if __name__ == "__main__":
    num_requests = 10  # 模拟的请求数量
    max_workers = 5  # 最大并发数
    simulate_concurrent_post_requests(target_url, post_data, headers, num_requests, max_workers)
