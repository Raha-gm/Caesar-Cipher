# The English alphabet
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x", "y", "z"
]


# Encrypt the text
def encode(text, shift):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = (position + shift) % 26
        new_text += alphabet[new_position]
    print(new_text)


# Decrypt the text
def decode(text, shift):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = (position - shift) % 26
        new_text += alphabet[new_position]
    print(new_text)


# Main program
while True:
    text = input("Enter your text: ").lower()
    shift = int(input("Enter your shift: "))
    direction = input("Encode or decode: ").lower()

    if direction == "encode":
        encode(text, shift)
    elif direction == "decode":
        decode(text, shift)