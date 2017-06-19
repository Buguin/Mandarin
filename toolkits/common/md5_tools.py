# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'


class ConfigClass:
    def __init__(self):
        self.target_abspath = ""
        self.source_abspath = ""
        self.id = ""
        self.name = ""
        self.offering = ""
        self.version = ""
        self.type = ""
        self.model = set()
        self.compareresult = ""
        self.iscommercial = ""
        self.isupdate = ""
        self.iscompare = ""
        self.targetexcludeC = ""
        self.sourveexcludeC = ""

    def initial(self):
        print()

    def source_initial(self):
        self.initial()
        source_xmlpath = ""
        print()
        return source_xmlpath

    def target_initial(self):
        self.initial()
        target_xmlpath = ""
        print()
        return target_xmlpath

    def compare_diff(self, source_xmlpath, target_xmlpath):
        print()


class ExcludeToolClass:
    def __init__(self):
        """ExcludeToolClass is for initial the exclude file, folder and type in the target and source folder.
        """
        self.type = set()
        # restore the abs path of folder
        self.folder = set()
        # restore the abs path of file
        self.file = set()

    def __or__(self, other):
        self.type |= other.type
        print(self.type)
        # restore the abs path of folder
        self.folder |= other.folder
        # restore the abs path of file
        self.file |= other.file
        return self
