# -*-coding:utf-8-*-
from flask_babel import gettext
from qiniu import put_file, etag
from apps.core.plug_in.config_process import get_plugin_config
from apps.plugins.qiniu_cloud_plugin.config import PLUGIN_NAME
from apps.plugins.qiniu_cloud_plugin.upfile_local import upload_to_local, local_file_del

__author__ = "Allen Woo"


def qiniu_upload(qiniu, **kwargs):

    """
    文件上传
    :param kwargs:

    file:上传：获取文件对象
    fetch_url:远程文件url
    file_name:文件名, 如果带上"/"则会创建对应的子目录,如post-img/xxxx-xxx-xxx.jpg
    file_format_name: jpg, png,txt, json....
    prefix: 文件名前缀
    is_base_64: 上传的时转码成base64的格式文件

    :return:
    """

    file = kwargs.get("file")
    fetch_url = kwargs.get("fetch_url")
    filename = kwargs.get("file_name")
    file_format_name = kwargs.get("file_format_name")
    prefix = kwargs.get("prefix")
    is_base_64 = kwargs.get("is_base_64")

    if is_base_64:
        # localfilepath要上传文件的本地路径, key上传到七牛后保存的文件名
        localfile_path, key = upload_to_local(file=file, filename=filename,
                                              file_format=file_format_name,
                                              fetch_url=fetch_url, prefix=prefix)
    else:
        # localfilepath要上传文件的本地路径, key上传到七牛后保存的文件名
        localfile_path, key = upload_to_local(file=file, filename=filename,
                                              file_format=file_format_name,
                                              fetch_url=fetch_url, prefix=prefix)

    # 生成上传 Token，可以指定过期时间等
    token = qiniu.upload_token(get_plugin_config(PLUGIN_NAME, "BUCKET_NAME"),
                               key, 3600)
    ret, info = put_file(token, key, localfile_path)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile_path)

    # 删除本地临时文件
    local_file_del(localfile_path)

    result = {"key": key, "type": "qini",
              "bucket_name": get_plugin_config(PLUGIN_NAME, "BUCKET_NAME")}
    return result

def qiniu_save_file(qiniu, **kwargs):
    """
    本地文件上传保存
    :param kwargs:

    localfile_path:要保存的本地文件路径
    file_name:文件名, 如果带上"/"则会创建对应的子目录,如post-img/xxxx-xxx-xxx.jpg

    :return:
    """


    filename = kwargs.get("file_name")
    localfile_path = kwargs.get("localfile_path")

    # 生成上传 Token，可以指定过期时间等
    token = qiniu.upload_token(get_plugin_config(PLUGIN_NAME, "BUCKET_NAME"),
                               filename, 3600)
    ret, info = put_file(token, filename, localfile_path)
    assert ret['key'] == filename
    assert ret['hash'] == etag(localfile_path)

    # 删除本地临时文件
    local_file_del(localfile_path)

    result = {"key": filename, "type": "qini",
              "bucket_name": get_plugin_config(PLUGIN_NAME, "BUCKET_NAME")}
    return result



def qiniu_file_del(bucket, **kwargs):

    '''
    七牛云上文件删除
    :return:
    '''

    # path_obj:上传文件时返回的那个result格式的字典
    path_obj = kwargs.get("path_obj")
    if isinstance(path_obj, dict) and "bucket_name" in path_obj and "key" in path_obj:

        # 删除bucket_name 中的文件 key
        ret, info = bucket.delete(path_obj["bucket_name"], path_obj["key"])
        try:
            assert ret == {}
        except:
            return False
        return True
    return False


def qiniu_file_rename(bucket, **kwargs):

    '''
    文件重命名
    :return:
    '''

    # path_obj:上传文件时返回的那个result格式的字典
    path_obj = kwargs.get("path_obj")
    new_filename = kwargs.get("new_filename")
    if isinstance(path_obj, dict) and "bucket_name" in path_obj and "key" in path_obj:
        ret, info = bucket.move(path_obj["bucket_var"], path_obj["key"],
                                path_obj["bucket_var"], new_filename)
        try:
            assert ret == {}
        except:
            return False
        return True
    else:
        return False

def get_file_url(**kwargs):

    '''
    七牛云上文件删除
    :return:
    '''

    # path_obj:上传文件时返回的那个result格式的字典
    path_obj = kwargs.get("path_obj")
    if isinstance(path_obj, dict) and "bucket_name" in path_obj and "key" in path_obj:
        domain = get_plugin_config(PLUGIN_NAME, "DOMAIN")
        if not domain:
            raise Exception(gettext("Please configure the third-party file storage domain name"))

        url = "{}/{}".format(domain, path_obj["key"])
        return url
    return None
