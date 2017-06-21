# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkits.common.str_tools import file_name_connect
from toolkits.xmltools.write_xml_tools import get_source_infor


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
        self.sourveexcludeC = file_name_connect(self.target_abspath, self.sourveexcludeC)
        source_xmlpath = get_source_infor(self)
        print()
        return source_xmlpath

    def target_initial(self):
        self.targetexcludeC = file_name_connect(self.target_abspath, self.targetexcludeC)
        target_xmlpath = ""
        print()
        return target_xmlpath

    def compare_diff(self, source_xmlpath, target_xmlpath):
        print()


class ExcludeToolClass:
    def __init__(self):
        """ExcludeToolClass is for initial the exclude file, folder and type in the target and source folder.
        """
        self.types = set()
        # restore the abs path of folder
        self.folders = set()
        # restore the abs path of file
        self.files = set()

    def __or__(self, other):
        self.types |= other.types
        print(self.types)
        # restore the abs path of folder
        self.folders |= other.folders
        # restore the abs path of file
        self.files |= other.files
        return self
