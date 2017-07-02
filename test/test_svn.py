import unittest

import toolkits.svntools.local as lc
import toolkits.svntools.remote as re
from toolkits.svntools.svn_tools import SVNToolClass


class MyTestCase(unittest.TestCase):
    def test_svn_remote(self):
        r = re.RemoteClient('file:///D:/Users/buguin/SVN_REPOS/svn_test')
        result = r.checkout('D:\svn_test')
        self.assertEqual(result, 0)

    def test_svn_local(self):
        r = lc.LocalClient('D:\svn_test')
        result = r.update()
        self.assertEqual(result, 0)

    def test_svn_tools(self):
        svntools = SVNToolClass()
        svntools.folder_name = "working"
        svntools.username = ""
        svntools.passwd = ""
        svntools.repo_path = "file:///D:/Users/buguin/SVN_REPOS/svn_test"
        svntools.svn_source_path = "D:\Temp"
        result = svntools.initial()
        ture_result = [100, 200, 300]
        self.assertEqual(result in ture_result, True)


if __name__ == '__main__':
    unittest.main()
