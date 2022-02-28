from tkinter import *

def button_clicked():
    my_label.config(text=input.get())
    print(type(input.get()))

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)

#Label
my_label = Label(text= "I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
my_label.config(text= "New Text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Cancel", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button_2 = Button(text="Submit", command=button_clicked)
button_2.grid(column=2, row=0)

#Entry
input = Entry()
entered_text= input.get()
input.grid(column=3, row=2)


window.mainloop()