from Crypto.Cipher import AES

BLOCK_SIZE = 16

def pkcs7Padding(plaintext, blockSize=BLOCK_SIZE):
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

def cbcEncrypt(plaintext, key, IV = b'\x00'*BLOCK_SIZE):
    assert len(key) == 16 and len(IV) == 16, "Key and IV must be 16 bytes long"
    assert len(plaintext) % BLOCK_SIZE == 0, "Plaintext must be padded to blocksize"
    ciphertext = []
    cipher = AES.new(key, AES.MODE_ECB)
    previousBlock = cipher.encrypt(singleXOR(IV, plaintext[ :BLOCK_SIZE]))
    ciphertext += previousBlock
    for i in range(BLOCK_SIZE,len(plaintext), BLOCK_SIZE):
        block = cipher.encrypt(singleXOR(previousBlock, plaintext[i : i+BLOCK_SIZE]))
        previousBlock = block
        ciphertext += block

    return bytes(ciphertext)

def cbcDecrypt(ciphertext, key, IV = b'\x00'*BLOCK_SIZE):
    assert len(key) == 16 and len(IV) == 16, "Key and IV must be 16 bytes long"
    plaintext = []
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(len(ciphertext), BLOCK_SIZE, -BLOCK_SIZE):
        block = cipher.decrypt(ciphertext[i-BLOCK_SIZE : i])
        plaintext.insert(0, singleXOR(block, ciphertext[i-2*BLOCK_SIZE : i - BLOCK_SIZE]))

    plaintext.insert(0, singleXOR(cipher.decrypt(ciphertext[:BLOCK_SIZE]), IV))

    return b''.join(plaintext)

def ecbEncrypt(plaintext, key):
    assert len(plaintext) % BLOCK_SIZE == 0, "Plaintext must be padded to blocksize"
    return AES.new(key, AES.MODE_ECB).encrypt(plaintext)

def detectEcbMode(ciphertext):
    seen = {}
    for i in range(0,len(ciphertext), BLOCK_SIZE):
        block = ciphertext[i : i+BLOCK_SIZE]
        if block in seen:
            return True
        seen[block] = True
    
    return False