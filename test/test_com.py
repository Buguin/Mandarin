import unittest

from toolkit.common.folder_tools import *


class MyTestCase(unittest.TestCase):
    def test_folder_path(self):
        folder_path = get_folder_path("Mandarin")
        if folder_path == r"D:\Users\buguin\PycharmProjects\Mandarin":
            result = True
        else:
            result = False
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
