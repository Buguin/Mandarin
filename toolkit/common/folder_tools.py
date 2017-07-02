# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os


def get_folder_size(dir_path):
    """
    According to the param of dir_path, cacullate the size of folder and return it.
    :param dir_path: The path of folder, like D:\Temp
    :return: The size of folder
    """
    size = 0
    for root, dirs, files in os.walk(dir_path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def get_folder_status(fodler_path):
    """
    According to the param of dir_path, get the status of folder and return it.
    :param fodler_path: The path of folder, like D:\Temp
    :return: The status of folder:
    parm1 : The folder which on user computer is not create
    parm2 : The folder which on user computer is created, but is empty (<30)
    parm3 : The folder which on user computer is created and not empty  
    """
    if os.path.exists(fodler_path):
        print("This size of repo is existed")
        print(float(get_folder_size(fodler_path)))
        if float(get_folder_size(fodler_path)) < 30:
            print("This size of repo is ", get_folder_size(fodler_path) / 1024 / 1024)
            return 2
        else:
            print("This size of repo is ", get_folder_size(fodler_path) / 1024 / 1024)
            return 3
    else:
        print("This size of repo is not existed")
        return 1


def get_folder_path(fodler_name):
    folder_path = os.getcwd()
    path_list = folder_path.split('\\')
    num = path_list.index(fodler_name)
    path_list = path_list[:num + 1]
    folder_path = '\\'.join(path_list)
    return folder_path
