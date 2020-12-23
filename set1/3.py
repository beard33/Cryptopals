import binascii
import utils.tools as tools

encoded = binascii.unhexlify(b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

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

    return bytes(pt).decode("utf-8"), probKey

print(breakSingleXor(encoded))
