import random as rd
import string as st

if __name__ == '__main__':
    print('Welcome to the PyPassword Generator!')

    n_of_letters = 0
    n_of_symbols = 0
    n_of_numbers = 0

    while(1):
        try:
            n_of_letters = int(input('How many letters would you like in your password?\n> '))
            break
        except ValueError:
            print('You must enter a valid number.')

    while(1):
        try:
            n_of_symbols = int(input('How many symbols would you like in your password?\n> '))
            break
        except ValueError:
            print('You must enter a valid number.')

    while(1):
        try:
            n_of_numbers = int(input('How many numbers would you like in your password?\n> '))
            break
        except ValueError:
            print('You must enter a valid number.')

    password_characters = []

    for letter in range(1, n_of_letters + 1):
        password_characters.append(str(rd.choice(st.ascii_letters)))

    for symbol in range(1, n_of_symbols + 1):
        password_characters.append(str(rd.choice(st.punctuation)))

    for number in range(1, n_of_numbers + 1):
        password_characters.append(str(rd.randint(0, 9)))

    rd.shuffle(password_characters)
    new_password = ''.join(password_characters)
    
    print(f'\nHere is your password: {new_password}\n')