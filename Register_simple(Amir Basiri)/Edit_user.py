from tkinter import Toplevel, messagebox
from tkinter import *
from RW_data import write_json, read_json, check_read


def edit():
    def pas_validation(old_pas, new_pas, cn_pas):
        information = read_json()
        check = check_read()
        if information[check] != old_pas:
            print("Wrong old password!")
            return False
        if new_pas != cn_pas:
            print("Password and confirmation mismatch!")
            return False
        if len(new_pas) < 8:
            print("Password is too short!")
            return False
        return True

    def get():
        check = check_read()
        old_pas = old_pas_entry.get()
        new_pas = new_pas_entry.get()
        c_new_pas = c_pas_entry.get()
        result = pas_validation(old_pas, new_pas, c_new_pas)
        information = read_json()
        if result:
            information[check] = new_pas
        write_json(information)
        messagebox.showwarning("Done!","your password changed successfully!")


    check_dct = check_read()
    if check_dct == {}:
        messagebox.showwarning("Error!", "please login first!")
        return
    if check_dct == {"admin"}:
        messagebox.showwarning("Error!", "Cant edit Admin`s account!")
        return

    edit_win = Toplevel()
    edit_win.title("Edit")
    edit_win.geometry("600x400+300+200")
    edit_win.config(bg="white")
    Label(edit_win, text="Edit", width=10, height=2, bg="darkred", fg="#fff", font="arial 28 bold").pack(
        side=TOP,
        fill=X)
    Label(edit_win, text="Old Password: ", bg="white", fg="black", font="arial 12 bold").pack(side=TOP, fill=X)
    old_pas_entry =Entry(edit_win, font="arial 12 bold", bg='white')
    old_pas_entry.pack()

    Label(edit_win, text="New Password: ", bg="white", fg="black", font="arial 12 bold").pack(side=TOP, fill=X)
    new_pas_entry = Entry(edit_win, font="arial 12 bold", bg='white')
    new_pas_entry.pack()

    Label(edit_win, text="New Password Confirmation: ", bg="white", fg="black", font="arial 12 bold").pack(
        side=TOP,fill=X)
    c_pas_entry = Entry(edit_win, font="arial 12 bold", bg='white')
    c_pas_entry.pack()
    Button(edit_win, text="Edit", font="arial 12 bold", command=get).pack()





