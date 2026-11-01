# Repeat the alphabet to support shifting
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
] * 2


# Encrypt the text
def encrypt(txt, shift):
    encrypted_txt = ""
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position + shift
        encrypted_txt += alphabet[new_position]
    return encrypted_txt


# Decrypt the text
def decrypt(txt, shift):
    decrypt_txt = ""
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position - shift
        decrypt_txt += alphabet[new_position]
    return decrypt_txt


# Run the encryption or decryption process
def run():
    dir = int(dir_entry.get())
    txt = txt_entry.get().lower()
    shift = int(shift_entry.get())

    if dir == 1:
        output = encrypt(txt, shift)
    else:
        output = decrypt(txt, shift)

    result.config(text=f"Result: {output}")


# Font settings
FONT = ("Helvetica", 20, "bold")
RESULT_FONT = ("Helvetica", 14, "bold")

from tkinter import *

# Create the main window
root = Tk()
root.geometry("500x500")
root.title("Caesar Cipher")

# Direction selection
Label(
    root,
    text="1: Encrypt    2: Decrypt",
    fg="darkblue",
    font=FONT
).pack()

dir_entry = Entry(root, width=10, font=FONT)
dir_entry.pack(pady=15)

# Text input
Label(root, text="Text", fg="darkblue", font=FONT).pack()

txt_entry = Entry(root, width=15, font=FONT)
txt_entry.pack(pady=15)

# Shift input
Label(root, text="Shift Amount", fg="darkblue", font=FONT).pack()

shift_entry = Entry(root, width=10, font=FONT)
shift_entry.pack(pady=15)

# Run button
btn = Button(
    root,
    text="Run",
    bg="blue",
    fg="white",
    font=FONT,
    command=run
)
btn.pack(pady=10)

# Display the result
result = Label(root, text="", fg="darkblue", font=RESULT_FONT)
result.pack(pady=20)

# Start the application
root.mainloop()