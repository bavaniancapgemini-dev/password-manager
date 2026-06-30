MASTER_PASSWORD = "admin123"


def check_login(password):

    if password == MASTER_PASSWORD:

        return True

    else:

        return False