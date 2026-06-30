from tkinter import *
from tkinter import messagebox
import pyperclip

from auth import *
from generator import generate_password
from database import *
from security import *

create_table()

show_password = False


def open_main_app():

    global window
    global website_entry
    global username_entry
    global password_entry
    global category_entry
    global notes_entry
    global output
    global show_password

    window = Tk()

    window.title(
        "Password Manager v9.0"
    )

    window.geometry(
        "700x950"
    )

    window.config(
        bg="#1e1e1e"
    )

    title = Label(

        window,

        text="Password Manager v9.0",

        font=("Arial", 24, "bold"),

        bg="#1e1e1e",

        fg="white"

    )

    title.pack(pady=15)

    # WEBSITE

    website_label = Label(

        window,

        text="Website",

        bg="#1e1e1e",

        fg="white",

        font=("Arial", 12)

    )

    website_label.pack()

    website_entry = Entry(

        window,

        width=40,

        font=("Arial", 12)

    )

    website_entry.pack(pady=5)

    # USERNAME

    username_label = Label(

        window,

        text="Username",

        bg="#1e1e1e",

        fg="white",

        font=("Arial", 12)

    )

    username_label.pack()

    username_entry = Entry(

        window,

        width=40,

        font=("Arial", 12)

    )

    username_entry.pack(pady=5)

    # PASSWORD

    password_label = Label(

        window,

        text="Password",

        bg="#1e1e1e",

        fg="white",

        font=("Arial", 12)

    )

    password_label.pack()

    password_entry = Entry(

        window,

        width=40,

        show="*",

        font=("Arial", 12)

    )

    password_entry.pack(pady=5)

    # CATEGORY

    category_label = Label(

        window,

        text="Category",

        bg="#1e1e1e",

        fg="white",

        font=("Arial", 12)

    )

    category_label.pack()

    category_entry = Entry(

        window,

        width=40,

        font=("Arial", 12)

    )

    category_entry.pack(pady=5)

    # NOTES

    notes_label = Label(

        window,

        text="Notes",

        bg="#1e1e1e",

        fg="white",

        font=("Arial", 12)

    )

    notes_label.pack()

    notes_entry = Entry(

        window,

        width=40,

        font=("Arial", 12)

    )

    notes_entry.pack(pady=5)

    # OUTPUT BOX

    output = Text(

        window,

        height=12,

        width=65,

        bg="#2d2d2d",

        fg="white",

        font=("Arial", 10)

    )

    output.pack(pady=15)

    # BUTTONS

    save_button = Button(

        window,

        text="Save Password",

        command=save_password,

        bg="green",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    save_button.pack(pady=5)

    view_button = Button(

        window,

        text="View Passwords",

        command=view_passwords,

        bg="blue",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    view_button.pack(pady=5)

    search_button = Button(

        window,

        text="Search Password",

        command=search_password,

        bg="orange",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    search_button.pack(pady=5)

    delete_button = Button(

        window,

        text="Delete Password",

        command=delete_password_gui,

        bg="red",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    delete_button.pack(pady=5)

    generate_button = Button(

        window,

        text="Generate Password",

        command=generate_password_gui,

        bg="purple",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    generate_button.pack(pady=5)

    copy_button = Button(

        window,

        text="Copy Password",

        command=copy_password,

        bg="brown",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    copy_button.pack(pady=5)

    show_button = Button(

        window,

        text="Show / Hide Password",

        command=toggle_password,

        bg="gray",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    show_button.pack(pady=5)

    clear_button = Button(

        window,

        text="Clear Fields",

        command=clear_fields,

        bg="black",

        fg="white",

        width=25,

        font=("Arial", 11)

    )

    clear_button.pack(pady=5)

    window.mainloop()


def toggle_password():

    global show_password

    if show_password == False:

        password_entry.config(
            show=""
        )

        show_password = True

    else:

        password_entry.config(
            show="*"
        )

        show_password = False


def check_strength(password):

    if len(password) < 6:

        return "Weak"

    elif len(password) < 10:

        return "Medium"

    else:

        return "Strong"


def save_password():

    website = website_entry.get()

    username = username_entry.get()

    password = password_entry.get()

    category = category_entry.get()

    notes = notes_entry.get()

    strength = check_strength(
        password
    )

    encrypted = encrypt_password(
        password
    )

    save_password_db(

        website,

        username,

        encrypted,

        category,

        notes

    )

    messagebox.showinfo(

        "Saved",

        f"Password Saved\nStrength: {strength}"

    )


def view_passwords():

    output.delete(
        1.0,
        END
    )

    data = view_passwords_db()

    for row in data:

        decrypted = decrypt_password(
            row[3]
        )

        output.insert(

            END,

            f"Website: {row[1]}\n"

        )

        output.insert(

            END,

            f"Username: {row[2]}\n"

        )

        output.insert(

            END,

            f"Password: {decrypted}\n"

        )

        output.insert(

            END,

            f"Category: {row[4]}\n"

        )

        output.insert(

            END,

            f"Notes: {row[5]}\n"

        )

        output.insert(

            END,

            "----------------------\n"

        )


def search_password():

    output.delete(
        1.0,
        END
    )

    website = website_entry.get()

    data = search_password_db(
        website
    )

    if len(data) == 0:

        output.insert(
            END,
            "No password found.\n"
        )

    for row in data:

        decrypted = decrypt_password(
            row[3]
        )

        output.insert(

            END,

            f"Website: {row[1]}\n"

        )

        output.insert(

            END,

            f"Username: {row[2]}\n"

        )

        output.insert(

            END,

            f"Password: {decrypted}\n"

        )

        output.insert(

            END,

            f"Category: {row[4]}\n"

        )

        output.insert(

            END,

            f"Notes: {row[5]}\n"

        )

        output.insert(

            END,

            "----------------------\n"

        )


def delete_password_gui():

    website = website_entry.get()

    delete_password_db(
        website
    )

    messagebox.showinfo(

        "Deleted",

        "Password Deleted"

    )


def generate_password_gui():

    password_entry.delete(
        0,
        END
    )

    new_password = generate_password()

    password_entry.insert(
        0,
        new_password
    )


def clear_fields():

    website_entry.delete(
        0,
        END
    )

    username_entry.delete(
        0,
        END
    )

    password_entry.delete(
        0,
        END
    )

    category_entry.delete(
        0,
        END
    )

    notes_entry.delete(
        0,
        END
    )


def copy_password():

    password = password_entry.get()

    pyperclip.copy(
        password
    )

    messagebox.showinfo(

        "Copied",

        "Password Copied"

    )


def login():

    password = login_password_entry.get()

    if check_login(password):

        login_window.destroy()

        open_main_app()

    else:

        messagebox.showerror(

            "Error",

            "Wrong Password"

        )


# LOGIN WINDOW

login_window = Tk()

login_window.title(
    "Login"
)

login_window.geometry(
    "400x300"
)

login_window.config(
    bg="#1e1e1e"
)

title = Label(

    login_window,

    text="Password Manager Login",

    font=("Arial", 20, "bold"),

    bg="#1e1e1e",

    fg="white"

)

title.pack(pady=30)

password_label = Label(

    login_window,

    text="Master Password",

    bg="#1e1e1e",

    fg="white",

    font=("Arial", 12)

)

password_label.pack(pady=10)

login_password_entry = Entry(

    login_window,

    show="*",

    width=30,

    font=("Arial", 12)

)

login_password_entry.pack(pady=10)

login_button = Button(

    login_window,

    text="Login",

    command=login,

    bg="green",

    fg="white",

    width=20,

    font=("Arial", 12)

)

login_button.pack(pady=20)

login_window.mainloop()