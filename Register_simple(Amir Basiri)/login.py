import tkinter
from tkinter import *
from tkinter import messagebox
from RW_data import read_json,check_read,check_write


def login():
    def get():
        user = user_entry.get()
        pas = pas_entry.get()
        if (user in information) and (information[user] == pas):
            messagebox.showwarning("Welcome!", "Welcome to your account!")
            check_write(user)
        else:
            messagebox.showwarning("Error!","Wrong username or password!")

    information = read_json()
    check_dct= check_read()
    if check_dct != {}:
        messagebox.showwarning("Error!","You are already logged in!")
        return

    login_win = Toplevel()
    login_win.title("Login")
    login_win.geometry("600x400+300+200")
    login_win.config(bg="white")
    Label(login_win, text="LOGIN", width=10, height=2, bg="darkred", fg="#fff", font="arial 28 bold").pack(
        side=TOP,
        fill=X)
    Label(login_win, text="Username: ", bg="white", fg="black", font="arial 12 bold").pack(side=TOP, fill=X)
    user_entry = tkinter.Entry(login_win, font="arial 12 bold", bg='white')
    user_entry.pack()
    Label(login_win, text="Password: ", bg="white", fg="black", font="arial 12 bold").pack(side=TOP, fill=X)
    pas_entry = Entry(login_win, font="arial 12 bold", bg='white')
    pas_entry.pack()
    Button(login_win, text="Login", font="arial 12 bold", command=get).pack()

