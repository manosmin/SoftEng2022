from tkinter import *


def viewborrowed():

    root = Tk()
    root.title("Δανεισμένα Βιβλία")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    Label(labelFrame, text="%-10s%-10s%-20s%-10s" % ('ID', 'Τίτλος', 'Συγγραφέας',
          'Κατάσταση'), bg='white', font=('Courier', 10), fg='#d68227').place(relx=0.07, rely=0.0)
    Label(labelFrame, text="___________________________________________________________________________________",
          bg='white', fg='#d68227').place(relx=0.07, rely=0.05)

    SubmitBtn = Button(root, text="Βαθμολόγηση", bg='#d68227',
                       font=('Courier', 10), fg='white', command=EvaluationBook)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    root.mainloop()  

def EvaluationBook():
    root = Tk()
    root.title("Αξιολόγηση βιβλίου")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    Label(labelFrame, text="%-10s%-10s%-20s%-10s" % ('ID', 'Τίτλος', 'Συγγραφέας',
          'Κατάσταση'), bg='white', font=('Courier', 10), fg='#d68227').place(relx=0.07, rely=0.0)
    Label(labelFrame, text="___________________________________________________________________________________",
          bg='white', fg='#d68227').place(relx=0.07, rely=0.05)

    # Change the label text
    def getTime():
        label.config( text = clicked.get() )   
    
    # Dropdown menu options
    options = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
    ] 
    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("1")
    
    # Create Dropdown menu
    drop = OptionMenu( root , clicked , *options )
    drop.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.08)
    
    # Create button, it will change label text
    Btn = Button(root, text="Εισαγωγή βαθμού", bg='#d68227',
                       font=('Courier', 10), fg='white', command=getTime)
    Btn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

     # Create Label
    label = Label( root , text = "Βαθμός" , font='Courier')
    label.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.08)

    SubmitBtn = Button(root, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=introcriticism)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)
      
    root.mainloop()

def introcriticism():

    root = Tk()
    root.title("Εισαγωγή κριτικής")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.75)

    label = Label(labelFrame, text="\n Γράψτε μια κριτική για το βιβλίο!",
                  bg='white', fg='#d68227', font='Courier')
    label.place(relx=0.05, rely=0.1)

    lb1 = Label(labelFrame, text="Τίτλος: ", bg='white',
                fg='#d68227', font=('Courier', 10))
    lb1.place(relx=0.05, rely=0.3, relheight=0.08)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.25, rely=0.3, relwidth=0.62, relheight=0.08)
    BtnOk = Button(root, text="Υποβολή", bg='#d68227',
                   font=('Courier', 10), fg='white', command=message2)
    BtnOk.place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.08)


def message2():
    root = Tk()
    root.title("Καταχώρηση κριτικής")
    root.geometry("440x100")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label( root , text = "Η κριτική καταχωρήθηκε" , bg='white', fg='#d68227', font=('Courier',10))
    label.place(relx=0.15, rely=0.1)

    BtnYes = Button(root, text="ΟΚ", bg='#d68227',
                       font=('Courier', 10), fg='white', command=average)
    BtnYes.place(relx=0.3, rely=0.55)

    root.mainloop()


def average():
    root = Tk()
    root.title("Ανανέωση του μέσου όρου βαθμολογίας")
    root.geometry("440x100")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label( root , text = "Ο μέσος όρος ανανεώθηκε" , bg='white', fg='#d68227', font=('Courier',10))
    label.place(relx=0.15, rely=0.1)

    BtnYes = Button(root, text="ΟΚ", bg='#d68227',
                       font=('Courier', 10), fg='white', command=evall)
    BtnYes.place(relx=0.3, rely=0.55)

    root.mainloop()

def evall():
    root = Tk()
    root.title("Καταχώρηση αξιολόγησης")
    root.geometry("440x100")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label( root , text = "Η αξιολόγηση σας καταχωρήθηκε" , bg='white', fg='#d68227', font=('Courier',10))
    label.place(relx=0.15, rely=0.1)

    BtnYes = Button(root, text="ΟΚ", bg='#d68227',
                       font=('Courier', 10), fg='white', command=incredits)
    BtnYes.place(relx=0.3, rely=0.55)

    root.mainloop()

def incredits():
    root = Tk()
    root.title("Προσθήκη credits")
    root.geometry("440x100")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label( root , text = "Προστέθηκαν credits στο λογαριασμό σας" , bg='white', fg='#d68227', font=('Courier',10))
    label.place(relx=0.15, rely=0.1)

    BtnYes = Button(root, text="ΟΚ", bg='#d68227',
                       font=('Courier', 10), fg='white', command=root.destroy)
    BtnYes.place(relx=0.3, rely=0.55)

    root.mainloop()