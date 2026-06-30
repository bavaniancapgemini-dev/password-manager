from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog

from datetime import datetime

import csv
import pyperclip
import shutil

from auth import *
from database import *
from generator import generate_password
from security import *

create_table()

dark_mode = True
show_password = False


# ---------------- MAIN APP ---------------- #

def open_main_app():

    global root
    global website_entry
    global username_entry
    global password_entry
    global category_entry
    global notes_entry
    global output
    global stats_label
    global theme_button

    root = Tk()

    root.title(
        "Password Manager v14.0"
    )

    root.geometry(
        "1250x750"
    )

    root.config(
        bg="#0d1117"
    )

    # ---------------- TOP BAR ---------------- #

    topbar = Frame(
        root,
        bg="#161b22",
        height=60
    )

    topbar.pack(
        fill=X
    )

    title = Label(

        topbar,

        text="🔐 PASSWORD MANAGER v14.0",

        bg="#161b22",

        fg="#00ffcc",

        font=("Arial", 22, "bold")

    )

    title.pack(
        side=LEFT,
        padx=20,
        pady=10
    )

    theme_button = Button(

        topbar,

        text="☀ Light Mode",

        command=toggle_theme,

        bg="#30363d",

        fg="white"

    )

    theme_button.pack(
        side=RIGHT,
        padx=20
    )

    # ---------------- NOTEBOOK ---------------- #

    notebook = ttk.Notebook(
        root
    )

    notebook.pack(
        fill=BOTH,
        expand=True
    )

    dashboard_tab = Frame(
        notebook,
        bg="#0d1117"
    )

    vault_tab = Frame(
        notebook,
        bg="#0d1117"
    )

    settings_tab = Frame(
        notebook,
        bg="#0d1117"
    )

    notebook.add(
        dashboard_tab,
        text="Dashboard"
    )

    notebook.add(
        vault_tab,
        text="Vault"
    )

    notebook.add(
        settings_tab,
        text="Settings"
    )

    # ---------------- DASHBOARD ---------------- #

    heading = Label(

        dashboard_tab,

        text="Cyber Security Vault",

        bg="#0d1117",

        fg="white",

        font=("Arial", 26, "bold")

    )

    heading.pack(pady=20)

    form = Frame(
        dashboard_tab,
        bg="#0d1117"
    )

    form.pack()

    Label(
        form,
        text="Website",
        bg="#0d1117",
        fg="white"
    ).grid(row=0, column=0, pady=10)

    website_entry = Entry(
        form,
        width=45
    )

    website_entry.grid(row=0, column=1)

    Label(
        form,
        text="Username",
        bg="#0d1117",
        fg="white"
    ).grid(row=1, column=0, pady=10)

    username_entry = Entry(
        form,
        width=45
    )

    username_entry.grid(row=1, column=1)

    Label(
        form,
        text="Password",
        bg="#0d1117",
        fg="white"
    ).grid(row=2, column=0, pady=10)

    password_entry = Entry(
        form,
        width=45,
        show="*"
    )

    password_entry.grid(row=2, column=1)

    Label(
        form,
        text="Category",
        bg="#0d1117",
        fg="white"
    ).grid(row=3, column=0, pady=10)

    category_entry = Entry(
        form,
        width=45
    )

    category_entry.grid(row=3, column=1)

    Label(
        form,
        text="Notes",
        bg="#0d1117",
        fg="white"
    ).grid(row=4, column=0, pady=10)

    notes_entry = Entry(
        form,
        width=45
    )

    notes_entry.grid(row=4, column=1)

    # ---------------- BUTTONS ---------------- #

    button_frame = Frame(
        dashboard_tab,
        bg="#0d1117"
    )

    button_frame.pack(pady=20)

    Button(

        button_frame,

        text="Save Password",

        command=save_password,

        bg="#238636",

        fg="white",

        width=18

    ).grid(row=0, column=0, padx=5)

    Button(

        button_frame,

        text="View Passwords",

        command=view_passwords,

        bg="#1f6feb",

        fg="white",

        width=18

    ).grid(row=0, column=1, padx=5)

    Button(

        button_frame,

        text="Generate Password",

        command=generate_password_gui,

        bg="#8957e5",

        fg="white",

        width=18

    ).grid(row=0, column=2, padx=5)

    Button(

        button_frame,

        text="Delete Password",

        command=delete_password_gui,

        bg="#f85149",

        fg="white",

        width=18

    ).grid(row=0, column=3, padx=5)

    Button(

        button_frame,

        text="Copy Password",

        command=copy_password,

        bg="#d29922",

        fg="black",

        width=18

    ).grid(row=1, column=0, pady=10)

    Button(

        button_frame,

        text="Show / Hide",

        command=toggle_password,

        bg="#30363d",

        fg="white",

        width=18

    ).grid(row=1, column=1)

    Button(

        button_frame,

        text="Export CSV",

        command=export_csv,

        bg="#ff7b72",

        fg="white",

        width=18

    ).grid(row=1, column=2)

    Button(

        button_frame,

        text="Backup DB",

        command=backup_database,

        bg="#00b4d8",

        fg="black",

        width=18

    ).grid(row=1, column=3)

    # ---------------- OUTPUT ---------------- #

    output = Text(

        dashboard_tab,

        width=120,

        height=18,

        bg="#161b22",

        fg="#00ffcc",

        font=("Consolas", 10)

    )

    output.pack(pady=20)

    # ---------------- VAULT TAB ---------------- #

    stats_label = Label(

        vault_tab,

        text=f"Saved Passwords: {total_passwords_db()}",

        bg="#0d1117",

        fg="yellow",

        font=("Arial", 22, "bold")

    )

    stats_label.pack(pady=50)

    Button(

        vault_tab,

        text="🔒 SECRET VAULT",

        command=secret_vault,

        bg="black",

        fg="#00ffcc",

        width=30,

        height=2,

        font=("Arial", 14, "bold")

    ).pack(pady=20)

    # ---------------- SETTINGS TAB ---------------- #

    Label(

        settings_tab,

        text="Security Settings",

        bg="#0d1117",

        fg="white",

        font=("Arial", 24, "bold")

    ).pack(pady=30)

    Button(

        settings_tab,

        text="PIN Lock",

        command=pin_lock,

        bg="#8957e5",

        fg="white",

        width=30,

        height=2

    ).pack(pady=10)

    Button(

        settings_tab,

        text="Auto Logout",

        command=auto_logout,

        bg="#f85149",

        fg="white",

        width=30,

        height=2

    ).pack(pady=10)

    root.mainloop()


# ---------------- FUNCTIONS ---------------- #

def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    category = category_entry.get()
    notes = notes_entry.get()

    encrypted = encrypt_password(
        password
    )

    created_at = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    save_password_db(

        website,
        username,
        encrypted,
        category,
        notes,
        created_at

    )

    stats_label.config(
        text=f"Saved Passwords: {total_passwords_db()}"
    )

    messagebox.showinfo(
        "Saved",
        "Password Saved"
    )

    clear_fields()


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

            f"""
Website : {row[1]}
Username: {row[2]}
Password: {decrypted}
Category: {row[4]}
Notes   : {row[5]}
Created : {row[6]}

-------------------------------------
"""

        )


def generate_password_gui():

    password_entry.delete(
        0,
        END
    )

    password_entry.insert(
        0,
        generate_password()
    )


def delete_password_gui():

    delete_password_db(
        website_entry.get()
    )

    messagebox.showinfo(
        "Deleted",
        "Password Deleted"
    )


def copy_password():

    pyperclip.copy(
        password_entry.get()
    )

    messagebox.showinfo(
        "Copied",
        "Password Copied"
    )


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


def clear_fields():

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    category_entry.delete(0, END)
    notes_entry.delete(0, END)


def export_csv():

    data = view_passwords_db()

    with open(

        "password_export.csv",

        "w",

        newline=""

    ) as file:

        writer = csv.writer(file)

        writer.writerow(

            [
                "Website",
                "Username",
                "Password",
                "Category",
                "Notes",
                "Created"
            ]

        )

        for row in data:

            writer.writerow(

                [
                    row[1],
                    row[2],
                    decrypt_password(row[3]),
                    row[4],
                    row[5],
                    row[6]
                ]

            )

    messagebox.showinfo(
        "Exported",
        "CSV Exported"
    )


def backup_database():

    shutil.copy(
        "passwords.db",
        "backup_passwords.db"
    )

    messagebox.showinfo(
        "Backup",
        "Database Backup Created"
    )


def secret_vault():

    messagebox.showinfo(
        "Vault",
        "🔥 Secret Vault Activated 🔥"
    )


def pin_lock():

    pin = simpledialog.askstring(
        "PIN",
        "Enter PIN"
    )

    if check_pin(pin):

        messagebox.showinfo(
            "Access",
            "PIN Accepted"
        )

    else:

        messagebox.showerror(
            "Error",
            "Wrong PIN"
        )


def auto_logout():

    root.after(
        30000,
        root.destroy
    )

    messagebox.showinfo(
        "Auto Logout",
        "App Will Close In 30 Seconds"
    )


def toggle_theme():

    global dark_mode

    if dark_mode:

        root.config(bg="white")

        theme_button.config(
            text="🌙 Dark Mode"
        )

        dark_mode = False

    else:

        root.config(bg="#0d1117")

        theme_button.config(
            text="☀ Light Mode"
        )

        dark_mode = True


# ---------------- LOGIN ---------------- #

def login():

    password = password_entry_login.get()

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
    "Login"
)

login_window.geometry(
    "450x350"
)

login_window.config(
    bg="#0d1117"
)

title = Label(

    login_window,

    text="PASSWORD MANAGER",

    font=("Arial", 24, "bold"),

    bg="#0d1117",

    fg="#00ffcc"

)

title.pack(pady=40)

Label(

    login_window,

    text="Master Password",

    bg="#0d1117",

    fg="white",

    font=("Arial", 12)

).pack(pady=10)

password_entry_login = Entry(

    login_window,

    show="*",

    width=30,

    font=("Arial", 12)

)

password_entry_login.pack(pady=10)

Button(

    login_window,

    text="LOGIN",

    command=login,

    bg="#238636",

    fg="white",

    width=20,

    font=("Arial", 12, "bold")

).pack(pady=20)

login_window.mainloop()