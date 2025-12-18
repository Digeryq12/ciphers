# Requires caesar.py

from caesar import alphabet
from caesar import caesar

def vigenere(text, k, meth):
    i = 0
    res = ""

    for char in text:
        cc = ""
        shift = alphabet.index(k[i])

        cc = caesar(char, shift, meth)
        if cc == None:
            return

        res += cc

        if cc.lower() in alphabet:
            i += 1
            if i > len(k) - 1:
                i = 0

    print("Ciphertext: " + res)

key_valid = True
method = input("Encrypt/Decrypt: ")
key = input("Key: ").lower()
plaintext = input("Plaintext: ")

for l in key:
    if l not in alphabet:
        key_valid = False

if key_valid:
    vigenere(plaintext, key, method.lower())
else:
    print("Invalid key.")