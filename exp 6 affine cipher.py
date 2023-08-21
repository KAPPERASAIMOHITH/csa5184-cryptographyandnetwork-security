def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                P = (mod_inverse(a, 26) * (ord(char) - ord('A') - b)) % 26
                plaintext += chr(P + ord('A'))
            else:
                P = (mod_inverse(a, 26) * (ord(char) - ord('a') - b)) % 26
                plaintext += chr(P + ord('a'))
        else:
            plaintext += char
    return plaintext

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def break_affine(ciphertext):
    E = 4
    T = 19
    B = ord('B') - ord('A')
    U = ord('U') - ord('A')

    valid_as = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    potential_keys = []

    for a in valid_as:
        b_B = (B - a * E) % 26
        b_U = (U - a * T) % 26

        if b_B == b_U:
            potential_keys.append((a, b_B))

    for (a, b) in potential_keys:
        decrypted_text = affine_decrypt(ciphertext, a, b)
        print(f"Key (a={a}, b={b}): {decrypted_text}")

ciphertext = "YOUR_CIPHERTEXT_HERE"
break_affine(ciphertext)
Key (a=3, b=15): DRTS_NPAGFSKFUK_GFSF

