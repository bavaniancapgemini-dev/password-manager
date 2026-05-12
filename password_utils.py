def show_passwords(passwords):

    print("\n---- SAVED PASSWORDS ----")

    if len(passwords) == 0:

        print("No passwords saved")

    else:

        for item in passwords:

            print(item)