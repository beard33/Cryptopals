import binascii
import base64
import utils.tools as tools

MAX_KEY_SIZE = 40

def findKeyElement(ciphertext):
    bestScore = -1

    for i in range(0,256):
        key = i.to_bytes(1,'big')*len(ciphertext)
        plaintext = tools.singleXOR(ciphertext,key)
        score = tools.scorePlaintext(plaintext)
        if score > bestScore:
            bestScore = score
            probKey = i
    
    return probKey


def hammingDistance(string1, string2):
    if len(string1) != len(string2):
        print("Error in strings length")
        exit(1)

    distance = 0
    x = zip(string1, string2)

    for i,j in x:
        distance += bin(i ^ j).count('1')

    return distance

# test = b'this is a test'
# test1 = b'wokka wokka!!!'

# HD between test and test1 should be 37
# print(hammingDistance(test, test1))

def findKeySize(ciphertext):
    bestDistance = 9999.99
    distance = 0

    for keyLen in range(2,MAX_KEY_SIZE):
        for i in range (0,10):
            a = ciphertext[i*keyLen : (i+1)*keyLen]
            b = ciphertext[(i+1)*keyLen : (i+2)*keyLen]
            distance += hammingDistance(a,b)
        
        normalizedDistance = (distance / keyLen / 10)
        if (normalizedDistance < bestDistance):
            bestDistance = normalizedDistance
            keySize = keyLen

        distance = 0
    
    return keySize

def findBlockKey(ciphertext, column, keyLen):
    block = []
    for row in range(0, int(len(ciphertext)/keyLen)):
        block.append(ciphertext[row*keyLen+column])

    return findKeyElement(block)

def findKey(ciphertext):
    keyLen = findKeySize(ciphertext)
    key = []
    
    for i in range (0,keyLen):
        key.append(findBlockKey(ciphertext, i, keyLen))
    
    return bytes(key)


with open("6/file.txt") as f:
    text = base64.b64decode(f.read())
print('Possible Key size: ' + str(findKeySize(text)))
key = findKey(text)
print('Key: ', bytes(key).decode("utf-8"))
print("------------------------------------")
plaintext = tools.repeatingXor(text, key)
print(bytes(plaintext).decode("utf-8"))