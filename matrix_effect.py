from tkinter import *
import random

letters = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def start_matrix(canvas, width, height):

    columns = int(width / 20)

    drops = [0 for _ in range(columns)]

    def draw():

        canvas.delete("matrix")

        for i in range(len(drops)):

            text = random.choice(letters)

            x = i * 20

            y = drops[i] * 20

            canvas.create_text(

                x,
                y,

                text=text,

                fill="#00ff00",

                font=("Consolas", 12),

                tags="matrix"

            )

            if y > height and random.randint(0, 100) > 95:

                drops[i] = 0

            drops[i] += 1

        canvas.after(80, draw)

    draw()
