#__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import os
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

#七牛云配置
#需要填写你的 Access Key 和 Secret Key
access_key = 'GLCCcNfZiqOx4pjL6SDZGRfDu-QMX6cYMB9Yupku'
secret_key = 'TOPsxBISmd091aVza3WNdiJwTPRtgHY_k8aWBOdj'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'officer'


# 图片上传七牛云，向数据库插入图片地址
def upload_qiniu(image_tag):
    # 上传到七牛后保存的文件名
    key = '%s.jps' % image_tag
    #生成上传Token,可以指定过期时间等
    token = q.upload_token(bucket_name,key,3600)
    #要上传的本地文件路径
    localPhoto = 'photos/%s.jpg' % image_tag
    ret,info = put_file(token,key,localPhoto)

    image_url = 'http://ozwyjb3op.bkt.clouddn.com/%s.jps' % image_tag

if __name__ == "__main__":
	upload_qiniu("430000_0780")

