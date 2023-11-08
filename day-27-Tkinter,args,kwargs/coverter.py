from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.config(padx=20,pady=20)

# Label
myles_label = Label(text="Miles")
myles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

my_result = Label(text="0")
my_result.grid(column=1, row=1)

#Button

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609)
    my_result.config(text=f"{km}")
    print("Button clicked")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Comes at the end of the code
window.mainloop()