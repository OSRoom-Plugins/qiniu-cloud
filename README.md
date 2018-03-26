## OSROOM开源系统的七牛云存储插件
### 注意:
- 1.使用前请配置好config.py, 再压缩上传安装(或直接放入osroom项目的apps/plugins目录下)

- 2.安装前请保证插件主目录名称为:qiniu_cloud_plugin, 而不是qiniu_cloud_plugin-master之类的

- 3.此插件需要安装qiniu的python包, 注意安装在osroom系统运行的python环境下. pip安装方法如下
 ```
    pip install qiniu
 ```
更多安装方法见:https://developer.qiniu.com/kodo/sdk/1242/python
### 配置:

```
    ACCESS_KEY = "你的AK"
    SECRET_KEY = "你的SK"
    LOCAL_TEMP_FOLDER = "upload_temp" # 临时保存目录
    BUCKET_NAME = "<你的空间名>"
```

### 类似插件还有

阿里云OSS对象存储插件:https://github.com/osroom-plugins/aliyun_oss_plugin
