alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift):
    cipher_text = ""
    for _ in plain_text:
        try:
            cipher_text += alphabet[alphabet.index(_) + shift %
                                    (len(alphabet) - 1)]
        except:
            cipher_text += _
    print(f"The encoded text is mjqqt{cipher_text}")


encrypt(text, shift)  # Call encrypt function to test
# e.g. plain_text = "hello", shift = 5 -> cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
