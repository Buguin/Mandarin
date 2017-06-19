# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkits.xmltools.xml_tools import *


# The deque for download sourcecode
git_deque = deque(maxlen=20)
svn_deque = deque(maxlen=20)
# The deque for compare code
compare_deque = deque(maxlen=20)
# initial relative path
targetpath = ""
sourcepath = ""

if __name__ == '__main__':
    # get deque of repository, include svn and git
    configpath = os.getcwd() + "\scripts\config.xml"
    # configtablepath = os.getcwd() + "\scripts\configtable.xml"
    # initial information of vcs
    """
    git_deque = get_git_deque(configpath)
    svn_deque = get_svn_deque(configpath)
    """
    # get code throgh git and svn tool
    """
    while git_deque:
        git_tool = git_deque.popleft()
        print(git_tool)
        git_tool.initial()
    """
    # initial information of config
    compare_deque = get_md5_deque(configpath)
    # while compare_deque:
    #     compare_tool = compare_deque.popleft()
    #     compare_deque.append(git_tool)
    #     print(git_tool)
    #     git_tool.initial()

    # Get configtable.xml
    # gitReop = GitTool(file_path)
    # gitReop.swicher = get_folderstatus(file_path)
    # print("status", gitReop.swicher)
    # print(gitReop.initial())
    # print(gitReop.git_source_path)
    # gitReop.initial()
    # TODO compare and export the compare result
