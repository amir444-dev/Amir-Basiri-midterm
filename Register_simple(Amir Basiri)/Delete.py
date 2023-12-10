from tkinter import messagebox
from tkinter.messagebox import askyesno

from RW_data import read_json, write_json, check_read


def delete():
    def confirm(check_dct):
        answer = askyesno(title='Confirmation',message='Are you sure?')
        if answer:
            information = read_json()
            information.pop(check_dct)
            write_json(information)
            messagebox.showwarning("Done!", "Your account has been deleted!")
            check_dct = {}
            return check_dct

    check_dct = check_read()
    if check_dct == {}:
        messagebox.showwarning("Error!", "please login first!")
        return
    if check_dct == {"admin"}:
        messagebox.showwarning("Error!", "Admin account is not removable!")
        return
    confirm(check_dct)


