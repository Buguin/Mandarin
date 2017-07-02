# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import base64
import os

import rsa


class RSAToolClass:
    def __init__(self):
        """
        
        """
        self.privkey_path = ""
        self.pubkey_path = ""

    def initial(self):
        if not os.path.exists('public.pem') and not os.path.exists('private.pem'):
            (pubkey, privkey) = rsa.newkeys(1024)
            with open('public.pem', 'w+') as f:
                f.write(pubkey.save_pkcs1().decode())
            with open('private.pem', 'w+') as f:
                f.write(privkey.save_pkcs1().decode())
        self.pubkey_path = "public.pem"
        self.privkey_path = "private.pem"

    def encrypt(self, message):
        with open(self.pubkey_path, 'r') as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        crypto = rsa.encrypt(message.encode(), pubkey)
        encrypt_msg = base64.encodebytes(crypto)
        return encrypt_msg

    def decrypt(self, message):
        with open(self.privkey_path, 'r') as f:
            privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
        encrypt_msg = base64.decodebytes(message)
        message = rsa.decrypt(encrypt_msg, privkey).decode()
        return message
