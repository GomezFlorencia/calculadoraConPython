import tkinter as tk


def button_press(num):
    global equation_text
    try:

        equation_text = equation_text + str(num)
        equation_label.set(equation_text)
    except SyntaxError:
        equation_label.set("SyntaxisError")
        equation_text = ""


def equals():
    global equation_text
    try:

        result = str(eval(equation_text))
        equation_label.set(result)
        equation_text = result
    except ZeroDivisionError:
        equation_label.set("No se puede dividir por 0")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


equation_text = ""

window = tk.Tk()
window.title("Calculadora")
window.geometry("500x500")

equation_label = tk.StringVar()
equation_label.set(equation_text)
label = tk.Label(window, textvariable=equation_label,
                 font=("consolas", 20), width=24, height=2)
label.pack()
frame = tk.Frame(window)
frame.pack()
button1 = tk.Button(frame, text=1, height=4, width=9,
                    font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)
button2 = tk.Button(frame, text=2, height=4, width=9,
                    font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)
button3 = tk.Button(frame, text=3, height=4, width=9,
                    font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)
button4 = tk.Button(frame, text=4, height=4, width=9,
                    font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)
button5 = tk.Button(frame, text=5, height=4, width=9,
                    font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)
button6 = tk.Button(frame, text=6, height=4, width=9,
                    font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)
button7 = tk.Button(frame, text=7, height=4, width=9,
                    font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)
button8 = tk.Button(frame, text=8, height=4, width=9,
                    font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)
button9 = tk.Button(frame, text=9, height=4, width=9,
                    font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)
button0 = tk.Button(frame, text=0, height=4, width=9,
                    font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)
plus_button = tk.Button(frame, text='+', height=4, width=9,
                        font=35, command=lambda: button_press('+'))
plus_button.grid(row=0, column=3)
minus_button = tk.Button(frame, text='-', height=4,
                         width=9, font=35, command=lambda: button_press('-'))
minus_button.grid(row=1, column=3)
mult_button = tk.Button(frame, text='*', height=4, width=9,
                        font=35, command=lambda: button_press('*'))
mult_button.grid(row=2, column=3)
div_button = tk.Button(frame, text='/', height=4, width=9,
                       font=35, command=lambda: button_press('/'))
div_button.grid(row=3, column=3)
decimal_button = tk.Button(frame, text='.', height=4,
                           width=9, font=35, command=lambda: button_press('.'))
decimal_button.grid(row=3, column=1)
equals_button = tk.Button(frame, text='=', height=4,
                          width=9, font=35, command=equals)
equals_button.grid(row=3, column=2)
clear_button = tk.Button(frame, text='Clear', height=4,
                         width=9, font=35, command=clear)
clear_button.grid(row=4, column=3)


window.mainloop()
