import tkinter as tk
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)
def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)
def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)
def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)
def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)
window = tk.Tk()
window.title('Калькулятор')
window.geometry("600x800")
window.resizable(False, False)
window.configure(bg='#1E1E1E')
button_add = tk.Button(window, text= '+', bg='#444444', fg='#FFFFFF', font='Comfortaa 32', width=3, height=2, command=add)
button_add.place (x= 95, y=504)
button_sub = tk.Button(window, text= '-', bg='#444444', fg='#FFFFFF', font='Comfortaa 32', width=3, height=2, command=sub)
button_sub.place (x= 200, y=504)
button_mul = tk.Button(window, text= '*', bg='#444444', fg='#FFFFFF', font='Comfortaa 32', width=3, height=2, command=mul)
button_mul.place (x= 305, y=504)
button_div = tk.Button(window, text= '/', bg='#444444', fg='#FFFFFF', font='Comfortaa 32', width=3, height=2, command=div)
button_div.place (x= 410, y=504)
number1_entry = tk.Entry(window, bg='#444444', fg='#FFFFFF', font='Comfortaa 28', width=20)
number1_entry.place (x= 50, y= 100)
number2_entry = tk.Entry(window, bg='#444444', fg='#FFFFFF', font='Comfortaa 28', width=20)
number2_entry.place (x= 50, y= 210)
answer_entry = tk.Entry(window, bg='#444444', fg='#FFFFFF', font='Comfortaa 28', width=20)
answer_entry.place (x= 50, y= 360)
number1 = tk.Label(window, text='Введите первое число:', bg='#1E1E1E', fg='#FFFFFF', font='Comfortaa 16')
number1.place (x= 50, y= 60)
number2 = tk.Label(window, text='Введите второе число:', bg='#1E1E1E', fg='#FFFFFF', font='Comfortaa 16')
number2.place (x= 50, y= 170)
answer = tk.Label(window, text='Результат:', bg='#1E1E1E', fg='#FFFFFF', font='Comfortaa 16')
answer.place (x= 50, y= 320)
window.mainloop()