from tkinter import *
from LendBook import chooseLib

def recommendBook():

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

    SubmitBtn = Button(root, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=makeRecommendation)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    root.mainloop()

def similarBooks():

    root = Tk()
    root.title("Προτεινόμενα Βιβλία")
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

    SubmitBtn = Button(root, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=chooseLib)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    root.mainloop()

def makeRecommendation():

    root = Tk()
    root.title("Αναζήτηση Βιβλίου")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.75)

    label = Label( labelFrame , text = "\n Αναζητήστε ένα βιβλίο για να λάβετε προτάσεις!" , bg='white', fg='#d68227', font='Courier')
    label.place(relx=0.05, rely=0.1)
    
    lb1 = Label(labelFrame,text="Τίτλος: ", bg='white', fg='#d68227', font=('Courier', 10))
    lb1.place(relx=0.05,rely=0.3, relheight=0.08)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.25,rely=0.3, relwidth=0.62, relheight=0.08)
    BtnOk = Button(root, text="Αναζήτηση", bg='#d68227',
                       font=('Courier', 10), fg='white', command=similarBooks)
    BtnOk.place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.08)

    root.mainloop()
