from database import view_passwords_db

def get_total_passwords(owner):

    data = view_passwords_db(owner)

    return len(data)