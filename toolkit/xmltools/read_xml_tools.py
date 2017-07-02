# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import xml.dom.minidom
from collections import deque

from toolkit.common.config_tools import ConfigClass
from toolkit.common.config_tools import ExcludeToolClass
from toolkit.gittools.git_tools import GitToolClass
from toolkit.rsatools.rsa_tool_class import RSAToolClass
from toolkit.svntools.svn_tools import SVNToolClass
from toolkit.xmltools.com_xml_tools import *


def get_targetpath(collection):
    """
    According to the type of os, get the target path of source code from config.xml
    :param collection: The root tag of config.xml
    :return: The target path of os
    """
    targetpath_tag = get_fist_tag(collection, "targetpath")
    osname = os.name
    if osname == "nt":
        return get_childtag_data(targetpath_tag, "windowspath")
    elif osname == "posix":
        return get_childtag_data(targetpath_tag, "linuxpath")


def get_sourcepath(collection):
    """
    According to the type of os, get the source path of source code from config.xml
    :param collection: The root tag of config.xml
    :return: The source path of os
    """
    sourcepath_tag = get_fist_tag(collection, "sourcepath")
    osname = os.name
    if osname == "nt":
        return get_childtag_data(sourcepath_tag, "windowspath")
    elif osname == "posix":
        return get_childtag_data(sourcepath_tag, "linuxpath")


def get_git_deque(xmlpath):
    git_deque = deque()
    rsa_tool = RSAToolClass()
    rsa_tool.initial()
    dom_tree = xml.dom.minidom.parse(xmlpath)
    collection = dom_tree.documentElement
    targetpath_tag = get_fist_tag(collection, "targetpath")
    gits_tag = get_fist_tag(targetpath_tag, "gits")
    com_username = gits_tag.getAttribute("username")
    com_passwd = get_childtag_data(gits_tag, "password")
    com_passwd_1 = "IapJddvWPm07qa6QqaAvMS7OTuBxNtLsbWlGHAfEesqUQ4Hs91mHD69Ch7M6xZxMH3+wBZnmrXZj\nuP2YEoaaiT4OSYhADKUmJGNNpDG/evoKNZGpcw0iq92rt1rffzJCy8W8+UOHz7oGXJ1jI6Os24fG\nu8jD9YfYPbRhQoZtDG4=\n"
    print(com_passwd == com_passwd_1)
    com_passwd_bytes_utf8 = com_passwd.encode(encoding="utf-8")
    com_passwd = rsa_tool.decrypt(com_passwd_bytes_utf8)
    # com_passwd = gits_tag.getAttribute("password")
    print(com_username, com_passwd)
    git_tags = gits_tag.getElementsByTagName("git")
    print(get_targetpath(collection))

    for git_tag in git_tags:
        git_tool = GitToolClass()
        git_tool.git_source_path = get_targetpath(collection)
        git_tool.repo_path = get_childtag_data(git_tag, "gitpath")
        if git_tag.getAttribute("username") == "":
            git_tool.user_name = com_username
        else:
            git_tool.user_name = git_tag.getAttribute("username")
        if get_childtag_data(git_tag, "password") == "":
            git_tool.pass_word = com_passwd
        else:
            git_tool.pass_word = get_childtag_data(git_tag, "password")
        print(get_childtag_data(git_tag, "foldername"))
        if get_childtag_data(git_tag, "foldername"):
            git_tool.folder_name = get_childtag_data(git_tag, "foldername")
        else:
            temp = git_tool.repo_path.split('/')
            temp = temp[len(temp)-1].split('.')
            git_tool.folder_name = temp[0]
        git_deque.append(git_tool)
    return git_deque


def get_svn_deque(xmlpath):
    svn_deque = deque()
    dom_tree = xml.dom.minidom.parse(xmlpath)
    collection = dom_tree.documentElement
    svns_tag = get_fist_tag(collection, "svns")
    com_username = svns_tag.getAttribute("username")
    com_passwd = get_childtag_data(svns_tag, "password")
    # com_passwd = svns.getAttribute("password")
    print(com_username, com_passwd)
    svn_tags = svns_tag.getElementsByTagName("svn")
    print(get_targetpath(collection))
    for svn_tag in svn_tags:
        svn_tool = SVNToolClass()
        svn_tool.svn_source_path = get_targetpath(collection)
        svn_tool.repo_path = get_childtag_data(svn_tag, "svnpath")
        if svn_tag.getAttribute("username") == "":
            svn_tool.user_name = com_username
        else:
            svn_tool.user_name = svn_tag.getAttribute("username")
        if get_childtag_data(svn_tag, "password") == "":
            svn_tool.pass_word = com_passwd
        else:
            svn_tool.pass_word = get_childtag_data(svn_tag, "password")
        print(get_childtag_data(svn_tag, "foldername"))
        if get_childtag_data(svn_tag, "foldername"):
            svn_tool.folder_name = get_childtag_data(svn_tag, "foldername")
        else:
            temp = svn_tool.repo_path.split('/')
            svn_tool.folder_name = temp[len(temp) - 1]
        svn_deque.append(svn_tool)
    return svn_deque


def get_config_deque(xmlpath):
    compare_deque = deque()
    dom_tree = xml.dom.minidom.parse(xmlpath)
    collection = dom_tree.documentElement
    com_targetpath = get_targetpath(collection)
    com_sourcepath = get_sourcepath(collection)
    targetpath_tag = get_fist_tag(collection, "targetpath")
    sourcepath_tag = get_fist_tag(collection, "sourcepath")
    com_targetexlude_tag = get_fist_tag(targetpath_tag, "exclude")
    com_targetexlude_class = get_exclude_class(com_targetexlude_tag)
    com_sourceexlude_tag = get_fist_tag(sourcepath_tag, "exclude")
    com_sourceexlude_class = get_exclude_class(com_sourceexlude_tag)
    configlist_tag = get_fist_tag(collection, "configlist")
    config_tags = configlist_tag.getElementsByTagName("config")
    for config_tag in config_tags:
        config_tool = ConfigClass()
        targetpath = get_childtag_data(config_tag, "targetpath")
        sourvepath = get_childtag_data(config_tag, "sourvepath")
        config_tool.target_abspath = path_connect(com_targetpath, targetpath)
        config_tool.source_abspath = path_connect(com_sourcepath, sourvepath)
        config_tool.id = config_tag.getAttribute("id")
        config_tool.name = config_tag.getAttribute("name")
        config_tool.offering = config_tag.getAttribute("offering")
        config_tool.version = config_tag.getAttribute("version")
        config_tool.type = get_childtag_data(config_tag, "type")
        config_models = config_tag.getElementsByTagName("modle")
        print(len(config_models))
        for config_model in config_models:
            config_tool.model |= {config_model.firstChild.data.strip()}
            print(config_tool.model)
        # print(config_tool.model)
        config_tool.iscommercial = get_childtag_data(config_tag, "iscommercial")
        config_tool.isupdate = get_childtag_data(config_tag, "isupdate")
        config_tool.iscompare = get_childtag_data(config_tag, "iscompare")
        config_tool.compareresult = get_childtag_data(config_tag, "compareresult")
        config_target_tag = get_fist_tag(config_tag, "targetexclude")
        config_source_tag = get_fist_tag(config_tag, "sourveexclude")
        com_target_class = get_exclude_class(config_target_tag)
        com_source_class = get_exclude_class(config_source_tag)
        config_tool.targetexcludeC = exclude_class_connect(com_target_class, com_targetexlude_class)
        config_tool.sourveexcludeC = exclude_class_connect(com_source_class, com_sourceexlude_class)
        config_tool.targetexcludeC = config_tool.targetexcludeC.initial(config_tool.target_abspath)
        config_tool.sourveexcludeC = config_tool.sourveexcludeC.initial(config_tool.source_abspath)
        compare_deque.append(config_tool)
        print(config_tool.id)
    return compare_deque


def get_exclude_class(exclude_tag):
    exclude_class = ExcludeToolClass()
    strtype = get_childtag_data(exclude_tag, "type")
    exclude_class.types = get_exclude_set(strtype, ';')
    strfolder = get_childtag_data(exclude_tag, "folder")
    exclude_class.folders = get_exclude_set(strfolder, ';')
    strfile = get_childtag_data(exclude_tag, "file")
    exclude_class.files = get_exclude_set(strfile, ';')
    return exclude_class


def get_exclude_set(exclude_str, split_char):
    exclude_set = set()
    etypes = exclude_str.split(split_char)
    for etype in etypes:
        exclude_set |= {etype}
    return exclude_set


def exclude_class_connect(first_exclude_class, second_exclude_class):
    exclude_class = first_exclude_class | second_exclude_class
    return exclude_class


def exclude_initial(exclude_class):
    return exclude_class
