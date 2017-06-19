import unittest

from toolkits.common.md5_tools import ExcludeToolClass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    ex1 = ExcludeToolClass()
    ex2 = ExcludeToolClass()
    # ex3 = ExcludeToolClass()
    ex1.type = {"ddd", "ddd", "aaaaaa"}
    ex2.type = {"xxxx", "xaaa", "ffff"}
    ex3 = ex1 | ex2
    print(ex3.type)
    unittest.main()
