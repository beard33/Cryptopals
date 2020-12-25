# Implement CBC mode for AES-128
import utils.tools as tools
from base64 import b64decode, b64encode
from Crypto.Cipher import AES

BLOCK_SIZE = 16

def cbcEncrypt(plaintext, key, IV = b'\x00'*BLOCK_SIZE):
    assert len(key) == 16 and len(IV) == 16, "Key and IV must be 16 bytes long"
    ciphertext = []
    cipher = AES.new(key, AES.MODE_ECB)
    paddedPt = tools.pkcs7Padding(plaintext, BLOCK_SIZE)
    firstBlock = cipher.encrypt(tools.singleXOR(IV, paddedPt[ :BLOCK_SIZE]))
    ciphertext += firstBlock
    previousBlock = firstBlock
    for i in range(BLOCK_SIZE,len(plaintext), BLOCK_SIZE):
        block = cipher.encrypt(tools.singleXOR(previousBlock, paddedPt[i : i+BLOCK_SIZE]))
        previousBlock = block
        ciphertext += block

    return bytes(ciphertext)


def cbcDecrypt(ciphertext, key, IV = b'\x00'*BLOCK_SIZE):
    assert len(key) == 16 and len(IV) == 16, "Key and IV must be 16 bytes long"
    plaintext = []
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(len(ciphertext), BLOCK_SIZE, -BLOCK_SIZE):
        block = cipher.decrypt(ciphertext[i-BLOCK_SIZE : i])
        plaintext.insert(0, tools.singleXOR(block, ciphertext[i-2*BLOCK_SIZE : i - BLOCK_SIZE]))

    plaintext.insert(0, tools.singleXOR(cipher.decrypt(ciphertext[:BLOCK_SIZE]), IV))

    return b''.join(plaintext)

with open("10/10.txt", "r") as f:
    text = b64decode(f.read())
key = b'YELLOW SUBMARINE'


plaintext = cbcDecrypt(text, key)
print(bytes(plaintext).decode("utf-8"))