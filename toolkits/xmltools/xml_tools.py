# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkits.gittools.git_tools import GitTool
from collections import deque
from xml.dom.minidom import parse
import os
import xml.dom.minidom


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
        git_tool = GitTool(get_targetpath(collection))
        git_tool.git_source_path = get_childtag_data(git_tag, "gitpath")
        git_tool.usernmae = git_tag.getAttribute("username")
        git_tool.passwd = git_tag.getAttribute("passwd")
        git_deque.append(git_tool)
    return git_deque


def get_targetpath(collection):
    # dom_tree = xml.dom.minidom.parse(xmlpath)
    # collection = dom_tree.documentElement
    targetpath_tag = get_fist_tag(collection, "targetpath")
    osname = os.name
    if osname == "nt":
        return get_childtag_data(targetpath_tag, "windowspath")
    elif osname == "posix":
        return get_childtag_data(targetpath_tag, "linuxpath")


def get_childtag_data(parent_tag, child_tag_name):
    child_tag = get_fist_tag(parent_tag, child_tag_name)
    return child_tag.firstChild.data


def get_fist_tag(parent_tag, child_tag_name):
    child_tags = parent_tag.getElementsByTagName(child_tag_name)
    return child_tags[0]
