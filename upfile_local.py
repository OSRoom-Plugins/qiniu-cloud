# -*-coding:utf-8-*-
import base64
import os
import urllib
from uuid import uuid1
from apps.configs.sys_config import STATIC_PATH
from apps.core.plug_in.config_process import get_plugin_config
from apps.plugins.qiniu_cloud_plugin.config import PLUGIN_NAME

__author__ = "Allen Woo"

def fileup_base_64(file, file_format="png", file_name=None, prefix=""):

    '''
     文件以base64编码上传上传
    :param file: 文件对象
    :param file_name:
    :return: 绝对路径，key(相对路径)
    '''
    if file:

        imgdata = base64.b64decode(file.split(",")[-1])
        if file_name:
            filename = '{}.{}'.format(file_name, file_format)
        else:
            filename = '{}.{}'.format(uuid1(), file_format)

        # 本地服务器
        if prefix:
            filename = "{}{}".format(prefix, filename)

        # 文件保存的绝对路径
        save_file_path = "{}/{}/{}".format(STATIC_PATH,
                                           get_plugin_config(PLUGIN_NAME, "LOCAL_TEMP_FOLDER"),
                                           filename).replace("//", "/")

        # 文件保存到本地服务器端
        save_dir = os.path.split(save_file_path)[0]
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        with open(save_file_path, 'wb') as file_w:
            file_w.write(imgdata)

        return save_file_path, filename
    else:
        return False, ""

def upload_to_local(file, filename=None, file_format="png", fetch_url=None, prefix=None):

    '''
    上传到本地
    :return:
    '''

    # 本地服务器
    # 文件保存的绝对路径
    save_dir = os.path.join("{}/qiniu_temp".format(STATIC_PATH))
    if filename:
        filename = '{}.{}'.format(filename, file_format)
    else:
        filename = '{}.{}'.format(uuid1(),file_format)

    # 本地服务器
    if prefix:
        filename = "{}{}".format(prefix, filename)

    # 文件保存的绝对路径
    save_file_path = "{}/{}/{}".format(STATIC_PATH,
                                       get_plugin_config(PLUGIN_NAME, "LOCAL_TEMP_FOLDER"),
                                       filename).replace("//", "/")

    # 文件保存到本地服务器端
    save_dir = os.path.split(save_file_path)[0]
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 文件保存到本地服务器端
    if fetch_url:
        urllib.request.urlretrieve(fetch_url, save_file_path)
    elif file:
        file.save(save_file_path)
    else:
        return None, ""
    return save_file_path, filename


def local_file_del(path):

    '''
    删除服务器端本地图片,可以给定path删除
    :param path:
    :return:
    '''

    if path:
        # 按路径删除服务器临时文件
        if os.path.exists(path):
            os.remove(path)
        else:
            return False
        return True
    return False
