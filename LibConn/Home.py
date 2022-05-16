from tkinter import *
from ReturnBook import *

root = Tk()
root.title("LibConn")
root.geometry("600x500")
root.resizable(width=0, height=0)

Canvas1 = Canvas(root)
Canvas1.create_image(300, 340)
Canvas1.config(bg="white")
Canvas1.pack(expand=True, fill=BOTH)

icon1 = PhotoImage(file='img/home.png')
icon2 = PhotoImage(file='img/profile.png')
icon3 = PhotoImage(file='img/calendar.png')
icon4 = PhotoImage(file='img/bookcase.png')
icon5 = PhotoImage(file='img/wallet.png')

btn7 = Button(root, image=icon1, bg='white', fg='#d68227',
              command='')
btn7.place(relx=0.16, rely=0.12, relwidth=0.12, relheight=0.12)

btn8 = Button(root, image=icon2, bg='white', fg='#d68227',
              command='')
btn8.place(relx=0.74, rely=0.12, relwidth=0.12, relheight=0.12)

headingFrame1 = Frame(root, bg="#d68227", bd=2)
headingFrame1.place(relx=0.3, rely=0.12, relwidth=0.42, relheight=0.12)

headingLabel1 = Label(headingFrame1, text="LibConn", bg='white',
                      fg='#d68227', font=('Courier', 28, 'bold'))
headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)


btn9 = Button(root, image=icon3, bg='white', fg='#d68227', command='')
btn9.place(relx=0.3, rely=0.3, relwidth=0.12, relheight=0.12)

btn10 = Button(root, image=icon4, bg='white', fg='#d68227', command='')
btn10.place(relx=0.45, rely=0.3, relwidth=0.12, relheight=0.12)

btn11 = Button(root, image=icon5, bg='white', fg='#d68227', command='')
btn11.place(relx=0.6, rely=0.3, relwidth=0.12, relheight=0.12)

btn1 = Button(root, text="Δανεισμός", bg='white',
              fg='#d68227', font=('Courier', 12), command='')
btn1.place(relx=0.3, rely=0.45, relwidth=0.42, relheight=0.08)

btn2 = Button(root, text="Επιστροφή", bg='white',
              fg='#d68227', font=('Courier', 12), command=returnBook)
btn2.place(relx=0.3, rely=0.55, relwidth=0.42, relheight=0.08)

btn3 = Button(root, text="Προτεινόμενα", bg='white',
              fg='#d68227', font=('Courier', 12), command='')
btn3.place(relx=0.3, rely=0.65, relwidth=0.42, relheight=0.08)

btn4 = Button(root, text="Αξιολόγηση", bg='white',
              fg='#d68227', font=('Courier', 12), command='')
btn4.place(relx=0.3, rely=0.75, relwidth=0.42, relheight=0.08)

btn5 = Button(root, text="Βοήθεια", bg='white',
              fg='#d68227', font=('Courier', 12), command='')
btn5.place(relx=0.3, rely=0.85, relwidth=0.42, relheight=0.08)

root.mainloop()
