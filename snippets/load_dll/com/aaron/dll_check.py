"""检查dll是否加载成功"""
__author__ = "aaron.qiu"


import ctypes


def check_dll_loading():
    """测试系统DLL加载能力"""

    # 测试一些基础系统DLL
    test_dlls = [
        "kernel32.dll",  # 应该总是存在
        "user32.dll",  # GUI相关
        "msvcrt.dll",  # C运行时库
        "advapi32.dll",  # 安全和服务
    ]

    print("测试系统DLL加载:")
    for dll in test_dlls:
        try:
            ctypes.WinDLL(dll)
            print(f"  ✓ {dll}")
        except Exception as e:
            print(f"  ✗ {dll}: {e}")


if __name__ == "__main__":
    # 测试是否能加载DLL
    check_dll_loading()