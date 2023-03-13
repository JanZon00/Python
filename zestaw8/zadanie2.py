import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import StringVar, Button, Entry
from tkinter import filedialog
import tkinter.font as font
from tkinter import Menu
from tkinter import scrolledtext 

okno = tk.Tk()
# dodać tytuł, rozmiar
okno.title("PDF reader")
# dodać widget Text i umieściś z jakimś marginesem
scrol_w = 100
scrol_h = 40
text = scrolledtext.ScrolledText(okno, width=scrol_w, height=scrol_h, wrap=tk.WORD)
text.grid(column=0, columnspan=3) # columnspan zależy od wcześniejszego podziału

def clear_text():
   text.delete('1.0', tk.END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   file_menu.quit()
   file_menu.destroy()
   exit() 

menu_bar = Menu(okno)
okno.config(menu=menu_bar) 
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator() # pozioma kreska
file_menu.add_command(label="Quit", command=quit_app)
menu_bar.add_cascade(label="File", menu=file_menu) # add File menu to menu bar and give it a label
# utworzyć widget Menu i jego strukturę jak na rysunku
# Open powinno wołać open_pdf
# Clear powinno wołać clear_text
# Quit powinno wołać quit_app

okno.mainloop()