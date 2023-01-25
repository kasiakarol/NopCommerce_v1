import random


def random_login_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    login = ""
    for n in range(1, 8):
        login = login + letters[random.randint(1, len(letters) - 1)]
    for number in range(1, 4):
        login = login + (numbers[random.randint(1, len(numbers) - 1)])
    return login

