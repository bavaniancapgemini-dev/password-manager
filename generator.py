import random
import string


def generate_password():

    characters = string.ascii_letters + string.digits + "!@#$%"

    password = ""

    for i in range(10):

        password += random.choice(characters)

    return password