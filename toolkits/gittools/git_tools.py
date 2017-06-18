# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import git
from git import Repo

from toolkits.common.folder_tools import *


class GitToolClass:
    def __init__(self, source_path):
        """
        
        :param source_path: 
        """
        self.repo_path = ""
        self.folder_name = ""
        self.username = ""
        self.passwd = ""
        self.git_tool_status = 0
        self.git_source_path = source_path
        self.swicher = ""

    def initial(self):
        self.git_source_path = self.git_source_path + "\\" + self.folder_name
        self.swicher = get_folder_status(self.git_source_path)
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
            repo = git.Repo.clone_from(self.repo_path, self.git_source_path, branch='master')
        except Exception as err:
            print(Exception, ":", err)
            return 101
        print("initialize_1", repo.head)
        return 100

    def initialize_2(self):
        cmd = r"rd /s /q " + self.git_source_path
        os.popen(cmd, 'r', 1)
        # os.removedirs(self.git_source_path)
        try:
            repo = git.Repo.clone_from(self.repo_path, self.git_source_path, branch='master')
        except Exception as err:
            print(Exception, ":", err)
            return 201
        print("initialize_1", repo.head)
        return 200

    def initialize_3(self):
        repo = Repo(self.git_source_path)
        try:
            repo.remote().pull()
        except Exception as err:
            print(Exception, ":", err)
            return 301
        return 300
