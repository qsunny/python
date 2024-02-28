import subprocess
import datetime
import pprint

# 域名和端口
domain = "example.com"
port = "443"

# 获取证书信息
# cert_info = subprocess.check_output(["openssl", "s_client", "-connect", f"{domain}:{port}"], stderr=subprocess.DEVNULL)
cert_path = "/data/workspace-py/out/*.yunlang.net.cn/fullchain.cer"
cert_dates = subprocess.check_output(["openssl", "x509", "-in", cert_path, "-noout", "-dates"])

# 解析证书有效期
cert_dates = cert_dates.decode("utf-8").splitlines()
start_date = datetime.datetime.strptime(cert_dates[0].split("=")[1], '%b %d %H:%M:%S %Y %Z')
end_date = datetime.datetime.strptime(cert_dates[1].split("=")[1], '%b %d %H:%M:%S %Y %Z')

# 检查证书是否过期
days_until_expiry = (end_date - datetime.datetime.now()).days
pprint(format("失效天数%d" , days_until_expiry))
if days_until_expiry < 30:  # 如果剩余天数少于30天，则更新证书
    pprint("小于30天")
    # subprocess.run(["certbot", "renew"])
