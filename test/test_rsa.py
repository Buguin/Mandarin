import unittest

from toolkit.rsatools.rsa_tool_class import RSAToolClass


class MyTestCase(unittest.TestCase):
    def test_rsatoolclass(self):
        rsa_tool = RSAToolClass()
        rsa_tool.initial()
        # result = False
        if rsa_tool.pubkey_path != "" and rsa_tool.privkey_path != "":
            result = True
        else:
            result = False
        self.assertEqual(True, result)

    def test_encrypt(self):
        rsa_tool = RSAToolClass()
        rsa_tool.initial()
        case_pass_word = "AMXNWE!/325[]'`"
        encrypt_word = rsa_tool.encrypt(case_pass_word)
        encrypt_word_str = "IapJddvWPm07qa6QqaAvMS7OTuBxNtLsbWlGHAfEesqUQ4Hs91mHD69Ch7M6xZxMH3+wBZnmrXZj\nuP2YEoaaiT4OSYhADKUmJGNNpDG/evoKNZGpcw0iq92rt1rffzJCy8W8+UOHz7oGXJ1jI6Os24fG\nu8jD9YfYPbRhQoZtDG4=\n"
        encrypt_word_byte = encrypt_word_str.encode(encoding="utf-8")
        pass_word = rsa_tool.decrypt(encrypt_word_byte)
        print(type(encrypt_word))
        print(encrypt_word)
        print(pass_word)
        if case_pass_word == pass_word:
            result = True
        else:
            result = False
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
