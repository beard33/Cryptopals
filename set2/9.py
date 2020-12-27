import utils.tools as tools

string = b'YELLOW SUBMARINE'
target = b'YELLOW SUBMARINE\x04\x04\x04\x04'

if target == tools.pkcs7Padding(string, 20):
    print("OK")
else:
    print("Wrong padding")