alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def substitution(text, letters, meth):
    ciphertext_alphabet = []
    ciphertext = ""

    for letter in letters:
        ciphertext_alphabet.append(letter)

    for char in text:
        char_uppercase = char.isupper()
        char = char.lower()

        if meth == "encrypt":
            if char in alphabet:
                ind = alphabet.index(char)
                char = ciphertext_alphabet[ind]
        elif meth == "decrypt":
            if char in ciphertext_alphabet:
                ind = ciphertext_alphabet.index(char)
                char = alphabet[ind]
        else:
            print("Invalid method.")
            return
        
        if char_uppercase:
            char = char.upper()

        ciphertext += char
    
    print(ciphertext)

method = input("Encrypt/Decrypt: ").lower()
ciphertext_alphabet_letters = input("Ciphertext alphabet: ")
if len(ciphertext_alphabet_letters) == len(alphabet):
    plaintext = input("Plaintext: ")
    substitution(plaintext, ciphertext_alphabet_letters, method)
else:
    print("The length of the ciphertext alphabet must match the english alphabet's.")