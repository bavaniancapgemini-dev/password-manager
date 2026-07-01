from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():

    if not os.path.exists(KEY_FILE):

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:

            file.write(key)

    else:

        with open(KEY_FILE, "rb") as file:

            key = file.read()

    return key

KEY = load_key()

fernet = Fernet(KEY)

def encrypt_password(password):

    encrypted = fernet.encrypt(
        password.encode()
    )

    return encrypted.decode()

def decrypt_password(password):

    decrypted = fernet.decrypt(
        password.encode()
    )

    return decrypted.decode()