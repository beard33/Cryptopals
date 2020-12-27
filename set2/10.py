# Implement CBC mode for AES-128
import utils.tools as tools
from base64 import b64decode, b64encode
from Crypto.Cipher import AES

test = b'YellowSubmarine'
key = b'YELLOW SUBMARINE'

# Testing if encryption and decryption processes work on test string and on given file
print(tools.cbcDecrypt(tools.cbcEncrypt(tools.pkcs7Padding(test, tools.BLOCK_SIZE), key), key))
print()

with open("10/10.txt", "r") as f:
    text = b64decode(f.read())
plaintext = tools.cbcDecrypt(text, key)
print(bytes(plaintext).decode("utf-8"))