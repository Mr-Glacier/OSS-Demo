import time
import os
import oss2

# 以下代码展示了Bucket相关操作，诸如创建、删除、列举Bucket等。

# 首先初始化AccessKeyId、AccessKeySecret、Endpoint等信息。
access_key_id = "======"
access_key_secret = "====="

bucket_name = "zedata-bucket"
endpoint = "oss-cn-hongkong.aliyuncs.com"

if __name__ == '__main__':

    auth = oss2.Auth(access_key_id, access_key_secret)
    service = oss2.Service(auth, endpoint)

    # 1.遍历地域下所有的 bucket
    for b in oss2.BucketIterator(service):
        print(b.name)

    # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

    # 2.简单的上传文件
    # bucket.put_object('motto.txt', 'Never give up. - Jack Ma')

    # 3.判断文件是否存在于存储空间中
    exist = bucket.object_exists('motto.txt')
    if exist:
        print('motto.txt exists')
    else:
        print('motto.txt not exists')

    # 4.获取文件数据的信息
    # 获取Object的metadata
    object_meta = bucket.get_object_meta('motto.txt')
    print('last modified: ' + str(object_meta.last_modified))
    print('etag: ' + object_meta.etag)
    print('size: ' + str(object_meta.content_length))

    # 5.获取文件具体内容
    object_content = bucket.get_object('motto.txt')
    # 对于不同的实现，get_object_content 返回的数据类型可能会不同
    # 如果它返回一个可读取的流，可以这样读取内容：
    if hasattr(object_content, 'read'):
        content = object_content.read()
        print(content.decode('utf-8'))  # 假设内容是字节流，需要解码为文本
    # 若get_object_content 直接返回字符串，则可以直接打印
    elif isinstance(object_content, str):
        print(object_content)

    # 6.删除文件
    # 删除名为motto.txt的Object
    bucket.delete_object('motto.txt')