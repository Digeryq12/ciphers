bacons_cipher = {
    'a': '00000',
    'b': '00001',
    'c': '00010',
    'd': '00011',
    'e': '00100',
    'f': '00101',
    'g': '00110',
    'h': '00111',
    'i': '01000',
    'j': '01001',
    'k': '01010',
    'l': '01011',
    'm': '01100',
    'n': '01101',
    'o': '01110',
    'p': '01111',
    'q': '10000',
    'r': '10001',
    's': '10010',
    't': '10011',
    'u': '10100',
    'v': '10101',
    'w': '10110',
    'x': '10111',
    'y': '11000',
    'z': '11001'
}

binary_repr_letters = {
    "0": "a",
    "1": "b"
}

def encode(text):
    encoded_text = ""
    text = text.lower().replace(" ", "")

    for character in text:
        encoded_character = ""

        try:
            binary = bacons_cipher[character]
        except:
            encoded_character = character
        else:
            for digit in binary:
                encoded_character += binary_repr_letters[digit]
        
        encoded_text += encoded_character + " "

    print(encoded_text)

def decode(text):
    decoded_text = ""
    encoded_characters = text.split()

    for character in encoded_characters:
        bin_character = ""
        decoded_character = ""

        for sub_character in character:
            for d in binary_repr_letters.keys():
                if binary_repr_letters[d] == sub_character:
                    decoded_bin = d
                    break
            
            bin_character += decoded_bin
            decoded_bin = ""

        for b in bacons_cipher.keys():
            if bacons_cipher[b] == bin_character:
                decoded_character = b
        
        decoded_text += decoded_character

    print(decoded_text)

original_text = input("Text: ")
method = input("Encode/Decode: ")

if method.lower() == "encode":
    encode(original_text)
elif method.lower() == "decode":
    decode(original_text)
else:
    print("Invalid method.")