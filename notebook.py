from tkinter import*
from tkinter import ttk
window=Tk()
window.title('окно2')
window.geometry('400x250')
tab_control = ttk.Notebook(window)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab_control.add(tab1,text='Первая')
tab_control.add(tab2,text='Вторая')
lbl1=Label(tab1,text='Вкладка1')
lbl1.grid(column=0,row=0)
lbl2=Label(tab2,text='Вкладка2')
lbl2.grid(column=0,row=0)
tab_control.pack(expand=1,fill='both')
window.mainloop()