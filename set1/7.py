from base64 import b64decode, b64encode
from Crypto.Cipher import AES


KEY = b'YELLOW SUBMARINE'
f = open("7/text.txt")
ciphertext = b64decode(f.read())

decipher = AES.new(KEY, AES.MODE_ECB)
print(bytes(decipher.decrypt(ciphertext)).decode("utf-8"))