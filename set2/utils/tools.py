def pkcs7Padding(plaintext, blockSize):
    if blockSize > 256:
        print("PKCS7 can only pad up to 256")

    padLen = blockSize - (len(plaintext) % blockSize)
    padded = list(plaintext)
    if padLen == 0:
        padLen = blockSize
    pad = padLen.to_bytes(1, 'big')
    for _ in range (0,padLen):
        padded += pad

    return bytes(padded)

def singleXOR(str1, str2):
    if len(str1) != len(str2):
        print("Error in strings length")
        exit(1)

    res = []
    for i,j in zip(str1, str2):
        res.append(i ^ j)
    return bytes(res)