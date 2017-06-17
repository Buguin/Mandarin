# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkits.xmltools.xml_tools import *

# 初始化队列
git_deque = deque()
svn_deque = deque()
# initial relative path
targetpath = ""
sourcepath = ""

if __name__ == '__main__':
    # TODO read xml file to get the info of CVS
    configpath = r"D:\Users\buguin\PycharmProjects\Mandarin\scripts\config.xml"
    configtablepath = r"D:\Users\buguin\PycharmProjects\Mandarin\scripts\configtable.xml"
    git_deque = get_git_deque(configpath)
    # xmltools.get_git_deque(xmlpath, gitdeque)
    # xmltools.get_svn_deque(xmlpath, svndeque)
    # xmltools.get_mandarin_deque(xmlpath, gitdeque)
    # out stack and initial
    # Get configtable.xml
    # repo_git = Repo(r"D:\Users\buguin\GitHub\game-of-life")
    file_path = r"D:\Temp\test"
    # TODO get code throgh git and svn tool
    # gitReop = GitTool(file_path)
    # gitReop.swicher = get_folderstatus(file_path)
    # print("status", gitReop.swicher)
    # print(gitReop.initial())
    # print(gitReop.git_source_path)
    # gitReop.initial()
    # TODO compare and export the compare result
