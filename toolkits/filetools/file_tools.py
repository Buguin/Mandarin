# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os


def get_dirsize(dir_path):
    """
    According to the param of dir_path, cacullate the size of folder and return it.
    :param dir_path: The path of folder, like D:\Temp
    :return: The size of folder
    """
    size = 0
    for root, dirs, files in os.walk(dir_path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def get_folderstatus(fodler_path):
    """
    According to the param of dir_path, get the status of folder and return it.
    :param fodler_path: The path of folder, like D:\Temp
    :return: The status of folder:
    parm0 : The folder which on user computer is not create
    parm1 : The folder which on user computer is created, but is empty
    parm2 : The folder which on user computer is created and not empty  
    """
    if os.path.exists(fodler_path):
        print("This size of repo is existed")
        if os.path.getsize(fodler_path):
            print("This size of repo is ", get_dirsize(fodler_path) / 1024 / 1024)
            return 2
        else:
            print("This size of repo is ", get_dirsize(fodler_path) / 1024 / 1024)
            return 1
            # repo = gittools.Repo.clone_from("https://github.com/Buguin/learngit.git", r"D:\Temp\test")
    else:
        print("This size of repo is not existed")
        return 0
