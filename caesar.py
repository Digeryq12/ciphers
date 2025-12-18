alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(text, sh, meth):
    result = ""

    for char in text:
        is_uppercase = char.isupper()
        char = char.lower()

        try:
            index = alphabet.index(char)
        except:
            result += char
        else:
            if meth == "cipher":

                if (index + sh) > (len(alphabet) - 1):
                    sh = (index + sh) % len(alphabet)
                    l = alphabet[sh]
                else:
                    l = alphabet[index + sh]
            
            elif meth == "decipher":

                if (index - sh) < 0:
                    sh = len(alphabet) + (index - sh)
                    l = alphabet[sh]
                else:
                    l = alphabet[index - sh]

            else:
                print("Invalid method.")

            if is_uppercase:
                l = l.upper()

            result += l

    return result

if __name__ == "__main__":

    method = input("Cipher/Decipher: ").lower()
    plaintext = input("Plaintext: ")
    shift = input("Shift: ")
    output = ""

    try:
        shift = int(shift)
    except:
        print("Invalid shift.")
    else:
        output = caesar(plaintext, shift, method)
        print(output)
