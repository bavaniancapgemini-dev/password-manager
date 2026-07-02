def hover_effect(button, color1, color2):

    def on_enter(e):

        button.config(
            bg=color2
        )

    def on_leave(e):

        button.config(
            bg=color1
        )

    button.bind("<Enter>", on_enter)

    button.bind("<Leave>", on_leave)