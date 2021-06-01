from tkinter import *

expression = ""

def event(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)

def evaluate():
    global expression

    finalans = str(eval(expression))
    equation.set(finalans)

    expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")



if __name__ == "__main__":

    calc_gui = Tk()

    calc_gui.configure(background="light green")
    calc_gui.title("Simple Calculator in Python")
    calc_gui.geometry("550x350")

    equation = StringVar()

    number_field = Entry(calc_gui,textvariable=equation)
    number_field.grid(columnspan=4, ipadx=220,ipady=15)

    button_1 = Button(calc_gui, text=' 1 ', fg='black', bg='grey',command=lambda: event(1), height=2, width=12)
    button_1.grid(row=2, column=0,pady=4)

    button_2 = Button(calc_gui, text=' 2 ', fg='black', bg='grey',command=lambda: event(2), height=2, width=12)
    button_2.grid(row=2, column=1,pady=4)

    button_3 = Button(calc_gui, text=' 3 ', fg='black', bg='grey',command=lambda: event(3), height=2, width=12)
    button_3.grid(row=2, column=2,pady=4)

    button_4 = Button(calc_gui, text=' 4 ', fg='black', bg='grey',command=lambda: event(4), height=2, width=12)
    button_4.grid(row=3, column=0,pady=4)

    button_5 = Button(calc_gui, text=' 5 ', fg='black', bg='grey',command=lambda: event(5), height=2, width=12)
    button_5.grid(row=3, column=1,pady=4)
 
    button_6 = Button(calc_gui, text=' 6 ', fg='black', bg='grey',command=lambda: event(6), height=2, width=12)
    button_6.grid(row=3, column=2,pady=4)

    button_7 = Button(calc_gui, text=' 7 ', fg='black', bg='grey',command=lambda: event(7), height=2, width=12)
    button_7.grid(row=4, column=0,pady=4)
 
    button_8 = Button(calc_gui, text=' 8 ', fg='black', bg='grey',command=lambda: event(8), height=2, width=12)
    button_8.grid(row=4, column=1,pady=4)
 
    button_9 = Button(calc_gui, text=' 9 ', fg='black', bg='grey',command=lambda: event(9), height=2, width=12)
    button_9.grid(row=4, column=2,pady=4)
 
    button_0 = Button(calc_gui, text=' 0 ', fg='black', bg='grey',command=lambda: event(0), height=2, width=12)
    button_0.grid(row=5, column=0,pady=4)

    addition = Button(calc_gui, text=' + ', fg='black', bg='grey',command=lambda: event("+"), height=2, width=12)
    addition.grid(row=2, column=3,pady=4)

    subtraction = Button(calc_gui, text=' - ', fg='black', bg='grey',command=lambda: event("-"), height=2, width=12)
    subtraction.grid(row=3, column=3,pady=4)

    multiplication = Button(calc_gui, text=' * ', fg='black', bg='grey',command=lambda: event("*"), height=2, width=12)
    multiplication.grid(row=4, column=3,pady=4)

    divide = Button(calc_gui, text=' / ', fg='black', bg='grey',command=lambda: event("/"), height=2, width=12)
    divide.grid(row=5, column=3,pady=4)
 
    equal = Button(calc_gui, text=' = ', fg='black', bg='red',command=evaluate, height=2, width=12)
    equal.grid(row=5, column=2,pady=4)

    clear_field = Button(calc_gui, text='Clear', fg='black', bg='grey',command=clear, height=2, width=12)
    clear_field.grid(row=5, column='1',pady=4)

    decimal_point= Button(calc_gui, text='.', fg='black', bg='grey',command=lambda: event('.'), height=2, width=12)
    decimal_point.grid(row=6, column=0,pady=4)



    calc_gui.mainloop()