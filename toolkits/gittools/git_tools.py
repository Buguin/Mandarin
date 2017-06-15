# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'


class GitTools:
    def __init__(self):
        """ The status of git repository        
        :parm0 : The folder which on user computer is not create
        :parm1 : The folder which on user computer is created, but is empty
        :parm2 : The folder which on user computer is created and not empty        
        """
        self.swicher = 0
        self.repo_path = ""

    def initial(self):
        # TODO  通过给出库的状态下载代码
        initialize_name = 'initialize_' + str(self.swicher)
        initialize = getattr(self, initialize_name, lambda: "nothing")
        # print(self.swicher)
        return initialize()

    def initialize_0(self):
        return 0

    def initialize_1(self):
        return 1

    def initialize_2(self):
        return 2

    # @property
    # def swicher(self):
    #     return self.swicher
