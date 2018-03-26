# -*-coding:utf-8-*-
from qiniu import Auth, BucketManager
from apps.core.plug_in.config_process import get_plugin_config, import_plugin_config
from apps.plugins.qiniu_cloud_plugin.config import PLUGIN_NAME, CONFIG
from apps.plugins.qiniu_cloud_plugin.upfile_cloud import qiniu_upload, qiniu_file_del, qiniu_file_rename, get_file_path, \
    qiniu_save_file

__author__ = "Allen Woo"

# 初始化
import_plugin_config(PLUGIN_NAME, CONFIG)
qiniu = Auth(get_plugin_config(PLUGIN_NAME, "ACCESS_KEY"),
                 get_plugin_config(PLUGIN_NAME, "SECRET_KEY"))

def main(**kwargs):

    '''
    主函数
    :param kwargs:
        action: 动作
    :return:
    '''
    bucket = BucketManager(qiniu)

    if kwargs.get("action") == "upload":
        data = qiniu_upload(qiniu, **kwargs)
    elif kwargs.get("action") == "save_file":
        data = qiniu_save_file(qiniu, **kwargs)
    elif kwargs.get("action") == "delete":
        data = qiniu_file_del(bucket, **kwargs)

    elif kwargs.get("action") == "rename":
        data = qiniu_file_rename(bucket, **kwargs)
    elif kwargs.get("action") == "get_file_url":
        data = get_file_path(**kwargs)
    else:
        assert False
    return data


