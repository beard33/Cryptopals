import base64
import binascii

given = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
target = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

x = base64.b64encode(binascii.unhexlify(given))
print(x)
if x != target:
    print("Error in conversion")
else:
    print("Conversion correct")