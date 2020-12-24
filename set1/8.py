import binascii

BLOCK_LEN = 16

def detectEcbMode(ciphertext):
    seen = {}
    for i in range(0,len(ciphertext), BLOCK_LEN):
        block = ciphertext[i : i+BLOCK_LEN]
        if block in seen:
            return True
        seen[block] = True
    
    return False

with open("8/text.txt") as f:
    text = f.read().splitlines()
for line in text:
    if detectEcbMode(binascii.unhexlify(line)):
        print("Found ECB at line", text.index(line) + 1)

