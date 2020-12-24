import binascii
import utils.tools as tools


def breakSingleXor(ciphertext):
    bestScore = -1

    for i in range(0,256):
        key = i.to_bytes(1,'big')*len(ciphertext)
        plaintext = tools.singleXOR(ciphertext,key)
        score = tools.scorePlaintext(plaintext)
        if score > bestScore:
            bestScore = score
            pt = plaintext
            probKey = chr(i)

    return pt, probKey, bestScore


with open("4/enc.txt", "r") as f:
    lines = f.read().splitlines()
bestScore = -1
for line in lines:
    text, probKey,score = breakSingleXor(binascii.unhexlify(line))
    if score > bestScore:
        pt = text
        key = probKey
        bestScore = score
print("Plaintext:", bytes(pt).decode('utf-8'), "KEY: ", key)

