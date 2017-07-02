# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkit.xmltools.write_xml_tools import get_source_infor, get_tatget_infor, get_compare_result


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

    def source_initial(self):
        source_xmlpath = get_source_infor(self)
        return source_xmlpath

    def target_initial(self):
        target_xmlpath = get_tatget_infor(self)
        return target_xmlpath

    def compare_diff(self, source_xmlpath, target_xmlpath):
        self.compareresult = get_compare_result(source_xmlpath, target_xmlpath)
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

    # TODO connect path of file and folder through file_path
    def initial(self, file_path):
        print()
        return self
