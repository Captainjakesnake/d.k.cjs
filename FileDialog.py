from tkinter import *
from tkinter import filedialog as fd

def insert_text():
    file_name = fd.askopenfilename()
    f =open(file_name)
    s= f.read()
    text.insert(1.0,s)
    f.close()

def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes =(("TXT files","*.txt"),
                    ("HTML files","*.html; *.htm"),
                    ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

def font_text(event,font):
    text['font'] = font

def color_text(event, color):
    text['fg'] = color

root = Tk()
text = Text(width = 50, height = 25)
text.grid(columnspan=2,row = 0)

b1 = Button(text="Открыть", command = insert_text)
b1.grid(row=1, sticky = E)
b2 = Button(text = "Save",command = extract_text)
b2.grid(row=1,column=1,sticky = W)
b3 = Button(text="Шрифт" )
b3.grid(row=2, column=1, sticky = W)
b3.bind('<Button-1>', lambda e, f= 'Arial': font_text(e,f))
b3.bind('<Button-3>', lambda e, f= 'Tahoma': font_text(e,f))
b4 = Button(text="Цвет Текста" )
b4.grid(row=2,sticky = E)
b4.bind('<Button-1>', lambda e, c= 'red': color_text(e,c))
b4.bind('<Button-3>', lambda e, c= 'green': color_text(e,c))
root.mainloop()