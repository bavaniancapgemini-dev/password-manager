def update_password(
    passwords,
    website,
    new_password
):

    found = False

    for i in range(len(passwords)):

        if website.lower() in passwords[i].lower():

            parts = passwords[i].split("|")

            username_part = parts[1]

            passwords[i] = (

                parts[0]
                + "|"
                + username_part
                + "| Password: "
                + new_password

            )

            found = True

            print("Password Updated")

            break

    if found == False:

        print("Website Not Found")