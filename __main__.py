# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from git import *
from toolkits.gittools.git_tools import GitTools
from toolkits.filetools.file_tools import *
import os


if __name__ == '__main__':
    # repo_git = Repo(r"D:\Users\buguin\GitHub\game-of-life")
    file_path = r"D:\Temp\test"
    gitReop = GitTools()
    # gitReop.swicher = get_folderstatus(file_path)
    print("status", gitReop.swicher)
    # print(gitReop.initial())
    print(gitReop.git_source_path)
    gitReop.initial()
