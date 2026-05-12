def search_password(passwords, website):

    found = False

    for item in passwords:

        if website.lower() in item.lower():

            print(item)

            found = True

    if found == False:

        print("No account found")