# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os


def get_dirsize(dir_path):
    size = 0
    for root, dirs, files in os.walk(dir_path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def get_repostatus(repo_path):
    if os.path.exists(repo_path):
        print('文件存在')
        # repo = Repo(file_path)
        # assert not repo.bare
        print(get_dirsize(repo_path)/1024/1024)
        if os.path.getsize(repo_path):
            print('文件存在且不为空')
            return 2
        else:
            print('文件存在且为空')
            return 1
            # repo = gittools.Repo.clone_from("https://github.com/Buguin/learngit.git", r"D:\Temp\test")
    else:
        print('文件不存在')
        return 0
