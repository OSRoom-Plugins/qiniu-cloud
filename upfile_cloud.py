# -*-coding:utf-8-*-
import os
from flask_babel import gettext
from qiniu import put_file, etag
from apps.core.plug_in.config_process import get_plugin_config
from apps.plugins.qiniu_cloud_plugin.config import PLUGIN_NAME

__author__ = "Allen Woo"


def qiniu_upload(qiniu, **kwargs):
    """
        文件上传
        :param kwargs:
        localfile_path:要上传的本地服务器文件路径
        filename:文件名, 如果带上"/"则会创建对应的子目录,如post-img/xxxx-xxx-xxx.jpg
        prefix: 文件名前缀
        :return:
        """

    localfile_path = kwargs.get("localfile_path")
    filename = kwargs.get("filename")
    prefix = kwargs.get("prefix")

    if prefix:
        filename = "{}{}".format(prefix, filename).replace("//", "/")

    # 生成上传 Token，可以指定过期时间等
    token = qiniu.upload_token(get_plugin_config(PLUGIN_NAME, "BUCKET_NAME"),
                               filename, 3600)
    ret, info = put_file(token, filename, localfile_path)
    assert ret['key'] == filename
    assert ret['hash'] == etag(localfile_path)

    result = {"key": filename, "type": "qiniu",
              "bucket_name": get_plugin_config(PLUGIN_NAME, "BUCKET_NAME")}
    return result

def qiniu_copy(bucket, **kwargs):
    """
    文件复制
    :param kwargs:
    :return:
    """

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    new_filename = kwargs.get("filename")
    if isinstance(file_url_obj, dict) and "key" in file_url_obj:

        bucket_name = get_plugin_config(PLUGIN_NAME, "BUCKET_NAME")
        # 将文件从文件key 复制到文件key2。 可以在不同bucket复制
        ret, info = bucket.copy(file_url_obj['bucket_name'], file_url_obj["key"],
                                bucket_name, new_filename)
        if ret != {}:
            return False
        return True
    else:
        return False

def qiniu_file_del(bucket, **kwargs):

    '''
    七牛云上文件删除
    :return:
    '''

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    if isinstance(file_url_obj, dict) and "bucket_name" in file_url_obj and "key" in file_url_obj:

        # 删除bucket_name 中的文件 key
        ret, info = bucket.delete(file_url_obj["bucket_name"], file_url_obj["key"])
        if ret != {}:
            return False
        return True
    return False


def qiniu_file_rename(bucket, **kwargs):

    '''
    文件重命名
    :return:
    '''

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    new_filename = kwargs.get("new_filename")
    if isinstance(file_url_obj, dict) and "bucket_name" in file_url_obj and "key" in file_url_obj:
        ret, info = bucket.move(file_url_obj["bucket_name"], file_url_obj["key"],
                                file_url_obj["bucket_name"], new_filename)
        if ret != {}:
            return False
        return True
    else:
        return False

def get_file_url(**kwargs):

    '''
    七牛云上文件删除
    :return:
    '''

    # file_url_obj:上传文件时返回的那个result格式的字典
    file_url_obj = kwargs.get("file_url_obj")
    if isinstance(file_url_obj, dict) and "bucket_name" in file_url_obj and "key" in file_url_obj:
        domain = get_plugin_config(PLUGIN_NAME, "DOMAIN")
        if not domain:
            raise Exception(gettext("Please configure the third-party file storage domain name"))

        url = "{}/{}".format(domain, file_url_obj["key"])
        return url
    return None
