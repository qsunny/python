# -*- encoding=utf-8 -*-

import oss2
import os
import subprocess
from pprint import pprint
from oss2.credentials import EnvironmentVariableCredentialsProvider
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

"ali oss测试"
'''
参考文档 https://help.aliyun.com/zh/oss/developer-reference/map-custom-domain-names-4?spm=a2c4g.11186623.0.0.aec17ee8aQe6TI
pip install oss2
pip install cryptography

ImportError: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017 
解决 pip install urllib3==1.26.15
'''


def print_region(auth=None, endpoint=None):
    # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
    service = oss2.Service(auth, endpoint)
    # 查询所有支持地域对应的Endpoint信息。
    result = service.describe_regions()

    for r in result.regions:
        # 打印所有支持地域的信息。
        print('region: {0}'.format(r.region))
        # 打印所有支持地域对应的外网访问（IPv4）Endpoint。
        print('internet_endpoint: {0}'.format(r.internet_endpoint))
        # 打印所有支持地域对应的内网访问（经典网络或VPC网络）Endpoint。
        print('internal_endpoint: {0}'.format(r.internal_endpoint))
        # 打印所有支持地域对应的传输加速域名（全地域上传下载加速）Endpoint。
        print('accelerate_endpoint: {0}'.format(r.accelerate_endpoint))

    # 以查询华东1（杭州）地域对应的Endpoint信息为例。如需查询其他地域对应的Endpoint信息，请替换为指定地域。
    result = service.describe_regions('oss-cn-shenzhen')

    for r in result.regions:
        # 打印指定地域的信息。
        print('region: {0}'.format(r.region))
        # 打印指定地域对应的外网访问（IPv4）Endpoint。
        print('internet_endpoint: {0}'.format(r.internet_endpoint))
        # 打印指定地域对应的内网访问（经典网络或VPC网络）Endpoint。
        print('internal_endpoint: {0}'.format(r.internal_endpoint))
        # 打印指定地域对应的传输加速域名（全地域上传下载加速）Endpoint。
        print('accelerate_endpoint: {0}'.format(r.accelerate_endpoint))


def read_cert_content(cert_path=None):
    try:
        with open(cert_path, 'rb') as cert_file:
            cert_pem = cert_file.read()
            cert_der = serialization.load_pem_x509_certificate(cert_pem, default_backend())
            cert_text = cert_der.pretty_print(indent=4)
            return cert_text
    except Exception as e:
        print(f"Error reading certificate: {e}")
        return None


def read_cert_content_v2(cert_path):
    try:
        result = subprocess.run(['openssl', 'x509', '-text', '-noout', '-in', cert_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return None
    except Exception as e:
        print(f"Error reading certificate: {e}")
        return None


def read_cert_as_string(cert_path=None):
    try:
        with open(cert_path, 'r') as cert_file:
            cert_content = cert_file.read()
            return cert_content
    except FileNotFoundError:
        print(f"Certificate file not found: {cert_path}")
        return None
    except Exception as e:
        print(f"Error reading certificate: {e}")
        return None


if __name__ == "__main__":
    # pprint(oss2.__version__   )
    os.environ = {"OSS_ACCESS_KEY_ID": "", "OSS_ACCESS_KEY_SECRET": ""}

    # 验证环境变量是否设置成功
    # print(os.getenv('OSS_ACCESS_KEY_ID'))

    # 使用环境变量中获取的RAM用户的访问密钥配置访问凭证。
    envProvider = EnvironmentVariableCredentialsProvider()
    # print(envProvider.access_key_id)
    auth = oss2.ProviderAuth(envProvider)

    # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
    endpoint = 'https://oss-cn-shenzhen.aliyuncs.com'

    # print_region(auth, endpoint)

    # 填写Bucket名称，并设置连接超时时间为30秒。
    bucket = oss2.Bucket(auth, endpoint, 'img-tulangkj', connect_timeout=30)

    # 填写自定义域名。
    test_domain = 'img.tulangkj.com'
    # 填写旧版证书ID。
    # previous_cert_id = '12294248-cn-hangzhou'
    # 使用示例
    certificate = read_cert_as_string('/data/ng-conf/cert/tulangkj/tulangkj_fullchain.pem')
    # 设置证书私钥。
    private_key = read_cert_as_string('/data/ng-conf/cert/tulangkj/tulangkj_privkey.pem')
    if certificate:
        print(certificate)
    if private_key:
        print(private_key)

    # cert = oss2.models.CertInfo(certificate=certificate, private_key=private_key)
    # 通过force=True设置强制覆盖旧版证书。
    # 通过delete_certificate选择是否删除证书。设置为delete_certificate=True表示删除证书，设置为delete_certificate=False表示不删除证书。
    cert = oss2.models.CertInfo(certificate=certificate, private_key=private_key, force=True, delete_certificate=False)
    input = oss2.models.PutBucketCnameRequest(test_domain, cert)
    bucket.put_bucket_cname(input)


    # list_result = bucket.list_bucket_cname()
    # for c in list_result.cname:
    #     # 打印证书ID。
    #     print(c.certificate.cert_id)
    #     # 打印证书来源。
    #     print(c.certificate.type)
    #     # 打印证书状态。
    #     print(c.certificate.status)
    #     # 打印自定义域名。
    #     print(c.domain)
    #     # 打印绑定自定义域名的时间。
    #     print(c.last_modified)
    #     # 打印域名所处状态。
    #     print(c.status)


