# -*-coding:utf-8-*-
import base64
import os
import urllib
from uuid import uuid1
from apps.configs.sys_config import STATIC_PATH
from apps.plugins.qiniu_cloud_plugin.config import LOCAL_TEMP_FOLDER

__author__ = "Allen Woo"

def fileup_base_64(file, file_format="png", file_name=None, prefix=""):

    '''
     文件以base64编码上传上传
    :param file: 文件对象
    :param file_name:
    :return:
    '''
    if file:
        imgdata = base64.b64decode(file.split(",")[-1])
        if file_name:
            filename = '{}.{}'.format(file_name, file_format)
        else:
            filename = '{}.{}'.format(uuid1(), file_format)

        # 本地服务器
        # 文件保存的绝对路径
        save_dir = os.path.join(STATIC_PATH, LOCAL_TEMP_FOLDER)
        if prefix:
            filename = "{}{}".format(prefix, filename)
        save_file_path = os.path.join(save_dir, filename)

        # 文件保存到本地服务器端
        filename_split = os.path.split(filename)
        if filename_split[0]:
            temp_dir = "{}/{}".format(save_dir, filename_split[0])
        else:
            temp_dir = save_dir
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        with open(save_file_path, 'wb') as file_w:
            file_w.write(imgdata)
        return save_file_path, filename
    else:
        return None, ""

def upload_to_local(file, filename=None, file_format_name="png", fetch_url=None, prefix=None):

    '''
    上传到本地
    :return:
    '''

    # 本地服务器
    # 文件保存的绝对路径
    save_dir = os.path.join("{}/qiniu_temp".format(STATIC_PATH))
    if filename:
        filename = '{}.{}'.format(filename, file_format_name)
    else:
        filename = '{}.{}'.format(uuid1(),file_format_name)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    if prefix:
        filename = "{}{}".format(prefix, filename)
    save_file_path = os.path.join(save_dir, filename)

    # 文件保存到本地服务器端
    if fetch_url:
        urllib.request.urlretrieve(fetch_url, save_file_path)
    elif file:
        filename_split = os.path.split(filename)
        if filename_split[0]:
            temp_dir = "{}/{}".format(save_dir, filename_split[0])
        else:
            temp_dir = save_dir
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        file.save(save_file_path)

    else:
        return None
    return save_file_path, filename


def local_file_del(path):

    '''
    删除服务器端本地图片,可以给定path删除
    :param path:
    :return:
    '''

    if path:
        # 按路径删除服务器临时文件
        file_split = os.path.splitext(path)
        if os.path.exists(path):
            os.remove(path)
        return path
    return False
