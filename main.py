import tkinter
import fileinput
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

#File=fileinput('Cat.jpg')
#File1=fileinput('Dog.png')


def cat():
    frame = tkinter.Toplevel()
    frame.title = "Cat and Dog"
    frame.geometry = "500 X 500"
    canvas = tkinter.Canvas(frame, width=500, height=500)
    img = tkinter.PhotoImage(file="Cat.jpg")
    canvas.create_image(500, 500, anchor=NW, image=img)
    canvas.pack()


Cat_button = Button(frame, text='Cat', fg='red', command=cat)
Cat_button.pack(side=LEFT)


def Dog():
    frame = tkinter.Toplevel()
    frame.title = "Cat and Dog"
    frame.geometry = "500 X 500"
    canvas = tkinter.Canvas(frame, width=500, height=500)
    img = tkinter.PhotoImage(file='Dog.png')
    canvas.create_image(500, 500, anchor=NW, image=img)
    canvas.pack()


Dogbutton = Button(frame, text='Dog', fg='Blue', command=Dog)
Dogbutton.pack(side=RIGHT)

root.mainloop()
