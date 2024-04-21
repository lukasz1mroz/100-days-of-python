import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Entry
my_entry = tkinter.Entry(width=10)
my_entry.grid(column=1, row=0)

#Label
miles_label = tkinter.Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

kms_label = tkinter.Label(text=f"Is equal to 0 km", font=("Arial", 24))
kms_label.grid(column=1, row=1)

def button_clicked():
    entry_miles = my_entry.get()
    kms = int(int(entry_miles) * 1.6)
    kms_label.config(text=f"Is equal to {kms} km")

#Button
my_button = tkinter.Button(text="Calculate", command=button_clicked)
my_button.grid(column=2, row=2)

#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# def scale_used(value):
#     print(value)
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = tkinter.IntVar()
# checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = tkinter.IntVar()
# radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = tkinter.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()