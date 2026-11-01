# Repeat the alphabet to make shifting easier
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
] * 2

dir = int(input("Type the direction (1: encrypt, 2: decrypt):\n"))


# Encrypt the text
def encrypt(txt, shift):
    encrypted_txt = ""
    for letter in txt:
        if letter in alphabet[:26]:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            encrypted_txt += alphabet[new_position]
        else:
            encrypted_txt += letter
    print(encrypted_txt)


# Decrypt the text
def decrypt(txt, shift):
    decrypt_txt = ""
    for letter in txt:
        if letter in alphabet[:26]:
            position = alphabet.index(letter)
            new_position = (position - shift) % 26
            decrypt_txt += alphabet[new_position]
        else:
            decrypt_txt += letter
    print(decrypt_txt)


# Main program
while True:
    if dir == 1:
        txt = input("Type the text to be encrypted:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(txt, shift)

    elif dir == 2:
        txt = input("Type the text to be decrypted:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(txt, shift)

    else:
        print("Invalid direction!")
        break