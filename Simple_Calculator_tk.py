# By Ammar_An

from tkinter import *

window = Tk()

window.title("Simple Calculator")


e = Entry(window, width=45, borderwidth=5, bg="blue", fg="white")
e.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
#e.place(height=50, width=150)

# Define functions

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0,END)

def button_devide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0,END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition' :
        e.insert(0, f_num + float(second_number))
    elif math == 'subtraction' :
        e.insert(0, f_num - float(second_number))
    elif math == 'multiplication' :
        e.insert(0, f_num * float(second_number))
    elif math == 'division' :
        e.insert(0, f_num / float(second_number))




# Difine buttons

button_1 = Button(window, text="1", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, bg="orange", fg="black", command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=41, pady=20, bg="orange", fg="black", command=lambda: button_click(0))
button_comma = Button(window, text=".", padx=41, pady=20, bg="orange", fg="black", command=lambda: button_click('.'))

button_clear = Button(window, text="Clear", padx=29, pady=20, bg="yellow", fg="black", command=button_clear)

button_equal = Button(window, text="=", padx=87, pady=20, bg="yellow", fg="black", command=button_equal)

button_add = Button(window, text="+", padx=39, pady=20, bg="pink", fg="black", command=button_add)
button_subtract = Button(window, text="-", padx=41, pady=20, bg="pink", fg="black", command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, bg="pink", fg="black", command=button_multiply)
button_devide = Button(window, text="/", padx=40, pady=20, bg="pink", fg="black", command=button_devide)



# Put the buttons on the screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)
button_comma.grid(row=4, column=0)

button_clear.grid(row=4, column=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_devide.grid(row=6, column=2)



window.mainloop()



# python Simple_Calculator_tk.py
