from tkinter import *
from tkinter import messagebox
from RW_data import read_json, write_json


# -------------------------------------------------------------------------------------
def submit():
    information = read_json()

    def get():
        user = user_entry.get()
        pas = pas_entry.get()
        c_pas = c_pas_entry.get()
        result = validation(user, pas, c_pas)
        if result:
            information[user_entry.get()] = pas_entry.get()
            write_json(information)
            messagebox.showwarning("Done!", "You have successfully registered!")

    submit_win = Toplevel()
    submit_win.title("Submit")
    submit_win.geometry("600x400+300+200")
    submit_win.config(bg="white")
    Label(submit_win, text="SUBMIT", width=10, height=2, bg="darkred", fg="#fff", font="arial 28 bold").pack(
        side=TOP,
        fill=X)
    Label(submit_win, text="Username: ", bg="white", fg="black", font="arial 12 bold").pack(side=TOP, fill=X)
    user_entry = Entry(submit_win, font="arial 12 bold", bg='white')
    user_entry.pack()
    Label(submit_win, text="Password: ", bg="white", fg="black", font="arial 12 bold").pack(side=TOP, fill=X)
    pas_entry = Entry(submit_win, font="arial 12 bold", bg='white')
    pas_entry.pack()
    Label(submit_win, text="Password Confirmation: ", bg="white", fg="black", font="arial 12 bold").pack(side=TOP,
                                                                                                         fill=X)
    c_pas_entry = Entry(submit_win, font="arial 12 bold", bg='white')
    c_pas_entry.pack()
    Button(submit_win, text="Submit", font="arial 12 bold", command=get).pack()

    def validation(user, pas, c_pas):
        check = read_json()
        if user in check:
            messagebox.showwarning("Error!", "Username Already Registered!")
            return
        if len(pas) < 8:
            messagebox.showwarning(
                "Password Error", "Password is too short!")
            submit_win.destroy()
            return False
        if pas != c_pas:
            messagebox.showwarning(
                "Password Error", "password and confirmation doesnt match!")
            submit_win.destroy()
            return False
        return True

    submit_win.mainloop()
