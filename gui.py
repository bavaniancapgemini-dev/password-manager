from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from datetime import datetime

import pyperclip

from user_auth import *
from generator import generate_password
from database import *
from security import *
from analyzer import *
from backup import *
from stats import *
from config import *
from cyber_theme import *
from activity import *
from health import *
from importer import *
from notifications import *
from matrix_effect import *
from ui_effects import *

create_table()
create_user_table()

CURRENT_USER = ""
show_password = False

window = Tk()

window.title(f"{APP_NAME} {VERSION}")

window.geometry("1600x900")

window.config(bg=BG_COLOR)

try:
    window.iconbitmap("icon.ico")
except:
    pass

window.withdraw()

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

logo.pack(pady=30)

user_panel = Label(
    sidebar,
    text="USER",
    bg=SIDEBAR_COLOR,
    fg="white",
    font=(FONT, 16, "bold")
)

user_panel.pack(pady=20)

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

security_score = Label(
    sidebar,
    text="Security Score\n100%",
    bg=SIDEBAR_COLOR,
    fg=GREEN,
    font=(FONT, 20, "bold")
)

security_score.pack(pady=20)

clock_label = Label(
    sidebar,
    bg=SIDEBAR_COLOR,
    fg=GREEN,
    font=(FONT, 26, "bold")
)

clock_label.pack(pady=30)

notification_box = Text(
    sidebar,
    height=10,
    width=28,
    bg="#111",
    fg="orange",
    font=("Consolas", 10)
)

notification_box.pack(pady=20)

# =========================
# MAIN AREA
# =========================

main = Frame(
    window,
    bg=BG_COLOR
)

main.pack(
    side=LEFT,
    fill=BOTH,
    expand=True
)

matrix_canvas = Canvas(

    main,

    bg="#000814",

    highlightthickness=0

)

matrix_canvas.place(

    x=0,
    y=0,

    relwidth=1,
    relheight=1

)

start_matrix(
    matrix_canvas,
    1400,
    900
)

title = Label(
    main,
    text="Password Manager Dashboard",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 30, "bold")
)

title.pack(pady=20)

# =========================
# FORM
# =========================

form = Frame(
    main,
    bg=BG_COLOR
)

form.pack(pady=10)

# WEBSITE

Label(
    form,
    text="Website",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 14)
).grid(row=0, column=0, padx=10, pady=10)

website_entry = Entry(
    form,
    width=40,
    font=(FONT, 14)
)

website_entry.grid(row=0, column=1)

# USERNAME

Label(
    form,
    text="Username",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 14)
).grid(row=1, column=0, padx=10, pady=10)

username_entry = Entry(
    form,
    width=40,
    font=(FONT, 14)
)

username_entry.grid(row=1, column=1)

# PASSWORD

Label(
    form,
    text="Password",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 14)
).grid(row=2, column=0, padx=10, pady=10)

password_entry = Entry(
    form,
    width=40,
    show="*",
    font=(FONT, 14)
)

password_entry.grid(row=2, column=1)

# CATEGORY

Label(
    form,
    text="Category",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 14)
).grid(row=3, column=0, padx=10, pady=10)

category_entry = Entry(
    form,
    width=40,
    font=(FONT, 14)
)

category_entry.grid(row=3, column=1)

# NOTES

Label(
    form,
    text="Notes",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 14)
).grid(row=4, column=0, padx=10, pady=10)

notes_entry = Entry(
    form,
    width=40,
    font=(FONT, 14)
)

notes_entry.grid(row=4, column=1)

# =========================
# STRENGTH LABEL
# =========================

strength_label = Label(
    main,
    text="Strength:",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 18, "bold")
)

strength_label.pack(pady=10)

# =========================
# TABLE
# =========================

table_frame = Frame(
    main,
    bg=BG_COLOR
)

table_frame.pack(
    fill=BOTH,
    expand=True,
    padx=20,
    pady=20
)

columns = (
    "Website",
    "Username",
    "Password",
    "Category",
    "Notes"
)

style = ttk.Style()

style.theme_use("clam")

style.configure(

    "Treeview",

    background="#001233",

    foreground="cyan",

    fieldbackground="#001233",

    rowheight=35,

    font=("Consolas", 11)

)

style.configure(

    "Treeview.Heading",

    background="#001845",

    foreground="white",

    font=("Arial", 12, "bold")

)

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:

    table.heading(col, text=col)

    table.column(col, width=220)

table.pack(
    fill=BOTH,
    expand=True
)

# =========================
# FUNCTIONS
# =========================

def update_clock():

    now = datetime.now().strftime("%H:%M:%S")

    clock_label.config(text=now)

    window.after(1000, update_clock)

def check_strength(password):

    if len(password) < 6:
        return "Weak"

    elif len(password) < 10:
        return "Medium"

    else:
        return "Strong"

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

password_entry.bind("<KeyRelease>", update_strength)

def refresh_table():

    for item in table.get_children():

        table.delete(item)

    data = view_passwords_db(CURRENT_USER)

    analysis = analyze_passwords(data)

    security_score.config(
        text=f"Security Score\n{analysis['score']}%"
    )

    notifications_list = generate_notifications(analysis)

    notification_box.delete(1.0, END)

    for note in notifications_list:

        notification_box.insert(
            END,
            note + "\n"
        )

    for row in data:

        decrypted = decrypt_password(row[3])

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

    stats_count.config(text=str(len(data)))

def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    category = category_entry.get()
    notes = notes_entry.get()

    encrypted = encrypt_password(password)

    save_password_db(
        website,
        username,
        encrypted,
        category,
        notes,
        CURRENT_USER
    )

    log_activity(
        f"{CURRENT_USER} saved password for {website}"
    )

    create_backup()

    refresh_table()

    clear_fields()

    messagebox.showinfo(
        "Saved",
        "Password Saved"
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

        decrypted = decrypt_password(row[3])

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

    log_activity(
        f"{CURRENT_USER} deleted password for {website}"
    )

    refresh_table()

def generate_password_gui():

    password_entry.delete(0, END)

    password_entry.insert(
        0,
        generate_password()
    )

    update_strength()

def clear_fields():

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    category_entry.delete(0, END)
    notes_entry.delete(0, END)

def copy_password():

    pyperclip.copy(password_entry.get())

    messagebox.showinfo(
        "Copied",
        "Password Copied"
    )

def toggle_password():

    global show_password

    if show_password:

        password_entry.config(show="*")

        show_password = False

    else:

        password_entry.config(show="")

        show_password = True

def select_record(event):

    selected = table.focus()

    values = table.item(selected, "values")

    if values:

        clear_fields()

        website_entry.insert(0, values[0])
        username_entry.insert(0, values[1])
        password_entry.insert(0, values[2])
        category_entry.insert(0, values[3])
        notes_entry.insert(0, values[4])

table.bind("<Double-1>", select_record)

def import_passwords():

    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )

    if filepath:

        import_csv(
            filepath,
            CURRENT_USER
        )

        refresh_table()

def view_activity():

    activity_window = Toplevel()

    activity_window.title("Activity Logs")

    activity_window.geometry("700x500")

    text = Text(
        activity_window,
        bg="black",
        fg="lime",
        font=("Consolas", 10)
    )

    text.pack(fill=BOTH, expand=True)

    try:

        with open("activity.log", "r") as file:

            text.insert(
                END,
                file.read()
            )

    except:

        text.insert(
            END,
            "No activity logs."
        )

# =========================
# BUTTONS
# =========================
# =========================
# MODERN BUTTON PANEL v23.0
# =========================

button_container = Frame(
    main,
    bg=BG_COLOR
)

button_container.pack(pady=20)

top_buttons = Frame(
    button_container,
    bg=BG_COLOR
)

top_buttons.pack(pady=10)

bottom_buttons = Frame(
    button_container,
    bg=BG_COLOR
)

bottom_buttons.pack(pady=10)

# =========================
# BUTTON STYLE FUNCTION
# =========================

def cyber_button(parent, text, command, color):

    btn = Button(

        parent,

        text=text,

        command=command,

        bg=color,

        fg="white",

        activebackground=color,

        activeforeground="white",

        font=("Arial", 12, "bold"),

        width=20,

        height=2,

        relief=FLAT,

        cursor="hand2",

        bd=0

    )

    def on_enter(e):

        btn.config(
            bg="#00ffee",
            fg="black"
        )

    def on_leave(e):

        btn.config(
            bg=color,
            fg="white"
        )

    btn.bind("<Enter>", on_enter)

    btn.bind("<Leave>", on_leave)

    return btn

# =========================
# TOP ROW BUTTONS
# =========================

save_btn = cyber_button(

    top_buttons,

    "💾 Save Password",

    save_password,

    "#00c853"

)

save_btn.grid(row=0, column=0, padx=10, pady=10)

refresh_btn = cyber_button(

    top_buttons,

    "🔄 Refresh",

    refresh_table,

    "#2962ff"

)

refresh_btn.grid(row=0, column=1, padx=10, pady=10)

search_btn = cyber_button(

    top_buttons,

    "🔍 Search",

    search_password,

    "#ff9100"

)

search_btn.grid(row=0, column=2, padx=10, pady=10)

delete_btn = cyber_button(

    top_buttons,

    "❌ Delete",

    delete_password_gui,

    "#ff1744"

)

delete_btn.grid(row=1, column=0, padx=10, pady=10)

generate_btn = cyber_button(

    top_buttons,

    "⚡ Generate",

    generate_password_gui,

    "#aa00ff"

)

generate_btn.grid(row=1, column=1, padx=10, pady=10)

copy_btn = cyber_button(

    top_buttons,

    "📋 Copy",

    copy_password,

    "#00b8d4"

)

copy_btn.grid(row=1, column=2, padx=10, pady=10)

# =========================
# BOTTOM ROW BUTTONS
# =========================

toggle_btn = cyber_button(

    bottom_buttons,

    "👁 Show / Hide",

    toggle_password,

    "#455a64"

)

toggle_btn.grid(row=0, column=0, padx=10, pady=10)

import_btn = cyber_button(

    bottom_buttons,

    "📂 Import CSV",

    import_passwords,

    "#7c4dff"

)

import_btn.grid(row=0, column=1, padx=10, pady=10)

activity_btn = cyber_button(

    bottom_buttons,

    "🧠 Activity Logs",

    view_activity,

    "#00bfa5"

)

activity_btn.grid(row=0, column=2, padx=10, pady=10)
# =========================
# LOGIN SYSTEM
# =========================

login_window = Toplevel()

login_window.title("CYBER VAULT Login")

login_window.geometry("500x500")

login_window.config(bg=BG_COLOR)

Label(
    login_window,
    text="CYBER VAULT",
    bg=BG_COLOR,
    fg=CYAN,
    font=(FONT, 30, "bold")
).pack(pady=40)

Label(
    login_window,
    text="Username",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 14)
).pack(pady=10)

username_entry_login = Entry(
    login_window,
    width=30,
    font=(FONT, 14)
)

username_entry_login.pack(pady=10)

Label(
    login_window,
    text="Password",
    bg=BG_COLOR,
    fg="white",
    font=(FONT, 14)
).pack(pady=10)

password_entry_login = Entry(
    login_window,
    width=30,
    show="*",
    font=(FONT, 14)
)

password_entry_login.pack(pady=10)

def login():

    global CURRENT_USER

    username = username_entry_login.get()

    password = password_entry_login.get()

    data = login_user(
        username,
        password
    )

    if data:

        CURRENT_USER = username

        user_panel.config(
            text=f"USER\n{CURRENT_USER}"
        )

        log_activity(
            f"{username} logged in"
        )

        login_window.destroy()

        refresh_table()

        window.deiconify()

    else:

        messagebox.showerror(
            "Error",
            "Invalid Login"
        )

def register():

    username = username_entry_login.get()

    password = password_entry_login.get()

    success = register_user(
        username,
        password
    )

    if success:

        messagebox.showinfo(
            "Success",
            "Account Created"
        )

    else:

        messagebox.showerror(
            "Error",
            "Username Already Exists"
        )

Button(
    login_window,
    text="Login",
    command=login,
    width=20,
    bg="#00c853",
    fg="white"
).pack(pady=20)

Button(
    login_window,
    text="Register",
    command=register,
    width=20,
    bg="#2962ff",
    fg="white"
).pack()

# =========================
# START
# =========================

update_clock()

status_bar = Label(

    window,

    text="CYBER VAULT v23.0 ACTIVE",

    bg="#001233",

    fg="#00ffcc",

    font=("Consolas", 11)

)

status_bar.pack(

    side=BOTTOM,

    fill=X
)

window.mainloop()