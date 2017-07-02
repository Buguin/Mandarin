# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import time

import toolkits.svntools.local as lc
import toolkits.svntools.remote as re
from toolkits.common.folder_tools import *


class SVNToolClass:
    def __init__(self):
        """
        
        """
        self.repo_path = ""
        self.folder_name = ""
        self.user_name = ""
        self.pass_word = ""
        self.svn_tool_status = 0
        self.svn_source_path = ""
        self.swicher = ""

    def initial(self):
        self.svn_source_path = self.svn_source_path + "\\" + self.folder_name
        self.swicher = get_folder_status(self.svn_source_path)
        if self.repo_path == "" or self.folder_name == "":
            print("repo_path and folder_name is empty")
            return 1
        else:
            initialize_name = 'initialize_' + str(self.swicher)
            initialize = getattr(self, initialize_name, lambda: "nothing")
            # print(self.swicher)
            return initialize()

    def initialize_1(self):
        # os.makedirs(self.git_source_path)
        try:
            repo = re.RemoteClient(self.repo_path)
            repo.checkout(self.svn_source_path)
            # repo = git.Repo.clone_from(self.repo_path, self.git_source_path, branch='master')
        except Exception as err:
            print(Exception, ":", err)
            return 101
        print("initialize_1", repo.path)
        return 100

    def initialize_2(self):
        cmd = r"rd /s /q " + self.svn_source_path + " & echo 0"
        os.popen(cmd, 'r', 1)
        # wait delet the file
        print("wait delet the file")
        # fixme if the folder delete error, the repository would not download successfull.
        time.sleep(5)
        # os.removedirs(self.git_source_path)
        try:
            while not os.path.exists(self.svn_source_path):
                repo = re.RemoteClient(self.repo_path)
                repo.checkout(self.svn_source_path)
                print("initialize_2", repo.path)
        except Exception as err:
            print(Exception, ":", err)
            return 201
        return 200

    def initialize_3(self):
        repo = lc.LocalClient(self.svn_source_path)
        try:
            repo.update()
            print("initialize_3", repo.path)
        except Exception as err:
            print(Exception, ":", err)
            return 301
        return 300
