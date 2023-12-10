from tkinter import messagebox
from tkinter.messagebox import askyesno
from RW_data import read_json, check_read, check_write


def logout():
    check_dct = check_read()
    if check_dct != {}:
        answer = askyesno(title='Confirmation', message='You are logging out\nAre you sure?')
        if answer:
            check_dct = {}
            check_write(check_dct)
            messagebox.showwarning("Done", "Logged out successfully!")
            return
    else:
        messagebox.showwarning("Error!","Please login first!")
