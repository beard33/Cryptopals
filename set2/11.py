import utils.tools as tools
import random
from os import urandom
import secrets

def generateKey():
    return bytes(urandom(16))

def generateIV():
    return bytes(urandom(tools.BLOCK_SIZE))

def oracleAES(plaintext):
    pt = []
    randomBytes = urandom(secrets.randbelow(6) + 5)
    pt = randomBytes + plaintext + randomBytes
    padded = tools.pkcs7Padding(pt)
    if secrets.randbelow(2) % 2 == 0:
        return tools.ecbEncrypt(padded, generateKey())
    else:
        return tools.cbcEncrypt(padded, generateKey(), generateIV())

plaintext = b'0x42'*32
ecb, cbc = 0, 0

for _ in range (100):
    ct = oracleAES(plaintext)
    if tools.detectEcbMode(ct):
        ecb += 1
    else:
        cbc += 1

print("ECB: %d \t CBC:%d" %(ecb, cbc))