from config import *

def button_style(button, color):

    button.config(

        bg=color,

        fg="white",

        activebackground=color,

        activeforeground="white",

        bd=0,

        font=(FONT, 11, "bold"),

        cursor="hand2"

    )