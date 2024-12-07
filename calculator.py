import customtkinter as ctk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        history_text = history_label.get()
        history_text += f"{equation_text}"
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
        history_text += f"={total}\n"
        history_label.set(history_text)

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = ctk.CTk()
window.title("Calculator program")
window.geometry("410x600")

equation_text = ""

equation_label = ctk.StringVar()
history_label = ctk.StringVar()

label = ctk.CTkLabel(window, textvariable=equation_label, font=('Arial', 20), width=450, height=50)
label.pack(pady=15)

frame = ctk.CTkFrame(window)
frame.pack()

button1 = ctk.CTkButton(frame, font=('Arial', 20), text=1, height=40, width=90, command=lambda: button_press(1))
button1.grid(padx=5, pady=5, row=0, column=0)

button2 = ctk.CTkButton(frame, font=('Arial', 20), text=2, height=40, width=90, command=lambda: button_press(2))
button2.grid(padx=5, pady=5, row=0, column=1)

button3 = ctk.CTkButton(frame, font=('Arial', 20), text=3, height=40, width=90, command=lambda: button_press(3))
button3.grid(padx=5, pady=5, row=0, column=2)

button4 = ctk.CTkButton(frame, font=('Arial', 20), text=4, height=40, width=90, command=lambda: button_press(4))
button4.grid(padx=5, pady=5, row=1, column=0)

button5 = ctk.CTkButton(frame, font=('Arial', 20), text=5, height=40, width=90, command=lambda: button_press(5))
button5.grid(padx=5, pady=5, row=1, column=1)

button6 = ctk.CTkButton(frame, font=('Arial', 20), text=6, height=40, width=90, command=lambda: button_press(6))
button6.grid(padx=5, pady=5, row=1, column=2)

button7 = ctk.CTkButton(frame, font=('Arial', 20), text=7, height=40, width=90, command=lambda: button_press(7))
button7.grid(padx=5, pady=5, row=2, column=0)

button8 = ctk.CTkButton(frame, font=('Arial', 20), text=8, height=40, width=90, command=lambda: button_press(8))
button8.grid(padx=5, pady=5, row=2, column=1)

button9 = ctk.CTkButton(frame, font=('Arial', 20), text=9, height=40, width=90, command=lambda: button_press(9))
button9.grid(padx=5, pady=5, row=2, column=2)

button0 = ctk.CTkButton(frame, font=('Arial', 20), text=0, height=40, width=90, command=lambda: button_press(0))
button0.grid(padx=5, pady=5, row=3, column=0)

plus = ctk.CTkButton(frame, font=('Arial', 20), text='+', height=40, width=90, command=lambda: button_press('+'))
plus.grid(padx=5, pady=5, row=0, column=3)

minus = ctk.CTkButton(frame, font=('Arial', 20), text='-', height=40, width=90, command=lambda: button_press('-'))
minus.grid(padx=5, pady=5, row=1, column=3)

multiply = ctk.CTkButton(frame, font=('Arial', 20), text='*', height=40, width=90, command=lambda: button_press('*'))
multiply.grid(padx=5, pady=5, row=2, column=3)

divide = ctk.CTkButton(frame, font=('Arial', 20), text='/', height=40, width=90, command=lambda: button_press('/'))
divide.grid(padx=5, pady=5, row=3, column=3)

equal = ctk.CTkButton(frame, font=('Arial', 20), text='=', height=40, width=90, command=equals)
equal.grid(padx=5, pady=5, row=3, column=2)

decimal = ctk.CTkButton(frame, font=('Arial', 20), text='.', height=40, width=90, command=lambda: button_press('.'))
decimal.grid(padx=5, pady=5, row=3, column=1)

clear = ctk.CTkButton(window, text='Clear', height=40, width=390, command=clear, font=('Arial', 20))
clear.pack(pady=5)

history_section = ctk.CTkLabel(window, height=600, width=390, textvariable=history_label)
history_section.pack(pady=5)

window.mainloop()
