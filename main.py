import tkinter
from tkinter import *
from tkinter import ttk
calc = Tk()
calc.title("Calculator")
calc.minsize(500 , 190)
calc.maxsize(500 , 190)

ent_var = tkinter.StringVar()
ent = ttk.Entry(calc , width = 60 , textvariable = ent_var)
ent.pack()

st = ttk.Style()
st.configure('equal.TButton' , background = 'red')

bu1 = ttk.Button(calc , text = "7")
bu1.place(x = 90 , y = 30)
bu2 = ttk.Button(calc , text = "8")
bu2.place(x = 170 , y = 30)
bu3 = ttk.Button(calc , text = "9")
bu3.place(x = 250 , y = 30)
bu4 = ttk.Button(calc , text = "4")
bu4.place(x = 90 , y = 60)
bu5 = ttk.Button(calc , text = "5")
bu5.place(x = 170 , y = 60)
bu6 = ttk.Button(calc , text = "6")
bu6.place(x = 250 , y = 60)
bu7 = ttk.Button(calc , text = "1")
bu7.place(x = 90 , y = 90)
bu8 = ttk.Button(calc , text = "2")
bu8.place(x = 170 , y = 90)
bu9 = ttk.Button(calc , text = "3")
bu9.place(x = 250 , y = 90)
bu10 = ttk.Button(calc , text = "0")
bu10.place(x = 170, y = 120)
bu11 = ttk.Button(calc , text = "/")
bu11.place(x = 340, y = 30)
bu12 = ttk.Button(calc , text = "+")
bu12.place(x = 340, y = 60)
bu13 = ttk.Button(calc , text = "-")
bu13.place(x = 340, y = 90)
bu14 = ttk.Button(calc , text = "%")
bu14.place(x = 90, y = 120)
bu15 = ttk.Button(calc , text = "x")
bu15.place(x = 250, y = 120)
bu16 = ttk.Button(calc , text = "=")
bu16.place(x = 340, y = 120)
bu16.configure(style = 'equal.TButton')

v = ""
def click(c):
    global v
    if c == '=':
        l = []
        num = ""
        for i in range(len(v)):
            if v[i] != '+' and v[i] != '-' and v[i] != '/' and v[i] != '%' and v[i] != '*':
                num += v[i]
            else:
                if num != "":
                    l.append(num)
                l.append(v[i])
                num = ""
        if num != "":
            l.append(num)
        ans = int(l[0])
        for i in range(1 , len(l)):
            if l[i] == '+':
                ans += int(l[i+1])
            if l[i] == '-':
                ans -= int(l[i+1])
            if l[i] == '/':
                ans /= int(l[i+1])
            if l[i] == '%':
                ans %= int(l[i+1])
            if l[i] == 'x':
                ans *= int(l[i+1])
        ent_var.set(ans)
        v = ""
    else:
        v += c
        ent_var.set(v)

bu1.config(command = lambda : click('7'))
bu2.config(command = lambda : click('8'))
bu3.config(command = lambda : click('9'))
bu4.config(command = lambda : click('4'))
bu5.config(command = lambda : click('5'))
bu6.config(command = lambda : click('6'))
bu7.config(command = lambda : click('1'))
bu8.config(command = lambda : click('2'))
bu9.config(command = lambda : click('3'))
bu10.config(command = lambda : click('0'))
bu11.config(command = lambda : click('/'))
bu12.config(command = lambda : click('+'))
bu13.config(command = lambda : click('-'))
bu14.config(command = lambda : click('%'))
bu15.config(command = lambda : click('x'))
bu16.config(command = lambda : click('='))

calc.mainloop()