from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pyperclip

from auth import *
from generator import generate_password
from database import *
from security import *
from analyzer import *
from backup import *
from stats import *
from config import *
from cyber_theme import *

create_table()

CURRENT_USER = "admin"

show_password = False

window = Tk()

window.title(f"{APP_NAME} {VERSION}")

window.geometry("1600x900")

window.config(bg=BG_COLOR)

window.iconbitmap("icon.ico")

sidebar = Frame(

    window,

    bg=SIDEBAR_COLOR,

    width=260

)

sidebar.pack(

    side=LEFT,

    fill=Y

)

sidebar.pack_propagate(False)

logo = Label(

    sidebar,

    text="CYBER\nVAULT",

    bg=SIDEBAR_COLOR,

    fg=CYAN,

    font=(FONT, 34, "bold")

)

logo.pack(pady=40)

stats_label = Label(

    sidebar,

    text="Stored Passwords",

    bg=SIDEBAR_COLOR,

    fg="white",

    font=(FONT, 18, "bold")

)

stats_label.pack(pady=10)

stats_count = Label(

    sidebar,

    text="0",

    bg=SIDEBAR_COLOR,

    fg="white",

    font=(FONT, 24, "bold")

)

stats_count.pack()

clock_label = Label(

    sidebar,

    bg=SIDEBAR_COLOR,

    fg=GREEN,

    font=(FONT, 28, "bold")

)

clock_label.pack(pady=80)

terminal = Text(

    sidebar,

    height=12,

    width=28,

    bg="black",

    fg=GREEN,

    font=("Consolas", 10)

)

terminal.pack(pady=20)

terminal.insert(

    END,

    "[ SYSTEM ONLINE ]\n"

)

terminal.insert(

    END,

    "[ VAULT ENCRYPTED ]\n"

)

terminal.insert(

    END,

    "[ SECURITY ACTIVE ]\n"

)

terminal.insert(

    END,

    "[ FIREWALL ENABLED ]\n"

)

terminal.insert(

    END,

    "[ ACCESS GRANTED ]\n"

)

terminal.config(state=DISABLED)

main = Frame(

    window,

    bg=BG_COLOR

)

main.pack(

    side=LEFT,

    fill=BOTH,

    expand=True

)

title = Label(

    main,

    text="Password Manager Dashboard",

    bg=BG_COLOR,

    fg="white",

    font=(FONT, 36, "bold")

)

title.pack(pady=25)

form = Frame(

    main,

    bg=BG_COLOR

)

form.pack(pady=10)

website_label = Label(

    form,

    text="Website",

    bg=BG_COLOR,

    fg="white",

    font=(FONT, 16)

)

website_label.grid(row=0, column=0, pady=10, padx=10)

website_entry = Entry(

    form,

    width=40,

    font=(FONT, 16)

)

website_entry.grid(row=0, column=1, pady=10)

username_label = Label(

    form,

    text="Username",

    bg=BG_COLOR,

    fg="white",

    font=(FONT, 16)

)

username_label.grid(row=1, column=0, pady=10)

username_entry = Entry(

    form,

    width=40,

    font=(FONT, 16)

)

username_entry.grid(row=1, column=1, pady=10)

password_label = Label(

    form,

    text="Password",

    bg=BG_COLOR,

    fg="white",

    font=(FONT, 16)

)

password_label.grid(row=2, column=0, pady=10)

password_entry = Entry(

    form,

    width=40,

    show="*",

    font=(FONT, 16)

)

password_entry.grid(row=2, column=1, pady=10)

category_label = Label(

    form,

    text="Category",

    bg=BG_COLOR,

    fg="white",

    font=(FONT, 16)

)

category_label.grid(row=3, column=0, pady=10)

category_entry = Entry(

    form,

    width=40,

    font=(FONT, 16)

)

category_entry.grid(row=3, column=1, pady=10)


# NOTES

notes_label = Label(

    form,

    text="Notes",

    bg=BG_COLOR,

    fg="white",

    font=(FONT, 16)

)

notes_label.grid(row=4, column=0, pady=10)

notes_entry = Entry(

    form,

    width=40,

    font=(FONT, 16)

)

notes_entry.grid(row=4, column=1, pady=10)

strength_label = Label(

    main,

    text="Strength: ",

    bg=BG_COLOR,

    fg="white",

    font=(FONT, 20, "bold")

)

strength_label.pack(pady=10)

def update_clock():

    time_now = datetime.now().strftime(
        "%H:%M:%S"
    )

    clock_label.config(
        text=time_now
    )

    window.after(
        1000,
        update_clock
    )


def update_strength(event=None):

    password = password_entry.get()

    strength = check_strength(password)

    if strength == "Weak":

        strength_label.config(

            text="Strength: Weak",

            fg=RED

        )

    elif strength == "Medium":

        strength_label.config(

            text="Strength: Medium",

            fg=YELLOW

        )

    else:

        strength_label.config(

            text="Strength: Strong",

            fg=GREEN

        )


password_entry.bind(

    "<KeyRelease>",

    update_strength

)


def refresh_table():

    for item in table.get_children():

        table.delete(item)

    data = view_passwords_db(
        CURRENT_USER
    )

    for row in data:

        decrypted = decrypt_password(
            row[3]
        )

        table.insert(

            "",

            END,

            values=(

                row[1],

                row[2],

                decrypted,

                row[4],

                row[5]

            )

        )

    stats_count.config(

        text=str(len(data))

    )


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

        notes,

        CURRENT_USER

    )

    create_backup()

    refresh_table()

    clear_fields()

    messagebox.showinfo(

        "Saved",

        "Password Saved Successfully"

    )


def search_password():

    website = website_entry.get()

    data = search_password_db(

        website,

        CURRENT_USER

    )

    for item in table.get_children():

        table.delete(item)

    for row in data:

        decrypted = decrypt_password(
            row[3]
        )

        table.insert(

            "",

            END,

            values=(

                row[1],

                row[2],

                decrypted,

                row[4],

                row[5]

            )

        )


def delete_password_gui():

    website = website_entry.get()

    delete_password_db(

        website,

        CURRENT_USER

    )

    refresh_table()

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

    update_strength()


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

    pyperclip.copy(

        password_entry.get()

    )

    messagebox.showinfo(

        "Copied",

        "Password Copied"

    )


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

button_frame = Frame(

    main,

    bg=BG_COLOR

)

button_frame.pack(pady=20)


save_button = Button(

    button_frame,

    text="Save Password",

    command=save_password,

    width=18

)

button_style(

    save_button,

    "#00c853"

)

save_button.grid(row=0, column=0, padx=10, pady=10)


view_button = Button(

    button_frame,

    text="Refresh Table",

    command=refresh_table,

    width=18

)

button_style(

    view_button,

    "#2962ff"

)

view_button.grid(row=0, column=1, padx=10)


search_button = Button(

    button_frame,

    text="Search Password",

    command=search_password,

    width=18

)

button_style(

    search_button,

    "#ff9100"

)

search_button.grid(row=0, column=2, padx=10)


delete_button = Button(

    button_frame,

    text="Delete Password",

    command=delete_password_gui,

    width=18

)

button_style(

    delete_button,

    "#ff1744"

)

delete_button.grid(row=1, column=0, padx=10, pady=10)


generate_button = Button(

    button_frame,

    text="Generate Password",

    command=generate_password_gui,

    width=18

)

button_style(

    generate_button,

    "#aa00ff"

)

generate_button.grid(row=1, column=1, padx=10)


copy_button = Button(

    button_frame,

    text="Copy Password",

    command=copy_password,

    width=18

)

button_style(

    copy_button,

    "#00b8d4"

)

copy_button.grid(row=1, column=2, padx=10)


show_button = Button(

    button_frame,

    text="Show / Hide",

    command=toggle_password,

    width=18

)

button_style(

    show_button,

    "#455a64"

)

show_button.grid(row=2, column=1, pady=10)

table_frame = Frame(

    main,

    bg=BG_COLOR

)

table_frame.pack(

    fill=BOTH,

    expand=True,

    padx=30,

    pady=20

)

columns = (

    "Website",

    "Username",

    "Password",

    "Category",

    "Notes"

)

table = ttk.Treeview(

    table_frame,

    columns=columns,

    show="headings",

    height=12

)

for col in columns:

    table.heading(

        col,

        text=col

    )

    table.column(

        col,

        width=220

    )

table.pack(

    fill=BOTH,

    expand=True

)

refresh_table()

update_clock()

window.mainloop()
