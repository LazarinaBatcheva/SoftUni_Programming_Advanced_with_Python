import tkinter

from canvas import app


def clean_screen():
    for el in app.grid_slaves():
        el.destroy()
        tkinter.Button(app, text="Exit", command=app.destroy).grid(row=10, column=0, pady=20)