# Password Generator Project
import random


def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    debugging = False
    if debugging == True:
        nr_letters = 4
        nr_symbols = 2
        nr_numbers = 2
    else:
        nr_letters = int(
            input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Easy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    password = []
    [password.append(random.choice(letters)) for _ in range(nr_letters)]
    [password.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password.append(random.choice(numbers)) for _ in range(nr_numbers)]
    random.shuffle(password)
    password = ''.join(password)
    return password


pw = generatePassword()
print(pw)
