import getpass
from password_utils import show_passwords
from search import search_password
from generator import generate_password
from utils import title
from update import update_password
from checker import check_strength
from security import *
from database import *

master_password = "admin123"

login = getpass.getpass(
    "Enter Master Password: "
)

if login != master_password:

    print("Access Denied")

    exit()

create_table()


while True:

    title()

    print("1. Save Password")
    print("2. View Passwords")
    print("3. Search Account")
    print("4. Generate Password")
    print("5. Delete Password")
    print("6. Update Password")
    print("7. Check Password Strength")
    print("8. Exit")

    choice = input("Choose: ")


    if choice == "1":

        website = input("Website: ")

        username = input("Username: ")

        password = getpass.getpass("Password: ")

        encrypted_password = encrypt_password(password)

        data = (
            "Website: " + website +
            " | Username: " + username +
            " | Password: " + encrypted_password
        )

        save_password_db(website,username,encrypted_password)

        print("Password Saved")


    elif choice == "2":

        data = view_passwords_db()

        for row in data:

            decrypted = decrypt_password(row[3])

            print("Website:",row[1],"| Username:",row[2],"| Password:",decrypted)


    elif choice == "3":

        website = input("Enter website to search: ")

        data = search_password_db(website)

        for row in data:

            decrypted = decrypt_password(row[3])

            print("Website:",row[1],"| Username:",row[2],"| Password:",decrypted)


    elif choice == "4":

        password = generate_password()

        print("Generated Password:", password)

    elif choice == "5":

        website = input("Enter Website: ")

        delete_password_db(website)

        print("Password Deleted")


    elif choice == "6":

        website = input("Enter Website: ")

        new_password = input("Enter New Password: ")

        update_password(password,website,new_password)

    elif choice == "7":

        password = input("Enter Password: ")

        strength = check_strength(password)

        print("Password Strength:",strength)

    elif choice == "8":

        break

    else:

        print("Invalid Choice")