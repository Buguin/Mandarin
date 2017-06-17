# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkits.xmltools.xml_tools import *

# 初始化队列
git_deque = deque(maxlen=20)
svn_deque = deque(maxlen=20)
# initial relative path
targetpath = ""
sourcepath = ""

if __name__ == '__main__':
    # get deque of repository, include svn and git
    configpath = os.getcwd() + "\scripts\config.xml"
    configtablepath = os.getcwd() + "\scripts\configtable.xml"
    git_deque = get_git_deque(configpath)
    svn_deque = get_svn_deque(configpath)
    print(len(git_deque))
    print(len(svn_deque))
    # while git_deque:
    #     git_tool = git_deque.popleft()
    #     print(1)
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
