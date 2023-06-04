def mulai():
          user= input("username:")

import getpass
password = getpass.getpass()
if password =="2003"and user == "kalumata":

    print("login berhasil congratsss")
    from tkinter import *
    import time

    root = Tk()
    root.resizable(FALSE, FALSE)
    root.title("Jam Digital")

    def waktu():
        x = time.strftime("%H:%M:%S:%p")
        label.config(text=x)
        label.after(200, waktu)

    label = Label(root, bg="black", fg="light blue", font="calibri 100 bold")
    label.pack()

    waktu()

    root.mainloop()

else  :
    print ("user atau pass salah silakan coba lagi")
    mulai()
mulai()
