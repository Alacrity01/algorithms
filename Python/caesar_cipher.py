alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift) % len(alphabet)
            new_letter = alphabet[new_index]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")
    return cipher_text


def decrypt(cipher_text, shift):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            new_index = alphabet.index(letter) - shift
            new_letter = alphabet[new_index]
            plain_text += new_letter
        else:
            plain_text += letter

    print(f"The decoded text is {plain_text}")
    return plain_text


complete = False
while not complete:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        complete = True
        if direction == "encode":
            cipher_text = encrypt(text, shift)
            # print(
            #     f"\tTesting decrypt function on {cipher_text} with shift = {shift} ...")
            plain_text = decrypt(cipher_text, shift)
        else:  # direction == "decode"
            plain_text = decrypt(text, shift)
    else:  # invalid choice for direction
        print("Please retry using either 'encode' or 'decode'.")
