BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
from pandas import *
from random import choice

#-----------------------------DATA SETUP----------------------------#
data = read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

#-----------------------------SWITCH WORD----------------------------#
def switch_word():
    new_word = choice(to_learn)
    canvas.itemconfig(word, text=new_word["French"])
    canvas.itemconfig(title, text="French")

#-----------------------------UI SETUP----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#left button
cross_img = PhotoImage(file="images/wrong.png")
left_button = Button(image=cross_img, highlightthickness=0, command=switch_word)
left_button.grid(column=0, row=1)

#right button
check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=switch_word)
right_button.grid(column=1, row=1)

switch_word()

window.mainloop()