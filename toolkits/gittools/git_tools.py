# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os
import git
from git import Repo
from toolkits.filetools.file_tools import *


class GitTools:
    def __init__(self):
        """ Swicher is describe the status of git repository        
        :parm0 : The folder which on user computer is not create
        :parm1 : The folder which on user computer is created, but is empty
        :parm2 : The folder which on user computer is created and not empty        
        """
        self.repo_path = "https://github.com/Buguin/learngit.git"
        self.source_path = "D:\Temp"
        self.folder_name = "learngit"
        self.git_source_path = self.source_path + "\\" + self.folder_name
        self.swicher = get_folderstatus(self.git_source_path)

    def initial(self):
        # TODO  通过给出库的状态下载代码
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
        repo = git.Repo.clone_from(self.repo_path, self.git_source_path, branch='master')
        print("initialize_1", repo.head)
        return 1

    def initialize_2(self):
        repo = Repo(self.git_source_path)
        print(repo.description)
        return 2
