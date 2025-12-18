alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

a = 5
b = 8


def affine(text, method):
    result = ""

    for character in text:
        character_uppercase = character.isupper()
        character = character.lower()

        try:
            x = alphabet.index(character)
        except:
            res_character = character
        else:
            if method == "encrypt":
                res_character = alphabet[(a * x + b) % len(alphabet)]
            elif method == "decrypt":
                res_character = alphabet[21 * (x - b) % 26]
            else:
                print("Invalid method.")
        
        if character_uppercase:
            res_character = res_character.upper()
        
        result += res_character

    print(result)


input_method = input("Encrypt/Decrypt: ")
original_text = input("Text: ")

affine(original_text, input_method)