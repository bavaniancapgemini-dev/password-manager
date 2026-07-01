MASTER_PASSWORD = "admin123"


def check_login(password):

    if password == MASTER_PASSWORD:

        return True

    else:

        return False
    
MASTER_PASSWORD = "admin123"

def check_login(password):

    return password == MASTER_PASSWORD