import unittest
import xml.dom.minidom

from toolkit.common.folder_tools import get_folder_path
from toolkit.xmltools.com_xml_tools import *


class MyTestCase(unittest.TestCase):
    def test_com_get_childtag_data(self):
        password_case = "IapJddvWPm07qa6QqaAvMS7OTuBxNtLsbWlGHAfEesqUQ4Hs91mHD69Ch7M6xZxMH3+wBZnmrXZj\\nuP2YEoaaiT4OSYhADKUmJGNNpDG/evoKNZGpcw0iq92rt1rffzJCy8W8+UOHz7oGXJ1jI6Os24fG\\nu8jD9YfYPbRhQoZtDG4=\\n"
        project_path = get_folder_path("Mandarin")
        config_path = project_path + "\\scripts\\config.xml"
        dom_tree = xml.dom.minidom.parse(config_path)
        collection = dom_tree.documentElement
        svn_tag = get_fist_tag(collection, "svn")
        password = get_childtag_data(svn_tag, "password")
        if password_case == password:
            result = True
        else:
            result = False
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
