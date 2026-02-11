BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *

#-----------------------------UI SETUP----------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="partie", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

#left button
cross_img = PhotoImage(file="images/wrong.png")
left_button = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, command="")
left_button.grid(column=0, row=1)

#right button
check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, command="")
right_button.grid(column=1, row=1)





window.mainloop()