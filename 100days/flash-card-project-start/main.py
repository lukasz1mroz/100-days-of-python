BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

current_card = {}
words = {}
# Get words and data
try:
    french_words = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
    words = french_words.to_dict(orient="records")
else:
    words = french_words.to_dict(orient="records")

# Def functions
def find_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(words)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card['French'])
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card['English'])

def is_known():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/to_learn.csv", index=False)
    find_word()

# Setup window
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Setup canvas with card and text
canvas = Canvas(height=526, width=800, bd=0, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Setup buttons
wrong_button_img = PhotoImage(file="./images/wrong.png")
right_button_img = PhotoImage(file="./images/right.png")
wrong_button = Button(image=wrong_button_img, bd=0, highlightthickness=0, command=find_word)
right_button = Button(image=right_button_img, bd=0, highlightthickness=0, command=is_known)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

find_word()

window.mainloop()