def save_passwords(passwords):

    file = open("passwords.txt", "w")

    for item in passwords:

        file.write(item + "\n")

    file.close()

def load_passwords():

    try:

        file = open("passwords.txt", "r")

        passwords = file.read().splitlines()

        file.close()

        return passwords

    except:

        return []