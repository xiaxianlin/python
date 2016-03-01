#-*- coding=utf-8 -*-
import rsa

if __name__ == '__main__':
    (pubkey, privkey) = rsa.newkeys(512)
    message = 'hello world'
    secretMessage = rsa.encrypt(message, pubkey)
    rsa.decrypt(secretMessage, privkey)