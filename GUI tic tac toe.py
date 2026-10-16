from tkinter import *
from tkinter import messagebox

import pyttsx3
e=pyttsx3.init()

root = Tk()

t=1
def restart():
    global t
    t=1
    b1.config(text="")
    b2.config(text="")
    b3.config(text="")
    b4.config(text="")
    b5.config(text="")
    b6.config(text="")
    b7.config(text="")
    b8.config(text="")


def winner():
    a1=b1["text"]
    a2=b2["text"]
    a3=b3["text"]
    a4=b4["text"]
    a5=b5["text"]
    a6=b6["text"]
    a7=b7["text"]
    a8=b8["text"]
    a9=b9["text"]

    if  (a1=="x" and a2=="x" and a3=="x") or (a4=="x" and a5=="x" and a6=="x") or (a7=="x" and a8=="x" and a9=="x") or (a1=="x" and a4=="x" and a7=="x") or (a2=="x" and a5=="x" and a8=="x") or (a3=="x" and a6=="x" and a9=="x")or (a1=="x" and a5=="x" and a9=="x")or (a3=="x" and a7=="x" and a7=="x"):
        messagebox.showinfo("result","player1wins")
        e.say("winner player 1")
        restart()
    if(a1=="o" and a2=="o" and a3=="o")or (a4=="o" and a5=="o" and a6=="o")or (a7=="o" and a8=="o" and a9=="o")or (a1=="o" and a4=="o" and a7=="o")or (a2=="o" and a5=="o" and a8=="o")or (a3=="o" and a6=="o" and a9=="o")or (a1=="o" and a5=="o" and a9=="o")or (a3=="o" and a5=="o" and a7=="o"):
        print("player2wins")
        e.say("winner player 2")
        restart()
    global  t
    if t==10:
        print("Draw")


def show1():
  if b1["text"]=="":
    global t
    if t%2==1:
       b1.config(text="x")
    else:
       b1.config(text="o")
    t=t+1
    winner()
def show2():
  if b2["text"]=="":
    global t
    if t%2==1:
       b2.config(text="x")
    else:
        b2.config(text="o")
    t=t+1
    winner()
def show3():
  if b3["text"]=="":
    global t
    if t%2==1:
        b3.config(text="x")
    else:
        b3.config(text="o")
    t=t+1
    winner()
def show4():
  if b4["text"]=="":
    global t
    if t%2==1:
        b4.config(text="x")
    else:
        b4.config(text="o")
    t=t+1
    winner()
def show5():
  if b5["text"]=="":
    global t
    if t%2==1:
        b5.config(text="x")
    else:
        b5.config(text="o")
    t=t+1
    winner()
def show6():
  if b6["text"]=="":
    global t
    if t%2==1:
        b6.config(text="x")
    else:
        b6.config(text="o")
    t=t+1
    winner()
def show7():
  if b7["text"]=="":
    global t
    if t%2==1:
        b7.config(text="x")
    t=t+1
    winner()
def show8():
  if b8["text"]=="":
    global t
    if t%2==1:
        b8.config(text="x")
    else:
        b8.config(text="o")
    t=t+1
    winner()
def show9():
  if b9["text"]=="":
    global t
    if t%2==1:
        b9.config(text="x")
    else:
        b9.config(text="o")
    t=t+1
    winner()

b1 = Button(root, text="", command=show1, width=5, height=2)
b2 = Button(root, text="", command=show2, width=5, height=2)
b3 = Button(root, text="", command=show3, width=5, height=2)
b4 = Button(root, text="", command=show4, width=5, height=2)
b5 = Button(root, text="", command=show5, width=5, height=2)
b6 = Button(root, text="", command=show6, width=5, height=2)
b7 = Button(root, text="", command=show7, width=5, height=2)
b8 = Button(root, text="", command=show8, width=5, height=2)
b9 = Button(root, text="", command=show9, width=5, height=2)

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)




mainloop()