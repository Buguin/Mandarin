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

    def initialize_0(self):
        # os.makedirs(self.git_source_path)
        repo = git.Repo.clone_from(self.repo_path, self.git_source_path, branch='master')
        print("initialize_0", repo.head)
        return 0

    def initialize_1(self):
        cmd = r"rd /s /q " + self.git_source_path
        os.popen(cmd, 'r', 1)
        # os.removedirs(self.git_source_path)
        repo = git.Repo.clone_from(self.repo_path, self.git_source_path, branch='master')
        print("initialize_1", repo.head)
        return 1

    def initialize_2(self):
        repo = Repo(self.git_source_path)
        print(repo.description)
        return 2
