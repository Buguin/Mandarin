# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import base64
import os

import rsa

from toolkit.common.folder_tools import get_folder_path


class RSAToolClass:
    def __init__(self):
        """
        
        """
        self.privkey_path = ""
        self.pubkey_path = ""

    def initial(self):
        project_path = get_folder_path("Mandarin")
        self.pubkey_path = project_path + "\\scripts\\public.pem"
        self.privkey_path = project_path + "\\scripts\\private.pem"
        if not os.path.exists(self.pubkey_path) and not os.path.exists(self.privkey_path):
            (pubkey, privkey) = rsa.newkeys(1024)
            with open(self.pubkey_path, 'w+') as f:
                f.write(pubkey.save_pkcs1().decode())
            with open(self.privkey_path, 'w+') as f:
                f.write(privkey.save_pkcs1().decode())

    def encrypt(self, message):
        with open(self.pubkey_path, 'r') as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        crypto = rsa.encrypt(message.encode(), pubkey)
        encrypt_msg = base64.encodebytes(crypto)
        return encrypt_msg

    def decrypt(self, message):
        with open(self.privkey_path, 'r') as f:
            privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
        # message = remove_character(message, '\\')
        encrypt_msg = base64.decodebytes(message)
        message = rsa.decrypt(encrypt_msg, privkey).decode()
        return message
