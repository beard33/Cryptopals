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

def detectSingleXOR():
    f = open("4/enc.txt", "r")
    bestScore = -1
    lines = f.read().splitlines()
    for line in lines:
        text, probKey,score = breakSingleXor(binascii.unhexlify(line))
        if score > bestScore:
            pt = text
            key = probKey
            bestScore = score
    return bytes(pt).decode('utf-8'), key, round(bestScore,2)

print(detectSingleXOR())
