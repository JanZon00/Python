import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry =  Entry(okno, bd=5, width=25, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

def delete():
    ans_entry.delete(first=0,last=100)

# przykładowy pierwszy Button 
btn_1 = Button(okno, text="1", padx=30, pady=5)
btn_1['font'] = myFont
btn_1.grid(row=1, column=0)

btn_2 = Button(okno, text="2", padx=30, pady=5)
btn_2['font'] = myFont
btn_2.grid(row=1, column=1)

btn_3 = Button(okno, text="3", padx=30, pady=5)
btn_3['font'] = myFont
btn_3.grid(row=1, column=2)

btn_4 = Button(okno, text="4", padx=30, pady=5)
btn_4['font'] = myFont
btn_4.grid(row=2, column=0)

btn_5 = Button(okno, text="5", padx=30, pady=5)
btn_5['font'] = myFont
btn_5.grid(row=2, column=1)

btn_6 = Button(okno, text="6", padx=30, pady=5)
btn_6['font'] = myFont
btn_6.grid(row=2, column=2)

btn_7 = Button(okno, text="7", padx=30, pady=5)
btn_7['font'] = myFont
btn_7.grid(row=3, column=0)

btn_8 = Button(okno, text="8", padx=30, pady=5)
btn_8['font'] = myFont
btn_8.grid(row=3, column=1)

btn_9 = Button(okno, text="9", padx=30, pady=5)
btn_9['font'] = myFont
btn_9.grid(row=3, column=2)

btn_10 = Button(okno, text="C", command=delete, padx=30, pady=5)
btn_10['font'] = myFont
btn_10.grid(row=4, column=0)

btn_11 = Button(okno, text="0", padx=30, pady=5)
btn_11['font'] = myFont
btn_11.grid(row=4, column=1)

btn_12 = Button(okno, text="=", command=delete, padx=30, pady=5)
btn_12['font'] = myFont
btn_12.grid(row=4, column=2)

btn_13 = Button(okno, text="/", padx=30, pady=5)
btn_13['font'] = myFont
btn_13.grid(row=1, column=3)

btn_14 = Button(okno, text="*", padx=30, pady=5)
btn_14['font'] = myFont
btn_14.grid(row=2, column=3)

btn_15 = Button(okno, text="-", padx=30, pady=5)
btn_15['font'] = myFont
btn_15.grid(row=3, column=3)

btn_16 = Button(okno, text="+", padx=30, pady=5)
btn_16['font'] = myFont
btn_16.grid(row=4, column=3)



# proponuje dopisywac do slownika trzy elementy:
# num_1, num_2, oper wraz z wartościami
equation = {} 
equation["num_1"] = ""
equation["num_2"] = ""
equation["oper"] = ""

def mouse_button_release(event):
    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789":
        ans_entry.insert(len(ans_entry.get()), text)
        if(equation["oper"] == ""):
            equation["num_1"] = equation["num_1"] + text
        else:
            equation["num_2"] = equation["num_2"] + text 
        
    if text in "+-*/":
        if(equation["oper"] != ""):
            pass
        else:
            ans_entry.insert(len(ans_entry.get()), text)
            equation["oper"] = text

    if text == "C":
        equation["oper"] = ""
        equation["num_1"] = ""
        equation["num_2"] = ""

    if text == "=":
        num1 = float(equation["num_1"])
        num2 = float(equation["num_2"])
        if(equation["oper"] == "+"):
            result = num1 + num2
            result = '%g'%(result)
        elif(equation["oper"] == "-"):
            result = num1 - num2
            result = '%g'%(result)
        elif(equation["oper"] == "*"):
            result = num1 * num2
            result = '%g'%(result)
        else:
            if(num2 == 0):
                ans_entry.insert(len(ans_entry.get()), "ERROR")
            else:
                result = num1 / num2
                result = '%g'%(result)
           
        ans_entry.insert(len(ans_entry.get()), result)
        equation["oper"] = ""
        equation["num_1"] = str(result)
        equation["num_2"] = ""

# sposób na reakcję 
okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()
