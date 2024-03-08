# -*- encoding=utf-8 -*-
import os
import sys
import time
import subprocess
import datetime
import pprint
import paramiko
from scp import SCPClient
from subprocess import CalledProcessError, STDOUT, check_output

"检查ssl证书是否过期，重新生成证书"
'''
pip install paramiko
pip install scp
'''


def check_cert_info(domain=None, cert_path=None):
    # 获取证书信息
    # cert_info = subprocess.check_output(["openssl", "s_client", "-connect", f"{domain}:{port}"], stderr=subprocess.DEVNULL)
    # cert_path = "/data/workspace-py/out/*.yunlang.net.cn/fullchain.cer"
    cert_dates = check_output(["openssl", "x509", "-in", cert_path, "-noout", "-dates"])

    # 解析证书有效期
    cert_dates = cert_dates.decode("utf-8").splitlines()
    start_date = datetime.datetime.strptime(cert_dates[0].split("=")[1], '%b %d %H:%M:%S %Y %Z')
    end_date = datetime.datetime.strptime(cert_dates[1].split("=")[1], '%b %d %H:%M:%S %Y %Z')

    # 检查证书是否过期
    days_until_expiry = (end_date - datetime.datetime.now()).days
    print("{} 证书将在{}天后过期".format(domain, days_until_expiry))
    if days_until_expiry < 5:  # 如果剩余天数少于5天，则更新证书
        pprint("小于5天")
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


def renew_cert(ali_key=None, ali_secret=None, acme_home=None, domain=None):
    """续签证书"""
    '''
    acme.sh --renew --dns dns_ali -d yunlang.net.cn -d *.yunlang.net.cn --force
    '''
    print("===========续签证书{}=============".format(domain))
    env_dic = {"Ali_Key": ali_key, "Ali_Secret": ali_secret}
    try:
        renew_result = subprocess.check_output(
            ["{}/acme.sh".format(acme_home), "--renew", "--dns", "dns_ali", "-d",
             domain, "--force",
             "--home", acme_home, "--config-home", acme_home,
             "--log", "{}/acme.sh.log".format(acme_home), "--accountconf", "{}/account.conf".format(acme_home)],
            env=env_dic, stderr=STDOUT, cwd=acme_home, universal_newlines=True)

        # renew_result = subprocess.check_output(["/home/aaron/.acme.sh/acme.sh", "--version"],
        #                                        env={"Ali_Key": ali_key, "Ali_Secret": ali_secret})
        print("renew result:{}".format(renew_result))
        return 0
    except CalledProcessError as e:
        sys.stderr.write(e.output)
        sys.stderr.flush()
        return e.returncode
    else:
        return 0


def install_cert(domain=None, acme_home=None, key_file=None, fullchain=None):
    """证书合成"""
    '''
    acme.sh --install-cert -d yunlang.net.cn --key-file /data/cert/yunlang_privkey.pem --fullchain-file /data/cert/yunlang_fullchain.pem
    '''

    print("===========证书合成{}=============".format(domain))
    try:
        result = subprocess.check_output(
            ["{}/acme.sh".format(acme_home), "--install-cert", "-d", domain, "--key-file", key_file, "--fullchain-file",
             fullchain],
            stderr=STDOUT, cwd=acme_home, universal_newlines=True)
        print("install result:{}".format(result))
        return 0
    except CalledProcessError as e:
        sys.stderr.write(e.output)
        sys.stderr.flush()
        return e.returncode
    else:
        return 0


def sync_file(source_file=None, dest_path=None, dest_host=None, account=None, passwd=None):
    """同步证书到远程服务器"""
    print("同步证书到远程服务器,source_file={},dest_path={},dest_host={}".format(source_file, dest_path, dest_host))
    try:
        # 连接到远程服务器
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(dest_host, username=account, password=passwd)

        # 创建SCP客户端
        scp = SCPClient(ssh.get_transport())

        # 上传文件到远程服务器
        scp.put(source_file, dest_path)

        # 下载文件到本地
        # scp.get('remote_file.txt', 'local_file.txt')

        # 关闭连接
        scp.close()
        ssh.close()

    except Exception as e:
        sys.stderr.write(e)
        sys.stderr.flush()
        return 1
    else:
        return 0


def remote_exec_command(exec_command=None, dest_host=None, account=None, passwd=None):
    """远程服务器执行对应的命令"""
    try:
        print("远程服务器{},执行对应的命令{}".format(dest_host, exec_command))
        # 创建SSH客户端
        ssh = paramiko.SSHClient()

        # 自动添加主机密钥
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接到远程服务器
        ssh.connect(dest_host, port=22, username=account, password=passwd)

        # 执行远程命令
        stdin, stdout, stderr = ssh.exec_command(exec_command)

        # 读取命令输出
        output = stdout.read().decode("utf-8")
        errors = stderr.read().decode("utf-8")
        if output:
            print("Command output:", output)
        if errors:
            print("Errors:", errors)
        # 关闭连接
        ssh.close()

    except Exception as e:
        sys.stderr.write(e)
        sys.stderr.flush()
        return 1
    else:
        return 0


def restart_nginx_service():
    """重启nginx服务"""
    print("===重启本地nginx服务===")
    # 使用Popen创建进程，并与进程进行复杂的交互
    proc = subprocess.Popen(
        # "docker exec nginx sh -c 'nginx -t'",  # cmd特定的查询空间的命令
        "docker exec nginx sh -c 'nginx -s reload'",  # cmd特定的查询空间的命令
        stdin=None,  # 标准输入 键盘
        stdout=subprocess.PIPE,  # -1 标准输出（演示器、终端) 保存到管道中以便进行操作
        stderr=subprocess.PIPE,  # 标准错误，保存到管道
        shell=True)
    outinfo, errinfo = proc.communicate()  # 获取输出和错误信息
    print(outinfo.decode('utf-8'))  # 外部程序 (windows系统)决定编码格式
    print(errinfo.decode('utf-8'))


def generate_cert(domain=None, star_flag=None, acme_home=None, cert_key_path=None, cert_path=None, ali_key=None, ali_secret=None):
    """判断证书是否在指定天数临期失效、重新生成证书"""
    expiry_flag = check_cert_info(domain, cert_path)
    print("{}证书是否临期失效{}".format(domain, expiry_flag))
    if expiry_flag:
        if star_flag:
            domain = "*.{}".format(domain)
        output = renew_cert(ali_key, ali_secret, acme_home, domain)
        print(output)
        if output == 0:
            install_output = install_cert(domain, acme_home, cert_key_path, cert_path)
            return install_output
    return 1


def copy_cert_restart_service(cert_key_path=None, cert_path=None, dest_file=None, dest_host=None, account=None, passwd=None):
    """复制证书到远程服务器、并重启nginx服务"""
    print("===复制证书到远程服务器、并重启nginx服务===")
    file_update_date = get_file_time(cert_path)
    print("file_update_date:{}".format(file_update_date))

    to_date = datetime.date.today()
    print("to_date:{}".format(to_date))
    cur_date = to_date.strftime("%Y-%m-%d")

    print(cur_date == file_update_date)

    if cur_date == file_update_date:
        print("===同步更新证书===")

        output = sync_file(cert_key_path, dest_file, dest_host, account, passwd)
        output2 = sync_file(cert_path, dest_file, dest_host, account, passwd)
        print(output)
        print(output2)
        remote_exec_command("/usr/local/nginx/sbin/nginx -s reload", dest_host, account, passwd)


if __name__ == "__main__":
    domain = "yunlang.net.cn"
    # acme_home = "/home/aaron/.acme.sh"
    # yun_lang_cert_key_path = "/data/cert/yunlang_privkey.pem"
    # yun_lang_cert_path = "/data/cert/yunlang_fullchain.pem"
    acme_home = "/root/.acme.sh"
    yun_lang_cert_key_path = "/data/ng-conf/cert/yunlang/yunlang_privkey.pem"
    yun_lang_cert_path = "/data/ng-conf/cert/yunlang/yunlang_fullchain.pem"
    dest_file = "/usr/local/nginx/conf/cert/yunlang"
    yun_lang_ali_key = ""
    yun_lang_ali_secret = ""

    generate_result = generate_cert(domain, True, acme_home, yun_lang_cert_key_path, yun_lang_cert_path, yun_lang_ali_key, yun_lang_ali_secret)
    if generate_result == 0:
        restart_nginx_service()
        copy_cert_restart_service(yun_lang_cert_key_path, yun_lang_cert_path, dest_file, "120", "root", "")


    domain = "rongzhoufu.com"
    rongzhoufu_cert_key_path = "/data/ng-conf/cert/rongzhoufu/rongzhoufu_privkey.pem"
    rongzhoufu_cert_path = "/data/ng-conf/cert/rongzhoufu/rongzhoufu_fullchain.pem"
    dest_file = "/usr/local/nginx/conf/cert/rongzhoufu"
    rongzhoufu_ali_key = ""
    rongzhoufu_ali_secret = ""

    generate_result = generate_cert(domain, True, acme_home, rongzhoufu_cert_key_path, rongzhoufu_cert_path, rongzhoufu_ali_key, rongzhoufu_ali_secret)
    if generate_result == 0:
        copy_cert_restart_service(rongzhoufu_cert_key_path, rongzhoufu_cert_path, dest_file, "", "root", "")
        copy_cert_restart_service(rongzhoufu_cert_key_path, rongzhoufu_cert_path,
                              "/usr/local/nginx/conf/conf.d/cert/rongzhoufu", "", "root", "")


    domain = "tulangkj.com"
    tulangkj_cert_key_path = "/data/ng-conf/cert/tulangkj/tulangkj_privkey.pem"
    tulangkj_cert_path = "/data/ng-conf/cert/tulangkj/tulangkj_fullchain.pem"
    dest_file = "/usr/local/nginx/conf/cert/tulangkj"
    tulangkj_ali_key = ""
    tulangkj_ali_secret = ""

    generate_result = generate_cert(domain, True, acme_home, tulangkj_cert_key_path, tulangkj_cert_path, tulangkj_ali_key, tulangkj_ali_secret)
    if generate_result == 0:
        restart_nginx_service()
        copy_cert_restart_service(tulangkj_cert_key_path, tulangkj_cert_path, dest_file, "", "root", "")
        copy_cert_restart_service(tulangkj_cert_key_path, tulangkj_cert_path, "/usr/local/nginx/conf/conf.d/cert/tulangkj", "", "root", "")


    domain = "moyuinfo.com"
    moyuinfo_cert_key_path = "/data/ng-conf/cert/moyuinfo/moyuinfo_privkey.pem"
    moyuinfo_cert_path = "/data/ng-conf/cert/moyuinfo/moyuinfo_fullchain.pem"
    dest_file = "/usr/local/nginx/conf/cert/moyuinfo"
    moyuinfo_ali_key = ""
    moyuinfo_ali_secret = ""

    generate_result = generate_cert(domain, True, acme_home, moyuinfo_cert_key_path, moyuinfo_cert_path, moyuinfo_ali_key, moyuinfo_ali_secret)
    if generate_result == 0:
        copy_cert_restart_service(moyuinfo_cert_key_path, moyuinfo_cert_path, dest_file, "", "root", "")

    domain = "mingliuinfo.com"
    mingliuinfo_cert_key_path = "/data/ng-conf/cert/mingliuinfo/mingliuinfo_privkey.pem"
    mingliuinfo_cert_path = "/data/ng-conf/cert/mingliuinfo/mingliuinfo_fullchain.pem"
    dest_file = "/usr/local/nginx/conf/cert/mingliuinfo"
    mingliuinfo_ali_key = ""
    mingliuinfo_ali_secret = ""

    generate_result = generate_cert(domain, True, acme_home, mingliuinfo_cert_key_path, mingliuinfo_cert_path, mingliuinfo_ali_key, mingliuinfo_ali_secret)
    if generate_result == 0:
        restart_nginx_service()
        # 铭流官网
        copy_cert_restart_service(mingliuinfo_cert_key_path, mingliuinfo_cert_path, dest_file, "", "root", "")
        # mall.mingliuinfo.com
        copy_cert_restart_service(mingliuinfo_cert_key_path, mingliuinfo_cert_path, dest_file, "", "root", "")
