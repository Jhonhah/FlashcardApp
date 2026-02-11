BACKGROUND_COLOR = "#B1DDC6"
global T


from tkinter import *
from pandas import *
from random import choice

#-----------------------------DATA SETUP----------------------------#
data = read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

#-----------------------------SWITCH WORD----------------------------#
def switch_word():
    new_word = choice(to_learn)
    canvas.itemconfig(current_image, image=front_image)
    canvas.itemconfig(word, text=new_word["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")


#-----------------------------FLIP CARD----------------------------#
def flip_card():
    current_word = canvas.itemcget(word, "text")
    translation = data[data.French == current_word].English.item()
    canvas.itemconfig(current_image, image=back_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=translation, fill="white")
    print(translation)
#-----------------------------UI SETUP----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
current_image = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#left button
cross_img = PhotoImage(file="images/wrong.png")
left_button = Button(image=cross_img, highlightthickness=0, command=flip_card)
left_button.grid(column=0, row=1)

#right button
check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=switch_word)
right_button.grid(column=1, row=1)

switch_word()

window.mainloop()