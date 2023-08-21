def vigenere_encrypt(plaintext, keyword):
    encrypted_text = ""
    keyword_repeated = ''
    keyword_index = 0

    # Repeat the keyword to match the length of the plaintext
    for char in plaintext:
        if char.isalpha():
            keyword_repeated += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)

    # Encrypt the plaintext
    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():
            shift = ord(k.lower()) - ord('a')
            if p.isupper():
                encrypted_text += chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(p) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += p

    return encrypted_text

def vigenere_decrypt(encrypted_text, keyword):
    decrypted_text = ""
    keyword_repeated = ''
    keyword_index = 0

    # Repeat the keyword to match the length of the encrypted_text
    for char in encrypted_text:
        if char.isalpha():
            keyword_repeated += keyword[keyword_index]
            keyword_index = (keyword_index + 1) % len(keyword)

    # Decrypt the encrypted_text
    for e, k in zip(encrypted_text, keyword_repeated):
        if e.isalpha():
            shift = ord(k.lower()) - ord('a')
            if e.isupper():
                decrypted_text += chr((ord(e) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(e) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += e

    return decrypted_text

# Example usage:
plaintext = "HELLO WORLD"
keyword = "KEY"
encrypted = vigenere_encrypt(plaintext, keyword)
decrypted = vigenere_decrypt(encrypted, keyword)
print(f"Original Text: {plaintext}")
print(f"Encrypted Text: {encrypted}")
print(f"Decrypted Text: {decrypted}")
