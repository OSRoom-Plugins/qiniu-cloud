# Osroom系统的七牛云存储插件
# 注意:
1.使用前请配置好config.py, 再压缩上传安装(或直接放入osroom项目的apps/plugins目录下)
2.安装前请保证插件主目录名称为:qiniu_cloud_plugin, 而不是qiniu_cloud_plugin-master之类的

# 配置:

```
    ACCESS_KEY = "你的AK"
    SECRET_KEY = "你的SK"
    LOCAL_TEMP_FOLDER = "qiniu_temp" # 临时保存目录
    BUCKET_NAME = "<你的空间名>"
```

