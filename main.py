from password_utils import show_passwords
from storage import save_passwords, load_passwords
from search import search_password
from generator import generate_password
from utils import title


passwords = load_passwords()


while True:

    title()

    print("1. Save Password")
    print("2. View Passwords")
    print("3. Search Account")
    print("4. Generate Password")
    print("5. Exit")

    choice = input("Choose: ")


    if choice == "1":

        website = input("Website: ")

        username = input("Username: ")

        password = input("Password: ")

        data = (
            "Website: " + website +
            " | Username: " + username +
            " | Password: " + password
        )

        passwords.append(data)

        save_passwords(passwords)

        print("Password Saved")


    elif choice == "2":

        show_passwords(passwords)


    elif choice == "3":

        website = input("Enter website to search: ")

        search_password(passwords, website)


    elif choice == "4":

        password = generate_password()

        print("Generated Password:", password)


    elif choice == "5":

        break


    else:

        print("Invalid Choice")