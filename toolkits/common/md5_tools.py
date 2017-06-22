# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import hashlib
import os


def get_md5(file_path):
    file_size = os.path.getsize(file_path) / 1024 / 1024
    if file_size > 80:
        return get_big_file_md5(file_path)
    else:
        return get_file_md5(file_path)


def get_file_md5(file_path):
    if os.path.isfile(file_path):
        f = open(file_path, 'rb')
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash_code = md5obj.hexdigest()
        f.close()
        return str(hash_code).upper()
    return None


def get_big_file_md5(file_path):
    if os.path.isfile(file_path):
        md5obj = hashlib.md5()
        maxbuf = 8192
        f = open(file_path, 'rb')
        while True:
            buf = f.read(maxbuf)
            if not buf:
                break
            md5obj.update(buf)
        f.close()
        hash_code = md5obj.hexdigest()
        return str(hash_code).upper()
    return None
