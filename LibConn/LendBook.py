from tkinter import *

def lendBook():

    global SubmitBtn, Canvas1, root, labelFrame

    root = Tk()
    root.title("Αναζήτηση Βιβλίου")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    lb1 = Label(labelFrame,text="Τίτλος: ", bg='white', fg='#d68227', font=('Courier', 10))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=chooseLib)
    SubmitBtn.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.08)

    root.mainloop()


def chooseLib():

    root = Tk()
    root.title("Επιλογή Βιβλιοθήκης")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)
    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    Label(labelFrame, text='Βιβλιοθήκη\t\t\t\tΔιαθεσιμότητα', bg='white', font=('Courier', 10), fg='#d68227').place(relx=0.07, rely=0.0)
    Label(labelFrame, text="______________________________________________________________________________________",
          bg='white', fg='#d68227').place(relx=0.07, rely=0.05)
    # Change the label text
    def getTime():
        label.config( text = clicked.get() )
    
    # Dropdown menu options
    options = [
        "1 εβδομάδα",
        "2 εβδομάδες",
        "3 εβδομάδες",
        "1 μήνας"
    ]
    
    # datatype of menu text
    clicked = StringVar()
    
    # initial menu text
    clicked.set("1 εβδομάδα")
    
    # Create Dropdown menu
    drop = OptionMenu( root , clicked , *options )
    drop.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.08)
    
    # Create button, it will change label text
    Btn = Button(root, text="Αλλαγή Χρόνου", bg='#d68227',
                       font=('Courier', 10), fg='white', command=getTime)
    Btn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)
    
    # Create Label
    label = Label( root , text = "1 εβδομάδα" , font='Courier')
    label.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.08)

    SubmitBtn = Button(root, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=noMoney)
    SubmitBtn.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.08)

    root.mainloop()

def noAvail():
    root = Tk()
    root.title("Πρόβλημα 1")
    root.geometry("440x100")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label( root , text = "Το βιβλίο δεν είναι διαθέσιμο :-(\nΘέλετε να το προσθέσετε στη wishlist;" , bg='white', fg='#d68227', font=('Courier',10))
    label.place(relx=0.15, rely=0.1)

    BtnYes = Button(root, text="Ναι", bg='#d68227',
                       font=('Courier', 10), fg='white', command='')
    BtnYes.place(relx=0.3, rely=0.55)

    BtnNo = Button(root, text="Όχι", bg='#d68227',
                       font=('Courier', 10), fg='white', command=root.destroy)
    BtnNo.place(relx=0.6, rely=0.55)

    root.mainloop()

def noMoney():
    root = Tk()
    root.title("Πρόβλημα 2")
    root.geometry("440x100")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label( root , text = "Ο λογαριασμός σας δεν έχει αρκετά credits :-(\nΘέλετε να προσθέσετε;" , bg='white', fg='#d68227', font=('Courier', 10))
    label.place(relx=0.15, rely=0.1)

    BtnYes = Button(root, text="Ναι", bg='#d68227',
                       font=('Courier', 10), fg='white', command='')
    BtnYes.place(relx=0.3, rely=0.55)

    BtnNo = Button(root, text="Όχι", bg='#d68227',
                       font=('Courier', 10), fg='white', command=root.destroy)
    BtnNo.place(relx=0.6, rely=0.55)

    root.mainloop()
