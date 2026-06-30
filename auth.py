MASTER_PASSWORD = "admin123"

PIN = "1234"


def check_login(password):

    return password == MASTER_PASSWORD


def check_pin(pin):

    return pin == PIN