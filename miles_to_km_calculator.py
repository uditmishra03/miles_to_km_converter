from tkinter import *

FONT = ("Courier", 14)

def miles_to_km():
    miles = float(miles_input.get())
    # miles_float = (miles)
    km = round(miles * 1.609,2)
    converted_value_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")

window.config(padx=20, pady=20)

# Entry for Miles
miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

isequalto_label = Label(text="is equal to", font=FONT)
isequalto_label.grid(column=0, row=1)


converted_value_label = Label(text="0", font=FONT)
converted_value_label.grid(column=1, row=1)

km_label = Label(text="km", font=FONT)
km_label.grid(column=3, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
