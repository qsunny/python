# -*- encoding=utf-8 -*-
import os
import time
import subprocess
import datetime
import pprint


def check_cert_info(cert_path):
    # 获取证书信息
    # cert_info = subprocess.check_output(["openssl", "s_client", "-connect", f"{domain}:{port}"], stderr=subprocess.DEVNULL)
    # cert_path = "/data/workspace-py/out/*.yunlang.net.cn/fullchain.cer"
    cert_dates = subprocess.check_output(["openssl", "x509", "-in", cert_path, "-noout", "-dates"])

    # 解析证书有效期
    cert_dates = cert_dates.decode("utf-8").splitlines()
    start_date = datetime.datetime.strptime(cert_dates[0].split("=")[1], '%b %d %H:%M:%S %Y %Z')
    end_date = datetime.datetime.strptime(cert_dates[1].split("=")[1], '%b %d %H:%M:%S %Y %Z')

    # 检查证书是否过期
    days_until_expiry = (end_date - datetime.datetime.now()).days
    print("失效天数{}".format(days_until_expiry))
    if days_until_expiry < 30:  # 如果剩余天数少于30天，则更新证书
        pprint("小于30天")
        return True
        # subprocess.run(["certbot", "renew"])
    else:
        return False


def get_file_time(filename):
    filename = os.path.abspath(filename)
    # create_time = os.path.getctime(filename)  # 创建时间
    # print('old create time:{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(create_time))))
    update_time = os.path.getmtime(filename)  # 修改时间
    update_time_str = time.strftime("%Y-%m-%d", time.localtime(update_time));
    print('old update time:{}'.format(update_time_str))
    # access_time = os.path.getatime(filename)  # 访问时间
    # print('old access time:{}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(access_time))))
    # return create_time, update_time, access_time
    return update_time_str


def renew_cert(ali_key="", ali_secret=""):
    env_dic = {"Ali_Key": ali_key, "Ali_Secret": ali_secret}
    renew_result = subprocess.check_output(["/home/aaron/.acme.sh/acme.sh", "--renew", "--dns", "dns_ali", "-d", "yunlang.net.cn", "-d", "*.yunlang.net.cn", "--force",
                                            "--log", "/home/aaron/.acme.sh/acme.sh.log", "--accountconf", "/home/aaron/.acme.sh/account.conf"],
                                           env=env_dic, errors="ddd")

    # renew_result = subprocess.check_output(["/home/aaron/.acme.sh/acme.sh", "--version"],
    #                                        env={"Ali_Key": ali_key, "Ali_Secret": ali_secret})
    return renew_result;


if __name__ == "__main__":

    yun_lang_cert_path = "/home/aaron/.acme.sh/yunlang.net.cn_ecc/yunlang.net.cn.cer"
    yun_lang_expiry_flag = check_cert_info(yun_lang_cert_path)
    print("云浪证书是否临期失效{}".format(yun_lang_expiry_flag))

    file_update_date = get_file_time(yun_lang_cert_path)
    print("file_update_date:{}".format(file_update_date))

    to_date = datetime.date.today()
    print("to_date:{}".format(to_date))
    cur_date = to_date.strftime("%Y-%m-%d")

    print(cur_date == file_update_date)

    if cur_date == file_update_date:
        yun_lang_ali_key = "LTAI5tLoxwSyoM6P6fxfqynw"
        yun_lang_ali_secret = "spYzggqokuudoJX84NxZYqBnGN2i0z"
        output = renew_cert(yun_lang_ali_key, yun_lang_ali_secret)
        print(output)