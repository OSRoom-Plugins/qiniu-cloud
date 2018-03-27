# -*-coding:utf-8-*-

__author__ = "Allen Woo"
PLUGIN_NAME = "qiniu_cloud_plugin"

CONFIG = {
    "ACCESS_KEY":{
        "info":"ACCESS KEY",
        "value_type":"string",
        "value":"<Your AK>",
        "reactivate":True
    },
    "SECRET_KEY":{
        "info":"SECRET KEY",
        "value_type":"password",
        "value":"<Your SK>",
        "reactivate":True
    },
    "BUCKET_NAME":{
        "info":"BUCKET 名称",
        "value_type":"string",
        "value":"如osroom-test",
        "reactivate":False
    },
    "DOMAIN":{
        "info":"域名(带http://或https://):访问上传的文件的域名",
        "value_type":"string",
        "value":"如http://p5q2navhz.bkt.clouddn.com",
        "reactivate":False
    }
}