import math
from tkinter import *


#Window definitions#
win = Tk()
win.geometry("337x596")
win.resizable(0, 0)
win.title("4004 Calculator")


def radtoangle(x):
    return x * 3.14159265359 / 180


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return pow(x, y)


def sqrt(x):
    return math.sqrt(x)


def naturallog(x):
    return math.log(x)


def sine(x):
    return math.sin(x)


def arcsin(x):
    return math.asin(x)


def cosine(x):
    return math.cos(x)


def arccosine(x):
    return math.acos(x)


def tangent(x):
    return math.tan(x)


def inchcm(x):
    return x * 2.54


def cminch(x):
    return x / 2.54



def calc_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)



def clear():
    global expression
    expression = ""
    input_text.set("")


def equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""

frame = Frame(win, width=337, height=596, bg="light blue")
frame.place(x=0, y=0)

input_text = StringVar()

input_frame = Frame(win, width=270, height=60, bd=0)
input_frame.place(x=35, y=25)
input_frame.tkraise(frame)
input_field = Entry(input_frame, font=('roboto', 18,),
                    textvariable=input_text, justify=RIGHT)

input_field.grid(row=0, column=0)

AC = Button(text="AC", fg="black", width=9, height=4, bd=0,
            bg="light gray", cursor="hand2", command=lambda: clear())
AC.place(x=20, y=215)

one = Button(text="1", fg="black", width=9, height=4,
             bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(1))
one.place(x=20, y=440)

two = Button(text="2", fg="black", width=9, height=4,
             bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(2))
two.place(x=96, y=440)

three = Button(text="3", fg="black", width=9, height=4,
               bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(3))
three.place(x=171, y=440)

four = Button(text="4", fg="black", width=9, height=4,
              bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(4))
four.place(x=20, y=365)

five = Button(text="5", fg="black", width=9, height=4,
              bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(5))
five.place(x=96, y=365)

six = Button(text="6", fg="black", width=9, height=4,
             bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(6))
six.place(x=171, y=365)

seven = Button(text="7", fg="black", width=9, height=4,
               bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(7))
seven.place(x=20, y=290)

eight = Button(text="8", fg="black", width=9, height=4,
               bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(8))
eight.place(x=96, y=290)

nine = Button(text="9", fg="black", width=9, height=4,
              bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(9))
nine.place(x=171, y=290)

zero = Button(text="0", fg="black", width=20, height=4,
              bd=0, bg="#fff", cursor="hand2", command=lambda: calc_click(0))
zero.place(x=20, y=514)

plus = Button(text="+", fg="black", width=9, height=4, bd=0,
              bg="light gray", cursor="hand2", command=lambda: calc_click("+"))
plus.place(x=246, y=440)

minus = Button(text="-", fg="black", width=9, height=4, bd=0,
               bg="light gray", cursor="hand2", command=lambda: calc_click("-"))
minus.place(x=246, y=365)

div = Button(text="/", fg="black", width=9, height=4, bd=0,
             bg="light gray", cursor="hand2", command=lambda: calc_click("/"))
div.place(x=246, y=290)

mult = Button(text="x", fg="black", width=9, height=4, bd=0,
              bg="light gray", cursor="hand2", command=lambda: calc_click("*"))
mult.place(x=246, y=215)

leftbracket = Button(text="(", fg="black", width=9, height=4, bd=0,
                     bg="light gray", cursor="hand2", command=lambda: calc_click("("))
leftbracket.place(x=96, y=215)

rightbracket = Button(text=")", fg="black", width=9, height=4, bd=0,
                      bg="light gray", cursor="hand2", command=lambda: calc_click(")"))
rightbracket.place(x=171, y=215)

inchtocm = Button(text="Inches → CM", fg="black", width=9, height=4, bd=0,
                  bg="light gray", cursor="hand2", command=lambda: calc_click("*2.54"))
inchtocm.place(x=20, y=140)

cmtoinch = Button(text="CM → Inches", fg="black", width=9, height=4, bd=0,
                  bg="light gray", cursor="hand2", command=lambda: calc_click("/2.54"))
cmtoinch.place(x=96, y=140)

percent = Button(text="%", fg="black", width=9, height=4, bd=0,
                 bg="light gray", cursor="hand2", command=lambda: calc_click("/100*100"))
percent.place(x=171, y=140)

equals = Button(text="=", fg="black", width=20, height=4,
                bd=0, bg="light gray", cursor="hand2", command=lambda: equal())
equals.place(x=171, y=514)


win.mainloop()


print(" ")
print("Select operation:")
print(" ")
print("-----Duo Value-----")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
print("Power")
print("-----Single Value-----")
print("Inches to Cm")
print("Cm to Inches")
print("Square Root")
print("Log")
print("Cos")
print("Arccosine")
print("Sin")
print("Arcsin")
print('Tan')


print(" ")
while True:

    choice = input("Enter operation name: ")

    if choice in ('Add', 'add', 'Subtract', 'subtract', 'Multiply', 'multiply', 'Divide', 'divide', 'Power', 'power',):

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice in ['Add', 'add']:
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice in ['Subtract', 'subtract']:
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice in ['Multiply', 'multiply']:
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice in ['Divide', 'divide']:
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice in ['Power', 'power']:
            print(num1, "^", num2, "=", power(num1, num2))
        else:
            break

    elif choice in ('Square Root', 'square root', 'Square root', 'Log', 'log', 'sin', 'Sin', 'arcsin',
                    'Arcsin', 'Cos', 'cos', 'arccosine', 'Arccosine', 'tan', 'Tan', 'Inches to Cm',
                    'inches to cm', 'Cm to Inches', 'cm to inches'):
        num1 = float(input("Enter first number: "))

        if choice in ['Square Root', 'square root', 'Square root']:
            print(num1, "SQRT", "=", sqrt(num1))

        elif choice in ['Log', 'log']:
            print(num1, "Log", "=", naturallog(num1))

        elif choice in ['Sin', 'sin']:
            option1 = input('Calculate with Angle or Rad: ')
            if option1 in ['Angle', 'angle']:
                print(num1, "°", "Sine", "=", radtoangle(num1))
            elif option1 in ['Rad', 'rad']:
                print(num1, "Sine", "=", sine(num1))
            else:
                print("Invalid Input")
                continue

        elif choice in ['arcsin', 'Arcsin']:
            print(num1, "Arcsin", "=", arcsin(num1))

        elif choice in ['cos', 'Cos']:
            option1 = input('Calculate with Angle or Rad: ')
            if option1 in ['Angle', 'angle']:
                print(num1, "°", "Cosine", "=", cosine(radtoangle(num1)))
            elif option1 in ['Rad', 'rad']:
                print(num1, "Cosine", "=", cosine(num1))
            else:
                print("Invalid Input")
                continue

        elif choice in ['arccosine', 'Arccosine']:
            print(num1, "Arccosine", "=", arccosine(num1))

        elif choice in ['tan', 'Tan']:
            option1 = input('Calculate with Angle or Rad: ')
            if option1 in ['Angle', 'angle']:
                print(num1, "°", "Tan", "=", tangent(radtoangle(num1)))
            elif option1 in ['Ran', 'Rad']:
                print(num1, "Tan", "=", tangent(num1))
            else:
                print("Invalid Input")
                continue

        elif choice in ['Inches to Cm', 'inches to cm']:
            print(num1, "Inches to Centimeter", "=", inchcm(num1))

        elif choice in ['Cm to Inches', 'cm to inches']:
            print(num1, "Centimeter to Inches", "=", cminch(num1))
        break
    else:
        print("Invalid Input")
