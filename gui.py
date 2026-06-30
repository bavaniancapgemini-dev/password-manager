from tkinter import *
from tkinter import messagebox
import pyperclip
import time

from auth import *
from generator import generate_password
from database import *
from security import *

create_table()

show_password = False
dark_mode = True


def update_clock():

    current = time.strftime("%H:%M:%S")

    clock_label.config(
        text=current
    )

    clock_label.after(
        1000,
        update_clock
    )


def update_counter():

    data = view_passwords_db()

    total = len(data)

    counter_label.config(
        text=f"Stored Passwords\n{total}"
    )


def toggle_theme():

    global dark_mode

    if dark_mode:

        window.config(bg="white")

        output.config(
            bg="white",
            fg="black"
        )

        dark_mode = False

    else:

        window.config(bg="#0a0f1f")

        output.config(
            bg="#1a1a1a",
            fg="lime"
        )

        dark_mode = True


def open_main_app():

    global window
    global website_entry
    global username_entry
    global password_entry
    global category_entry
    global notes_entry
    global output
    global clock_label
    global counter_label

    window = Tk()

    window.title(
        "CYBER VAULT v16.0"
    )

    window.geometry(
        "1200x900"
    )

    window.config(
        bg="#0a0f1f"
    )

    sidebar = Frame(

        window,

        bg="#111827",

        width=160

    )

    sidebar.pack(
        side=LEFT,
        fill=Y
    )
    sidebar.pack_propagate(False)
    

    logo = Label(

        sidebar,

        text="CYBER\nVAULT",

        bg="#111827",

        fg="cyan",

        font=("Arial", 28, "bold")

    )

    logo.pack(pady=20)

    counter_label = Label(

        sidebar,

        text="Stored Passwords\n0",

        bg="#111827",

        fg="white",

        font=("Arial", 14, "bold")

    )

    counter_label.pack(pady=20)

    clock_label = Label(

        sidebar,

        text="",

        bg="#111827",

        fg="lime",

        font=("Arial", 16, "bold")

    )

    clock_label.pack(pady=20)

    update_clock()

    main_frame = Frame(

        window,

        bg="#0a0f1f"

    )

    main_frame.pack(
        side=LEFT,
        fill=BOTH,
        expand=True,
        padx=30,
        pady=20
    )

    title = Label(

        main_frame,

        text="Password Manager",

        font=("Arial", 26, "bold"),

        bg="#0a0f1f",

        fg="white"

    )

    title.pack(pady=10)

    website_label = Label(

        main_frame,

        text="Website",

        bg="#0a0f1f",

        fg="white",

        font=("Arial", 12)

    )

    website_label.pack()

    website_entry = Entry(

        main_frame,

        width=45,

        font=("Arial", 12)

    )

    website_entry.pack(pady=5)

    username_label = Label(

        main_frame,

        text="Username",

        bg="#0a0f1f",

        fg="white",

        font=("Arial", 12)

    )

    username_label.pack()

    username_entry = Entry(

        main_frame,

        width=45,

        font=("Arial", 12)

    )

    username_entry.pack(pady=5)

    password_label = Label(

        main_frame,

        text="Password",

        bg="#0a0f1f",

        fg="white",

        font=("Arial", 12)

    )

    password_label.pack()

    password_entry = Entry(

        main_frame,

        width=45,

        show="*",

        font=("Arial", 12)

    )

    password_entry.pack(pady=5)

    category_label = Label(

        main_frame,

        text="Category",

        bg="#0a0f1f",

        fg="white",

        font=("Arial", 12)

    )

    category_label.pack()

    category_entry = Entry(

        main_frame,

        width=45,

        font=("Arial", 12)

    )

    category_entry.pack(pady=5)

    notes_label = Label(

        main_frame,

        text="Notes",

        bg="#0a0f1f",

        fg="white",

        font=("Arial", 12)

    )

    notes_label.pack()

    notes_entry = Entry(

        main_frame,

        width=45,

        font=("Arial", 12)

    )

    notes_entry.pack(pady=5)

    output = Text(

        main_frame,

        height=12,

        width=70,

        bg="#1a1a1a",

        fg="lime",

        font=("Consolas", 10)

    )

    output.pack(pady=15)

    button_frame = Frame(

        main_frame,

        bg="#0a0f1f"

    )

    button_frame.pack()

    Button(

        button_frame,

        text="Save Password",

        command=save_password,

        bg="green",

        fg="white",

        width=20

    ).grid(row=0, column=0, padx=5, pady=5)

    Button(

        button_frame,

        text="View Passwords",

        command=view_passwords,

        bg="blue",

        fg="white",

        width=20

    ).grid(row=0, column=1, padx=5, pady=5)

    Button(

        button_frame,

        text="Search Password",

        command=search_password,

        bg="orange",

        fg="white",

        width=20

    ).grid(row=1, column=0, padx=5, pady=5)

    Button(

        button_frame,

        text="Delete Password",

        command=delete_password_gui,

        bg="red",

        fg="white",

        width=20

    ).grid(row=1, column=1, padx=5, pady=5)

    Button(

        button_frame,

        text="Generate Password",

        command=generate_password_gui,

        bg="purple",

        fg="white",

        width=20

    ).grid(row=2, column=0, padx=5, pady=5)

    Button(

        button_frame,

        text="Copy Password",

        command=copy_password,

        bg="brown",

        fg="white",

        width=20

    ).grid(row=2, column=1, padx=5, pady=5)

    Button(

        button_frame,

        text="Show / Hide",

        command=toggle_password,

        bg="gray",

        fg="white",

        width=20

    ).grid(row=3, column=0, padx=5, pady=5)

    Button(

        button_frame,

        text="Clear Fields",

        command=clear_fields,

        bg="black",

        fg="white",

        width=20

    ).grid(row=3, column=1, padx=5, pady=5)

    Button(

        button_frame,

        text="Theme Switch",

        command=toggle_theme,

        bg="cyan",

        fg="black",

        width=20

    ).grid(row=4, column=0, padx=5, pady=5)

    update_counter()

    window.mainloop()


def toggle_password():

    global show_password

    if show_password:

        password_entry.config(
            show="*"
        )

        show_password = False

    else:

        password_entry.config(
            show=""
        )

        show_password = True


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

    update_counter()

    messagebox.showinfo(

        "Saved",

        "Password Saved"

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

            f"Website : {row[1]}\n"

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

            f"Notes   : {row[5]}\n"

        )

        output.insert(

            END,

            "-----------------------------\n"

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

    for row in data:

        decrypted = decrypt_password(
            row[3]
        )

        output.insert(

            END,

            f"Website : {row[1]}\n"

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

            "-----------------------------\n"

        )


def delete_password_gui():

    website = website_entry.get()

    delete_password_db(
        website
    )

    update_counter()

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


login_window = Tk()

login_window.title(
    "Cyber Vault Login"
)

login_window.geometry(
    "450x350"
)

login_window.config(
    bg="#0a0f1f"
)

title = Label(

    login_window,

    text="CYBER VAULT",

    font=("Arial", 28, "bold"),

    bg="#0a0f1f",

    fg="cyan"

)

title.pack(pady=30)

password_label = Label(

    login_window,

    text="Master Password",

    bg="#0a0f1f",

    fg="white",

    font=("Arial", 14)

)

password_label.pack(pady=10)

login_password_entry = Entry(

    login_window,

    show="*",

    width=30,

    font=("Arial", 14)

)

login_password_entry.pack(pady=10)

login_button = Button(

    login_window,

    text="LOGIN",

    command=login,

    bg="green",

    fg="white",

    width=20,

    font=("Arial", 12, "bold")

)

login_button.pack(pady=20)

login_window.mainloop()