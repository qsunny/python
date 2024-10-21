#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import datetime
import os
import shutil
import subprocess
import time
import zipfile

# 数据库用户名
db_user = "root"
# 数据库密码
db_password = "68"
# 备份目录
backup_dir = "/data/backup"
# tar -zcvf docker-mysql-devops.tar.gz docker-mysql-devops
# backup_prefix和backup_suffix分别为备份文件的前缀和后缀，如test_backup_2019-09-19-11则代表该文件是在2019年9月19日的11点时备份的
backup_prefix = "travel_app_new_backup"
backup_suffix = "%Y-%m-%d-%H"
# 备份数据库列表
backup_databases = [
    "travel_app_new"
]
# 容器名
container_name = "tulang-db"
# 过期小时，定期删除5个小时前的备份文件
expire_hour = 5


# 获取备份文件名
def get_backup_filename():
    t = time.strftime(backup_suffix, time.localtime())
    return "%s_%s" % (backup_prefix, t)


def get_backup_path():
    return "%s%s%s" % (backup_dir, os.sep, get_backup_filename())


# 获取过期时间戳
def get_expire_time():
    t = datetime.datetime.now() - datetime.timedelta(hours=expire_hour)
    return int(time.mktime(t.timetuple()))


def create_dir(dir_path):
    # 如果目录存在则退出
    if os.path.exists(dir_path):
        return
    os.mkdir(dir_path)


cmd_template = "mysqldump -u{db_user} -p{db_password} {database} > {file_path}"


# 备份指定数据库
def backup_database(backup_path, database):
    file_path = os.sep.join([backup_path, "%s.sql" % database])
    d = {
        "container_name": container_name,
        "db_user": db_user,
        "db_password": db_password,
        "database": database,
        "file_path": file_path,
    }
    cmd = cmd_template.format(**d)
    subprocess.call(cmd, shell=True)


def zip_dir(dir_path):
    file_path = '.'.join([dir_path, "zip"])
    if os.path.exists(file_path):
        os.remove(file_path)
    z = zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED)
    for root, directories, files in os.walk(dir_path):
        fpath = root.replace(dir_path, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in files:
            z.write(os.path.join(root, filename), fpath + filename)
    z.close()


# 备份数据库
def backup():
    backup_path = get_backup_path()
    # 确保备份目录存在
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    try:
        create_dir(backup_path)
        for database in backup_databases:
            backup_database(backup_path, database)
        zip_dir(backup_path)
    finally:
        shutil.rmtree(backup_path)


# 清理过期备份文件
def clean():
    expire_time = get_expire_time()
    for root, directories, files in os.walk(backup_dir):
        for file in files:
            if not file.startswith(backup_prefix):
                continue
            if not file.endswith(".zip"):
                continue
            file_path = os.sep.join([root, file])
            t = os.path.getctime(file_path)
            if t < expire_time:
                os.remove(file_path)


