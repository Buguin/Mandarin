# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os


def get_source_infor(compare_tool):
    walk_file_path = compare_tool.source_abspath
    source_xmlpath = r"D:\Users\buguin\PycharmProjects\Mandarin\logs\configitems\DOPRA V100R010C00.xml"

    for parent, dirnames, filenames in os.walk(walk_file_path):
        for filename in filenames:
            filepath = os.path.join(parent, filename)
            print("parent is:" + parent)
            print("filename is:" + filename)
            print("the full name of the file is:" + filepath)
    print()
    return source_xmlpath


def get_tatget_infor():
    print()
    target_xmlpath = ""
    return target_xmlpath
