# -*-coding:utf-8-*-

__author__ = "Allen Woo"
PLUGIN_NAME = "qiniu_cloud_plugin"

CONFIG = {
    "ACCESS_KEY":{
        "info":"ACCESS KEY ID",
        "value_type":"string",
        "value":""
    },
    "SECRET_KEY":{
        "info":"SECRET KEY",
        "value_type":"password",
        "value":""
    },
    "BUCKET_NAME":{
        "info":"BUCKET 名称",
        "value_type":"string",
        "value":"osroom-test"
    },
    "LOCAL_TEMP_FOLDER":{
        "info":"本地服务器临时保存目录名, 将建立在static目录下(可以不修改此项)",
        "value_type":"string",
        "value":"upload_temp"
    },
    "DOMAIN":{
        "info":"域名(带http://或https://):访问上传的文件的域名",
        "value_type":"string",
        "value":"http://p5q2navhz.bkt.clouddn.com"
    }

}
