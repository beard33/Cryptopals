import binascii

string1 = binascii.unhexlify(b'1c0111001f010100061a024b53535009181c')
string2 = binascii.unhexlify(b'686974207468652062756c6c277320657965')
target = binascii.unhexlify(b'746865206b696420646f6e277420706c6179')


def singleXOR(str1, str2):
    if len(str1) != len(str2):
        print("Error in strings length")
        exit(1)

    x = zip(str1, str2)
    res = []

    for i,j in x:
        res.append(i ^ j)
    print(bytes(res).decode("utf-8"))
    return bytes(res)


if singleXOR(string1, string2) != target:
    print("Error in conversion")
else:
    print("OK")



    
    