# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os

from lxml import etree as et

from toolkits.common.md5_tools import get_md5


def get_source_infor(compare_tool):
    walk_file_path = compare_tool.source_abspath
    # with open(source_xmlpath, 'w') as f:
    #     f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    file_num = 1
    file_name = compare_tool.offering + " " + compare_tool.version
    source_xmlpath = os.getcwd() + r"\logs\ConfigItems\\" + file_name + ".xml"
    root = et.Element('targetitem')
    files = et.SubElement(root, 'files')
    for parent, dir_names, file_names in os.walk(walk_file_path):
        for file_name in file_names:
            file_path = os.path.join(parent, file_name)
            filedict = {'ID': str(file_num), 'md5': "", 'brother': '', 'child': '', 'parent': '', 'type': ''}
            filedict.update({'md5': get_md5(file_path)})
            file = et.SubElement(files, 'file', filedict)
            file.text = file_path
            file_num += 1
            print("parent is:" + parent)
            print("filename is:" + file_name)
            print("the full name of the file is:" + file_path)
    files.set("num", str(file_num))
    tree = et.ElementTree(root)
    tree.write(source_xmlpath, encoding="utf-8", xml_declaration="utf-8", pretty_print=True)
    return source_xmlpath


def get_tatget_infor():
    print()
    target_xmlpath = ""
    return target_xmlpath
