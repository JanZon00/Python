import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
import tkinter.font as font
from tkinter import StringVar, Entry
from time import strftime
from tkcalendar import Calendar  # pip install tkcalendar

okno = tk.Tk()

okno.title("Kalendarz")
myFont = font.Font(family='Arial', size=50, weight='bold')
okno.geometry("600x600")
okno.resizable(False, False)

red_frame = tk.Frame(bd=0, highlightthickness=0, background="black")
red_frame.place(x=0, y=0, relwidth=1.0, relheight=.4, anchor="nw")

date_time=tk.Label(okno,font=myFont,bg='black',fg="white")
date_time.grid(row=1,column=1,padx=5,pady=25)

def update_date_time():
    label = strftime('%d %B %Y \n %A %H:%M:%S')
    date_time.config(text=label)
    date_time.after(1000, update_date_time)
    
date_time.pack(anchor="center")

current_time = datetime.now()


day = int(current_time.strftime('%d'))
month = int(current_time.strftime('%m'))
year = int(current_time.strftime('%Y'))

cal = Calendar(okno, selectmode = 'day', day=day, month=month, year=year)
 
cal.pack(pady = 120)

update_date_time()

okno.mainloop()