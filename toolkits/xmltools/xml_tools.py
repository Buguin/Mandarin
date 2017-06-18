# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkits.gittools.git_tools import GitToolClass
from collections import deque
from xml.dom.minidom import parse
import xml.dom.minidom
import os


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
        git_tool = GitToolClass(get_targetpath(collection))
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
        svn_tool = GitToolClass(get_targetpath(collection))
        svn_tool.git_source_path = get_childtag_data(svn_tag, "svnpath")
        svn_tool.username = svn_tag.getAttribute("username")
        svn_tool.passwd = svn_tag.getAttribute("passwd")
        svn_deque.append(svn_tool)
    return svn_deque


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
    print(child_tag.firstChild.data.strip())
    return child_tag.firstChild.data.strip()


def get_fist_tag(parent_tag, child_tag_name):
    child_tags = parent_tag.getElementsByTagName(child_tag_name)
    print(child_tags[0])
    return child_tags[0]
