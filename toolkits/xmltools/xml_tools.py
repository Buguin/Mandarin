# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os
import xml.dom.minidom
from collections import deque
from xml.dom.minidom import parse

from toolkits.common.md5_tools import ConfigClass
from toolkits.common.md5_tools import ExcludeToolClass
from toolkits.gittools.git_tools import GitToolClass


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


def get_childtag_data(parent_tag, child_tag_name):
    """
    Get the content of the child tag
    :param parent_tag: the parent of tag
    :param child_tag_name: the name of child
    :return: the content in child tag
    """
    child_tag = get_fist_tag(parent_tag, child_tag_name)
    print(child_tag.firstChild.data.strip())
    return child_tag.firstChild.data.strip()


def get_fist_tag(parent_tag, child_tag_name):
    """
    According to the name of child tag name, find the first tag of child
    :param parent_tag: the paten tag
    :param child_tag_name: the name of child tag
    :return: first tag of child
    """
    child_tags = parent_tag.getElementsByTagName(child_tag_name)
    print(child_tags[0])
    return child_tags[0]


def get_git_deque(xmlpath):
    git_deque = deque()
    dom_tree = xml.dom.minidom.parse(xmlpath)
    collection = dom_tree.documentElement
    gits = get_fist_tag(collection, "gits")
    com_username = gits.getAttribute("username")
    com_passwd = gits.getAttribute("passwd")
    print(com_username, com_passwd)
    git_tags = gits.getElementsByTagName("git")
    print(get_targetpath(collection))
    for git_tag in git_tags:
        git_tool = GitToolClass()
        git_tool.git_source_path = get_targetpath(collection)
        git_tool.repo_path = get_childtag_data(git_tag, "gitpath")
        git_tool.username = git_tag.getAttribute("username")
        git_tool.passwd = git_tag.getAttribute("passwd")
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
    svns = get_fist_tag(collection, "svns")
    com_username = svns.getAttribute("username")
    com_passwd = svns.getAttribute("passwd")
    print(com_username, com_passwd)
    svn_tags = svns.getElementsByTagName("svn")
    print(get_targetpath(collection))
    for svn_tag in svn_tags:
        svn_tool = GitToolClass()
        svn_tool.git_source_path = get_childtag_data(svn_tag, "svnpath")
        svn_tool.username = svn_tag.getAttribute("username")
        svn_tool.passwd = svn_tag.getAttribute("passwd")
        svn_deque.append(svn_tool)
    return svn_deque


def get_md5_deque(xmlpath):
    compare_deque = deque()
    dom_tree = xml.dom.minidom.parse(xmlpath)
    collection = dom_tree.documentElement
    com_targetpath = get_targetpath(collection)
    com_sourcepath = get_sourcepath(collection)
    targetpath_tag = get_fist_tag(collection, "targetpath")
    sourcepath_tag = get_fist_tag(collection, "sourcepath")
    com_targetexlude_tag = get_fist_tag(targetpath_tag, "exclude")
    com_sourceexlude_tag = get_fist_tag(sourcepath_tag, "exclude")
    configlist_tag = get_fist_tag(collection, "configlist")
    config_tags = configlist_tag.getElementsByTagName("config")
    for config_tag in config_tags:
        config_tool = ConfigClass()
        config_tool.target_abspath = com_targetpath
        config_tool.source_abspath = com_sourcepath
        config_tool.id = config_tag.getAttribute("id")
        config_tool.offering = config_tag.getAttribute("offering")
        config_tool.version = config_tag.getAttribute("version")
        config_tool.type = get_childtag_data(config_tag, "type")
        config_tool.model = get_childtag_data(config_tag, "model")
        config_tool.iscommercial = get_childtag_data(config_tag, "iscommercial")
        config_tool.isupdate = get_childtag_data(config_tag, "isupdate")
        config_tool.iscompare = get_childtag_data(config_tag, "iscompare")
        config_tool.compareresult = get_childtag_data(config_tag, "compareresult")
        targettemp = get_fist_tag(config_tag, "targetexclude")
        sourcetemp = get_fist_tag(config_tag, "sourveexclude")
        config_tool.targetexcludeC = exclude_connect(targettemp, com_targetexlude_tag)
        config_tool.sourveexcludeC = exclude_connect(sourcetemp, com_sourceexlude_tag)
        compare_deque.append(config_tool)
        print(config_tool.id)
    print()


def get_exclude_class(exclude_tag):
    exclude_class = ExcludeToolClass()
    strtype = get_childtag_data(exclude_tag, "type")
    exclude_class.type = strtype.split(";")
    strfolder = get_childtag_data(exclude_tag, "folder")
    exclude_class.folder = strfolder.split(";")
    strfile = get_childtag_data(exclude_tag, "file")
    exclude_class.file = strfile.split(";")
    return exclude_class


def exclude_connect(first_tag, second_tag):
    exclude_class = ""
    print()
    return exclude_class
