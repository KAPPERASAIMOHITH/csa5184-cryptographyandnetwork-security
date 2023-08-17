def caesar_cipher(text, key):
    result = []
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    text = input("Enter the text: ")

    for key in range(1, 26):
        encrypted_text = caesar_cipher(text, key)
        print(f"Key = {key}: {encrypted_text}")

if __name__ == "__main__":
    main()
#output"'
Enter the text: helloworld
Key = 1: ifmmpxpsme
Key = 2: jgnnqyqtnf
Key = 3: khoorzruog
Key = 4: lippsasvph
Key = 5: mjqqtbtwqi
Key = 6: nkrrucuxrj
Key = 7: olssvdvysk
Key = 8: pmttwewztl
Key = 9: qnuuxfxaum
Key = 10: rovvygybvn
Key = 11: spwwzhzcwo
Key = 12: tqxxaiadxp
Key = 13: uryybjbeyq
Key = 14: vszzckcfzr
Key = 15: wtaadldgas
Key = 16: xubbemehbt
Key = 17: yvccfnficu
Key = 18: zwddgogjdv
Key = 19: axeehphkew
Key = 20: byffiqilfx
Key = 21: czggjrjmgy
Key = 22: dahhksknhz
Key = 23: ebiiltloia
Key = 24: fcjjmumpjb
Key = 25: gdkknvnqkc"'
