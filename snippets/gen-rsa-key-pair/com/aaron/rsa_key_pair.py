from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_rsa_key_pair(
    key_size: int = 2048,  # 密钥长度，2048位足够安全，4096位更安全但速度慢
    private_key_path: str = "rsa_private_key.pem",  # 私钥保存路径
    public_key_path: str = "rsa_public_key.pem"     # 公钥保存路径
):
    """
    生成RSA公私钥对，并保存为PEM格式文件
    :param key_size: 密钥长度（2048/4096）
    :param private_key_path: 私钥保存路径
    :param public_key_path: 公钥保存路径
    :return: 私钥对象、公钥对象
    """
    try:
        # 1. 生成私钥（包含所有参数：p、q、d、e、n等）
        private_key = rsa.generate_private_key(
            public_exponent=65537,  # 固定65537，是行业标准的公钥指数，安全且高效
            key_size=key_size,
            backend=default_backend()
        )

        # 2. 序列化私钥为PEM格式（加密版，需设置密码；若无需加密，可改用no_encryption()）
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,  # PKCS8是通用的私钥格式
            encryption_algorithm=serialization.BestAvailableEncryption(b"your_password_here")  # 替换为你的密码
            # 若无需加密私钥，替换上面一行：encryption_algorithm=serialization.NoEncryption()
        )

        # 3. 获取公钥并序列化为PEM格式
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # 4. 保存公私钥到文件
        with open(private_key_path, "wb") as f:
            f.write(private_pem)
        with open(public_key_path, "wb") as f:
            f.write(public_pem)

        print(f"✅ 私钥已保存至：{private_key_path}")
        print(f"✅ 公钥已保存至：{public_key_path}")
        return private_key, public_key

    except Exception as e:
        print(f"❌ 生成密钥失败：{str(e)}")
        raise

# 调用函数生成密钥
if __name__ == "__main__":
    # 生成2048位密钥（推荐），如需更安全可改为4096
    private_key, public_key = generate_rsa_key_pair(key_size=2048)

    # 可选：打印公钥的数值形式（e和n），便于理解RSA核心参数
    public_numbers = public_key.public_numbers()
    print("\n📌 公钥核心参数：")
    print(f"公钥指数e: {public_numbers.e}")
    print(f"模数n（部分）: {str(public_numbers.n)[:50]}...")