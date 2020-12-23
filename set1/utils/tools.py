FREQUENCY = {
   "e": 13, 
   "t": 9.1, 
   "a": 8.2,
   "o": 7.5, 
   "i": 7,
   "n": 6.7, 
   "s": 6.3, 
   "h": 6.1, 
   "r": 6, 
   "d": 4.3,
   "l": 4,
   "u": 2.8,
   "c": 2.8,
   "m": 2.4,
   "'":2,
   " ":2
}

def singleXOR(str1, str2):
    if len(str1) != len(str2):
        print("Error in strings length")
        exit(1)

    x = zip(str1, str2)
    res = []

    for i,j in x:
        res.append(i ^ j)
    return bytes(res)

def scorePlaintext(plaintext):
    score = 0
    for letter in plaintext:
        if chr(letter) in FREQUENCY:
            score += FREQUENCY[chr(letter)]
    
    return score
   
def repeatingXor(text, key):
    out = []
    for i, char in enumerate(text):
        out.append(char ^ key[i % len(key)])
    return out