from tkinter import *
import os
from ReturnBook import *
from LendBook import *
from RecommendBook import *

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text=" Login success ").pack()
    Button(screen3, text="OK", command=screen3.destroy())


def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text=" Password error ").pack()
    Button(screen4, text="OK", command=screen4.destroy())


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text=" User not found ").pack()
    Button(screen5, text="OK", command=screen5.destroy())


def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info)
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(text="Registration Success")


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file = open(username1, "r")
        verify = file.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("LibConn")
    screen1.geometry("600x500")
    screen1.resizable(width=0, height=0)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    role = StringVar()

    Label(screen1, text="Εγγραφείτε στο LibConn", font=('Courier', 12), fg='#d68227').pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Τύπος * ", font=('Courier', 12), fg='#d68227').pack()
    role_entry = Entry(screen1, textvariable=role)
    role_entry.pack()
    Label(screen1, text="Όνομα * ", font=('Courier', 12), fg='#d68227').pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Κωδικός * ", font=('Courier', 12), fg='#d68227').pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Υποβολή", font=('Courier', 12), fg='#d68227',bg='white', width=10, height=1, command=home_screen).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("LibConn")
    screen2.geometry("600x500")
    screen2.resizable(width=0, height=0)
    Label(screen2, text="Εισάγετε τα στοιχεία σας", font=('Courier', 12), fg='#d68227').pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Όνομα * ", font=('Courier', 12), fg='#d68227').pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Κωδικός * ", font=('Courier', 12), fg='#d68227').pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Υποβολή", font=('Courier', 12), fg='#d68227',bg='white', width=10, height=1, command=home_screen).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x500")
    screen.title("LibConn")
    screen.resizable(width=0, height=0)
    Label(text="LibConn", fg='#d68227', width="300",
          height="2", font=("Courier", 28, 'bold')).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Είσοδος", height="2", width="30", bg='white',
           fg='#d68227', font=('Courier', 12), command=login).pack()
    Label(text="").pack()
    Button(text="Εγγραφή", height="2", width="30", bg='white',
           fg='#d68227', font=('Courier', 12), command=register).pack()

    screen.mainloop()

def home_screen():

    global screen6, Canvas1, icon1, icon2, icon3, icon4, icon5, btn1, btn2, btn3, btn4, btn5, btn7, btn8, btn9, headingFrame1, headingLabel1

    screen6 = Toplevel(screen)
    screen6.title("LibConn")
    screen6.geometry("600x500")
    screen6.resizable(width=0, height=0)

    Canvas1 = Canvas(screen6)
    Canvas1.create_image(300, 340)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    icon1 = PhotoImage(file='img/home.png')
    icon2 = PhotoImage(file='img/profile.png')
    icon3 = PhotoImage(file='img/calendar.png')
    icon4 = PhotoImage(file='img/bookcase.png')
    icon5 = PhotoImage(file='img/wallet.png')

    btn7 = Button(screen6, image=icon1, bg='white', fg='#d68227',
                command='')
    btn7.place(relx=0.16, rely=0.12, relwidth=0.12, relheight=0.12)

    btn8 = Button(screen6, image=icon2, bg='white', fg='#d68227',
                command='')
    btn8.place(relx=0.74, rely=0.12, relwidth=0.12, relheight=0.12)

    headingFrame1 = Frame(screen6, bg="#d68227", bd=2)
    headingFrame1.place(relx=0.3, rely=0.12, relwidth=0.42, relheight=0.12)

    headingLabel1 = Label(headingFrame1, text="LibConn", bg='white',
                        fg='#d68227', font=('Courier', 28, 'bold'))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)


    btn9 = Button(screen6, image=icon3, bg='white', fg='#d68227', command='')
    btn9.place(relx=0.3, rely=0.3, relwidth=0.12, relheight=0.12)

    btn10 = Button(screen6, image=icon4, bg='white', fg='#d68227', command='')
    btn10.place(relx=0.45, rely=0.3, relwidth=0.12, relheight=0.12)

    btn11 = Button(screen6, image=icon5, bg='white', fg='#d68227', command='')
    btn11.place(relx=0.6, rely=0.3, relwidth=0.12, relheight=0.12)

    btn1 = Button(screen6, text="Δανεισμός", bg='white',
                fg='#d68227', font=('Courier', 12), command=lendBook)
    btn1.place(relx=0.3, rely=0.45, relwidth=0.42, relheight=0.08)

    btn2 = Button(screen6, text="Επιστροφή", bg='white',
                fg='#d68227', font=('Courier', 12), command=returnBook)
    btn2.place(relx=0.3, rely=0.55, relwidth=0.42, relheight=0.08)

    btn3 = Button(screen6, text="Προτεινόμενα", bg='white',
                fg='#d68227', font=('Courier', 12), command=recommendBook)
    btn3.place(relx=0.3, rely=0.65, relwidth=0.42, relheight=0.08)

    btn4 = Button(screen6, text="Αξιολόγηση", bg='white',
                fg='#d68227', font=('Courier', 12), command='')
    btn4.place(relx=0.3, rely=0.75, relwidth=0.42, relheight=0.08)

    btn5 = Button(screen6, text="Βοήθεια", bg='white',
                fg='#d68227', font=('Courier', 12), command='')
    btn5.place(relx=0.3, rely=0.85, relwidth=0.42, relheight=0.08)



main_screen()
