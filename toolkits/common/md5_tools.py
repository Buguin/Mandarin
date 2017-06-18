# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'


class ConfigClass:
    def __init__(self):
        self.target_abspath = ""
        self.source_abspath = ""
        self.id = ""
        self.offering = ""
        self.version = ""
        self.type = ""
        self.model = ""
        self.compareresult = ""
        self.iscommercial = ""
        self.isupdate = ""
        self.iscompare = ""
        self.targetexcludeC = ""
        self.sourveexcludeC = ""

    def initial(self):
        print()

    def get_md5_deque(self, xmlpath):
        print()


class ExcludeToolClass:
    def __init__(self):
        self.type = ""
        # restore the abs path of folder
        self.folder = ""
        # restore the abs path of file
        self.file = ""
