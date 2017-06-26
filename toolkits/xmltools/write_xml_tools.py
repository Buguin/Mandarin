# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os

from lxml import etree as et

from toolkits.common.md5_tools import get_file_md5


def get_source_infor(compare_tool):
    walk_file_path = compare_tool.source_abspath
    # with open(source_xmlpath, 'w') as f:
    #     f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    file_num = 1
    file_name = compare_tool.offering + " " + compare_tool.version
    source_xmlpath = os.getcwd() + r"\logs\ConfigItems\\" + file_name + ".xml"
    root = et.Element('sourceitem')
    source_dict = {'offering': str(compare_tool.offering), 'version': str(compare_tool.version)}
    files = et.SubElement(root, 'files', source_dict)
    for parent, dir_names, file_names in os.walk(walk_file_path):
        for file_name in file_names:
            file_path = os.path.join(parent, file_name)
            print("parent is:" + parent)
            print("filename is:" + file_name)
            print("the full name of the file is:" + file_path)
            file_dict = {'ID': str(file_num), 'md5': "", 'brother': '', 'child': '', 'parent': '', 'type': ''}
            file_dict.update({'md5': get_file_md5(file_path)})
            file_tag = et.SubElement(files, 'file', file_dict)
            file_path_tag = et.SubElement(file_tag, 'filepath')
            signfile_tag = et.SubElement(file_tag, 'signfile')
            # TODO get content of signfile
            file_path_tag.text = file_path
            file_num += 1
    files.set("num", str(file_num))
    tree = et.ElementTree(root)
    tree.write(source_xmlpath, encoding="utf-8", xml_declaration="utf-8", pretty_print=True)
    return source_xmlpath


def get_tatget_infor(compare_tool):
    walk_file_path = compare_tool.target_abspath
    file_num = 1
    target_xmlpath = os.getcwd() + r"\logs\TargetItems\\" + compare_tool.name + ".xml"
    root = et.Element('targetitem')
    target_dict = {'name': str(compare_tool.name)}
    files = et.SubElement(root, 'files', target_dict)
    for parent, dir_names, file_names in os.walk(walk_file_path):
        for file_name in file_names:
            file_path = os.path.join(parent, file_name)
            print("parent is:" + parent)
            print("filename is:" + file_name)
            print("the full name of the file is:" + file_path)
            filedict = {'ID': str(file_num), 'md5': '', 'bro': '', 'child': '', 'parent': '', 'type': '', 'result': ''}
            filedict.update({'md5': get_file_md5(file_path)})
            file_tag = et.SubElement(files, 'file', filedict)
            configdict = {'offering': '', 'version': '', 'ID': ''}
            et.SubElement(file_tag, 'config', configdict)
            path_tag = et.SubElement(file_tag, 'path')
            path_tag.text = file_path
            file_num += 1
    files.set("num", str(file_num))
    tree = et.ElementTree(root)
    tree.write(target_xmlpath, encoding="utf-8", xml_declaration="utf-8", pretty_print=True)
    return target_xmlpath


def get_compare_result(source_xmlpath, target_xmlpath):
    result = "Yes"
    target_tree = et.parse(target_xmlpath)
    for target_file_elem in target_tree.iter(tag='file'):
        print(target_file_elem.tag, target_file_elem.attrib)
        file_md5 = target_file_elem.attrib['md5']
        config_file_attrs = search_file_md5(source_xmlpath, file_md5)
        if config_file_attrs == "":
            result = "No"
            target_file_elem.set('result', result)
            continue
        else:
            target_file_elem.set('result', 'Yes')
            for config_elem in target_file_elem.iter(tag='config'):
                # file_dict['offering'] = source_files_elem.get("offering")
                # config_tag = target_file_elem.iter("config")
                config_elem.set('ID', str(config_file_attrs['ID']))
                config_elem.set('offering', str(config_file_attrs['offering']))
                config_elem.set('version', str(config_file_attrs['version']))
        target_tree.write(target_xmlpath, encoding="utf-8", xml_declaration="utf-8", pretty_print=True)
        print()
    return result


def search_file_md5(source_xmlpath, file_md5):
    source_tree = et.parse(source_xmlpath)
    file_dict = {'ID': '', 'offering': '', 'version': ''}
    # files_tag = source_tree.Element("files")
    for source_files_elem in source_tree.iter(tag='files'):
        file_dict['offering'] = source_files_elem.get("offering")
        file_dict['version'] = source_files_elem.get("version")
    for source_file_elem in source_tree.iter(tag='file'):
        # print(source_file_elem.tag, source_file_elem.attrib, source_file_elem.attrib['ID'])
        if file_md5 == source_file_elem.attrib['md5']:
            file_dict['ID'] = source_file_elem.get("ID")
            return file_dict
    return ""
