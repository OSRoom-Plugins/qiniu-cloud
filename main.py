# -*-coding:utf-8-*-
from qiniu import Auth

from apps.plugins.qiniu_cloud.config import ACCESS_KEY, SECRET_KEY
from apps.plugins.qiniu_cloud.upfile_cloud import qiniu_upload, qiniu_file_del, qiniu_file_rename, get_file_path

__author__ = "Allen Woo"

# 初始化

qiniu = Auth(ACCESS_KEY, SECRET_KEY)

def main(**kwargs):

    '''
    主函数
    :param kwargs:
        action: 动作
    :return:
    '''
    if kwargs.get("action") == "upload":
        data = qiniu_upload(qiniu, **kwargs)

    elif kwargs.get("action") == "delete":
        data = qiniu_file_del(qiniu, **kwargs)

    elif kwargs.get("action") == "rename":
        data = qiniu_file_rename(qiniu, **kwargs)
    elif kwargs.get("action") == "get_file_path":
        data = get_file_path(qiniu, **kwargs)
    else:
        assert False
    return data


