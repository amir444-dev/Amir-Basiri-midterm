import tkinter
from tkinter import *

import Logout
from RW_data import read_json, check_read, check_write
import Delete
import Edit_user
import login
import submit


def gotosub():
    submit.submit()


def gotolog():
    login.login()


def gotodel():
    Delete.delete()


def gotoed():
    Edit_user.edit()


def gotolo():
    Logout.logout()


check = {}
check_dct = check_write(check)
information = read_json()

win = tkinter.Tk()
win.title("User Registration")
win.geometry('960x800+210+100')
win.config(bg="white")
Label(win, text="USER REGISTRATION", width=10, height=2, bg="darkred", fg="#fff", font="arial 28 bold").pack(side=TOP,
                                                                                                             fill=X)
Label(win, text="What is your plan?\n", bg="white", fg="black", font="arial 28 bold").pack()
# ---------------------button`s
btn1 = Button(win, text="Submit", font="arial 24 bold", command=gotosub)
btn1.pack(padx=10, pady=10)

btn2 = Button(win, text="Login", command=gotolog, font="arial 24 bold")
btn2.pack(padx=10, pady=10)

btn3 = Button(win, text="Delete", command=gotodel, font="arial 24 bold")
btn3.pack(padx=10, pady=10)


btn5 = Button(win, text="Logout", command=gotolo, font="arial 24 bold")
btn5.pack(padx=10, pady=10)

btn4 = Button(win, text="Edit", command=gotoed, font="arial 24 bold")
btn4.pack(padx=10, pady=10)

win.mainloop()
