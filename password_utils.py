from security import *
def show_passwords(passwords):

    for data in passwords:

        parts = data.split("|")

        encrypted_password = (
            parts[2]
            .replace(
                " Password: ",
                ""
            )
            .strip()
        )

        decrypted = decrypt_password(
            encrypted_password
        )

        print(

            parts[0]
            + "|"
            + parts[1]
            + "| Password: "
            + decrypted

        )