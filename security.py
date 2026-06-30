from cryptography.fernet import Fernet

KEY = Fernet.generate_key()

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