def monoalphabetic_substitution(text, substitution_key):
    result = []
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            index = ord(char) - shift
            encrypted_char = substitution_key[index]
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    substitution_key = "QWERTYUIOPASDFGHJKLZXCVBNM"  # Example substitution key
    text = input("Enter the text: ")

    encrypted_text = monoalphabetic_substitution(text, substitution_key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
#output
Enter the text: helloworld
Encrypted text: ITSSGVGKSR
