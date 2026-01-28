"""生成guid"""
__author__ = "aaron.qiu"

import uuid


if __name__ == "__main__":
    # 1. 生成原始UUID对象（核心）
    random_uuid = uuid.uuid4()
    print("原始UUID对象：", random_uuid)  # 输出示例：f81d4fae-7dec-11d0-a765-00a0c91e6bf6

    # 2. 转换为不同格式的字符串（适配不同场景）
    # 格式1：带连字符（默认，对应C#的ToString("D")）
    uuid_with_hyphen = str(random_uuid).upper()
    print("带连字符GUID：", uuid_with_hyphen)  # f81d4fae-7dec-11d0-a765-00a0c91e6bf6

    # 格式2：无连字符（适合存储/传输，对应C#的ToString("N")）
    uuid_without_hyphen = random_uuid.hex
    print("无连字符GUID：", uuid_without_hyphen)  # f81d4fae7dec11d0a76500a0c91e6bf6

    # 格式3：带大括号（适合可视化/注册表配置，对应C#的ToString("B")）
    uuid_with_braces = f"{{{random_uuid}}}"
    print("带大括号GUID：", uuid_with_braces)  # {f81d4fae-7dec-11d0-a765-00a0c91e6bf6}

    # 格式4：带小括号（对应C#的ToString("P")）
    uuid_with_parentheses = f"({random_uuid})"
    print("带小括号GUID：", uuid_with_parentheses)  # (f81d4fae-7dec-11d0-a765-00a0c91e6bf6)