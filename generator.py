import tkinter
from tkinter import messagebox

text = "0"

top = tkinter.Tk()
top.geometry("500x200")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", inputEmptyStar.get())

def updateTable():
    text = count.get()
    for c in range(0,int(text)):
        tkinter.Label(text=c, relief=tkinter.RIDGE,width=15).grid(row=c+5,column=0)
        tkinter.Entry(relief=tkinter.SUNKEN,width=10).grid(row=c+5,column=1)

tkinter.Label(text="Empty Star: ", relief=tkinter.RIDGE,width=20).grid(row=1,column=0)
tkinter.Entry(bg="yellow", relief=tkinter.SUNKEN,width=30).grid(row=1,column=1)
tkinter.Label(text="Full Star: ", relief=tkinter.RIDGE,width=20).grid(row=2,column=0)
tkinter.Entry(bg="yellow", relief=tkinter.SUNKEN,width=30).grid(row=2,column=1)
tkinter.Label(text="Max skill points: ", relief=tkinter.RIDGE,width=20).grid(row=3,column=0)
count = tkinter.Entry(bg="green", relief=tkinter.SUNKEN,width=30, textvariable=text)
count.grid(row=3,column=1)
tkinter.Button(text="Update!", bg="green", relief=tkinter.SUNKEN,width=30, command=updateTable).grid(row=3, column=2)


top.mainloop()
