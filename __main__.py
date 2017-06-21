# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkits.xmltools.read_xml_tools import *


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
    compare_deque = get_config_deque(configpath)
    while compare_deque:
        compare_tool = compare_deque.popleft()
        print(compare_tool.offering + compare_tool.version)
        source_xmlpath = compare_tool.source_initial()
        target_xmlpath = compare_tool.target_initial()
        compare_tool.compare_diff(source_xmlpath, target_xmlpath)
        print(compare_tool.compareresult)
        # TODO export the compare result
