from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from User import *
from Inventory import *
from Issued import *
from Book import *
from Reader import *
from Rating import *
from TechnicalSupport import *

class main:
    global inventoryList, issuedList, bookList, usersList, bookHistory, r1
    # Creating objects
    u1 = User("Library1", "Library")
    u2 = User("Library2", "Library")
    u3 = User("Library3", "Library")
    b1 = Book("Book1", "Author1", "Drama", 0, " ")
    b2 = Book("Book2", "Author2", "Comedy", 0, " ")
    b3 = Book("Book3", "Author3", "Thriller", 0, " ")
    r1 = Reader('Reader1', 500, 32, 'Patras', 'Romance')
    r2 = Reader('Reader2', 500, 57, 'Heraklion', 'History')
    print('Books: ')
    print(b1.bookTitle, b2.bookTitle, b3.bookTitle)
    print('Libraries: ')
    print(u1.userName, u2.userName, u3.userName)
    print('Readers: ')
    print(r1.userName, r2.userName)
    # Adding books to libraries' inventory
    i1 = Inventory(u2.userName, b1.bookTitle, 1)
    i2 = Inventory(u2.userName, b2.bookTitle, 1)
    i3 = Inventory(u3.userName, b2.bookTitle, 1)
    i4 = Inventory(u1.userName, b3.bookTitle, 1)
    i5 = Inventory(u2.userName, b3.bookTitle, 1)

    # Creating lists for objects
    usersList = [u1, u2, u3, r1, r2]
    inventoryList = [i1, i2, i3, i4, i5]
    bookList = [b1, b2, b3]
    issuedList = []
    bookHistory = []


def register():
    global username, screen1
    screen1 = Toplevel(screen)
    screen1.title("LibConn")
    screen1.geometry("600x500")
    screen1.resizable(width=0, height=0)

    username = StringVar()
    password = StringVar()
    type = StringVar()

    def bind5():
        global u
        # Create user object
        u = Reader(username.get(), 0, 0, ' ', ' ')
        # Set variables for user
        u.registerReader(55,250, 'Timbuktu', 'Sci-Fi')
        # Add user to usersList 
        u.addUserToList(usersList)
        screen1.wm_state('withdrawn')
        screen.wm_state('withdrawn')
        home_screen()

    Label(screen1, text="Εγγραφείτε στο LibConn",
          font=('Courier', 12), fg='#d68227').pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Τύπος * ", font=('Courier', 12), fg='#d68227').pack()
    type_entry = Entry(screen1, textvariable=type)
    type_entry.pack()
    Label(screen1, text="Όνομα * ", font=('Courier', 12), fg='#d68227').pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Κωδικός * ", font=('Courier', 12), fg='#d68227').pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Υποβολή", font=('Courier', 12), fg='#d68227',
           bg='white', width=10, height=1, command=bind5).pack()


def login():
    global username, screen1
    screen1 = Toplevel(screen)
    screen1.title("LibConn")
    screen1.geometry("600x500")
    screen1.resizable(width=0, height=0)
    Label(screen1, text="Εισάγετε τα στοιχεία σας",
          font=('Courier', 12), fg='#d68227').pack()
    Label(screen1, text="").pack()
    username = StringVar()
    password = StringVar()

    def bind6():
        global u
        # Create user object
        u = Reader(username.get(), 0, 0, ' ', ' ')
        # Set variables for user
        u.registerReader(55, 250, 'Timbuktu', 'Sci-Fi')
        # Add user to usersList 
        u.addUserToList(usersList)
        screen1.wm_state('withdrawn')
        screen.wm_state('withdrawn')
        home_screen()

    Label(screen1, text="Όνομα * ", font=('Courier', 12), fg='#d68227').pack()
    username_entry1 = Entry(screen1, textvariable=username)
    username_entry1.pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Κωδικός * ", font=('Courier', 12), fg='#d68227').pack()
    password_entry1 = Entry(screen1, textvariable=password, show="*")
    password_entry1.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Υποβολή", font=('Courier', 12), fg='#d68227',
           bg='white', width=10, height=1, command=bind6).pack()


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
    global icon1, icon2, icon3, icon4, icon5

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

    btn9 = Button(screen6, image=icon3, bg='white', fg='#d68227', command=chooseDate)
    btn9.place(relx=0.3, rely=0.3, relwidth=0.12, relheight=0.12)

    btn10 = Button(screen6, image=icon4, bg='white', fg='#d68227', command=recommendBook)
    btn10.place(relx=0.45, rely=0.3, relwidth=0.12, relheight=0.12)

    btn11 = Button(screen6, image=icon5, bg='white', fg='#d68227', command=creditsSystem)
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
                  fg='#d68227', font=('Courier', 12), command=viewborrowed)
    btn4.place(relx=0.3, rely=0.75, relwidth=0.42, relheight=0.08)

    btn5 = Button(screen6, text="Βοήθεια", bg='white',
                  fg='#d68227', font=('Courier', 12), command=techSupport)
    btn5.place(relx=0.3, rely=0.85, relwidth=0.42, relheight=0.08)


def lendBook():

    global bookInfo1, root4
    root4 = Tk()
    root4.title("Αναζήτηση Βιβλίου")
    root4.geometry("600x500")
    root4.resizable(width=0, height=0)
    Canvas1 = Canvas(root4)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root4, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    lb1 = Label(labelFrame, text="Τίτλος: ", bg='white',
                fg='#d68227', font=('Courier', 10))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    def bind4():
        # Search in bookList for book
        count = 0
        for b in bookList:
            count = b.checkIfBookExists(bookInfo1) + count
        if count != 0:
            chooseLib()
        else:
            noAvail()
    SubmitBtn = Button(root4, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=bind4)
    SubmitBtn.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.08)

    root4.mainloop()


def returnBook():

    global g, root5, EntryInfo2
    root5 = Tk()
    root5.title("Επιστροφή Βιβλίου")
    root5.geometry("600x500")
    root5.resizable(width=0, height=0)

    Canvas1 = Canvas(root5)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root5, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    Label(labelFrame, text="%-5s%-15s%-20s%-0s" % ('ΙID', 'Βιβλιοθήκη', 'Τίτλος',
          'Χρόνος'), bg='white', font=('Courier', 10), fg='#d68227').place(relx=0.07, rely=0.0)
    Label(labelFrame, text="___________________________________________________________________________________",
          bg='white', fg='#d68227').place(relx=0.07, rely=0.05)
    y = 0.1
    SubmitBtn = Button(root5, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=chooseDate)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    label2 = Label(root5, text="IID: ", font=(
        'Courier', 10), fg='#d68227', bg='white')
    label2.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.08)

    EntryInfo2 = Entry(labelFrame)
    EntryInfo2.place(relx=0.8, rely=0.75, relwidth=0.3, relheight=0.08)

    for g in issuedList:
        Label(labelFrame, text="%-5s%-15s%-20s%-0s" %
              (g.IssuedId, g.IssuedOwner, g.IssuedBook, g.IssuedTime), bg='white', fg='#d68227', font=('Courier', 10)).place(relx=0.07, rely=y)
        y += 0.05

    root5.mainloop()


def recommendBook():

    global g
    root = Tk()
    root.title("Δανεισμένα Βιβλία")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    Label(labelFrame, text="%-5s%-15s%-20s%-0s" % ('ΙID', 'Βιβλιοθήκη', 'Τίτλος',
          'Χρόνος'), bg='white', font=('Courier', 10), fg='#d68227').place(relx=0.07, rely=0.0)
    Label(labelFrame, text="___________________________________________________________________________________",
          bg='white', fg='#d68227').place(relx=0.07, rely=0.05)
    y = 0.1

    SubmitBtn = Button(root, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=searchForRecommendation)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    chosen_id3 = IntVar()

    label2 = Label(root, text="IID: ", font=(
        'Courier', 10), fg='#d68227', bg='white')
    label2.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.08)

    EntryInfo1 = Entry(labelFrame, textvariable=chosen_id3)
    EntryInfo1.place(relx=0.8, rely=0.75, relwidth=0.3, relheight=0.08)

    for g in bookHistory:
        Label(labelFrame, text="%-5s%-15s%-20s%-0s" %
              (g.IssuedId, g.IssuedOwner, g.IssuedBook, g.IssuedTime), bg='white', fg='#d68227', font=('Courier', 10)).place(relx=0.07, rely=y)
        y += 0.05

    root.mainloop()


def searchForRecommendation():

    root = Tk()
    root.title("Αναζήτηση Βιβλίου")
    root.geometry("600x500")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.75)

    label = Label(labelFrame, text="\n Αναζητήστε ένα βιβλίο για να λάβετε προτάσεις!",
                  bg='white', fg='#d68227', font='Courier')
    label.place(relx=0.05, rely=0.1)

    lb1 = Label(labelFrame, text="Τίτλος: ", bg='white',
                fg='#d68227', font=('Courier', 10))
    lb1.place(relx=0.05, rely=0.3, relheight=0.08)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.25, rely=0.3, relwidth=0.62, relheight=0.08)
    BtnOk = Button(root, text="Αναζήτηση", bg='#d68227',
                   font=('Courier', 10), fg='white', command=similarBooks)
    BtnOk.place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.08)


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

    Label(labelFrame, text="%-5s%-15s%-20s%-0s" % ('BID', 'Τίτλος', 'Συγγραφέας',
          'Κατηγορία'), bg='white', font=('Courier', 10), fg='#d68227').place(relx=0.07, rely=0.0)
    Label(labelFrame, text="___________________________________________________________________________________",
          bg='white', fg='#d68227').place(relx=0.07, rely=0.05)
    y = 0.1
    SubmitBtn = Button(root, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=chooseLib)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    label2 = Label(root, text="BID: ", font=(
        'Courier', 10), fg='#d68227', bg='white')
    label2.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.08)

    EntryInfo3 = Entry(labelFrame)
    EntryInfo3.place(relx=0.8, rely=0.75, relwidth=0.3, relheight=0.08)

    for b in bookList:
        Label(labelFrame, text="%-5s%-15s%-20s%-0s" % (b.bookBid, b.bookTitle, b.bookAuthor,
                                                       b.bookCategory), bg='white', fg='#d68227', font=('Courier', 10)).place(relx=0.07, rely=y)
        y += 0.05

    root.mainloop()


def chooseLib():

    global clicked, root6, EntryInfo1
    root6 = Tk()
    root6.title("Επιλογή Βιβλιοθήκης")
    root6.geometry("600x500")
    root6.resizable(width=0, height=0)

    Canvas1 = Canvas(root6)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)
    labelFrame = Frame(root6, bg='white')
    labelFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.75)

    Label(labelFrame, text="%-5s%-15s%-20s%-0s" % ('IΙD', 'Διαθέσιμα',
                                                   'Τίτλος', 'Βιβλιοθήκη'), bg='white', font=('Courier', 10), fg='#d68227').place(relx=0.07, rely=0.0)
    Label(labelFrame, text="______________________________________________________________________________________",
          bg='white', fg='#d68227').place(relx=0.07, rely=0.05)
    y = 0.1

    # Change the label text
    def getTime():
        label1.config(text=clicked.get())

    options = [
        "1 εβδομάδα",
        "2 εβδομάδες",
        "3 εβδομάδες",
        "1 μήνας"
    ]
    clicked = StringVar()
    clicked.set("1 εβδομάδα")

    drop = OptionMenu(root6, clicked, *options)
    drop.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.08)

    Btn = Button(root6, text="Αλλαγή Χρόνου", bg='#d68227',
                 font=('Courier', 10), fg='white', command=getTime)
    Btn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    label1 = Label(root6, text="1 εβδομάδα", font='Courier',
                   bg='white', fg='#d68227',)
    label1.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.08)

    def bind3():
        i.issueBook(u, inventoryList, issuedList, bookInfo1,
                    EntryInfo1, bookHistory, clicked, noCredits)
        root6.wm_state('withdrawn')
        root4.wm_state('withdrawn')

    SubmitBtn = Button(root6, text="Υποβολή", bg='#d68227',
                       font=('Courier', 10), fg='white', command=bind3)
    SubmitBtn.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.08)

    label2 = Label(root6, text="IID: ", font=(
        'Courier', 10), fg='#d68227', bg='white')
    label2.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.08)

    EntryInfo1 = Entry(labelFrame)
    EntryInfo1.place(relx=0.8, rely=0.75, relwidth=0.2, relheight=0.08)

    for i in inventoryList:
        if (i.InventoryBook == bookInfo1.get()) & (i.InventoryAvail == 1):
            Label(labelFrame, text="%-5s%-15s%-20s%-0s" %
                  (i.InventoryId, i.InventoryAvail, i.InventoryBook, i.InventoryOwner), bg='white', fg='#d68227', font=('Courier', 10)).place(relx=0.07, rely=y)
            y += 0.05

    root6.mainloop()


def noAvail():

    global root7
    root7 = Tk()
    root7.title("Πρόβλημα")
    root7.geometry("440x100")
    root7.resizable(width=0, height=0)

    Canvas1 = Canvas(root7)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label(root7, text="Το βιβλίο δεν είναι διαθέσιμο :-(\nΘέλετε να το προσθέσετε στη wishlist;",
                  bg='white', fg='#d68227', font=('Courier', 10))
    label.place(relx=0.15, rely=0.1)

    def bind2():
        root4.wm_state('withdrawn')
        root7.wm_state('withdrawn')
        u.addToWishlist(bookInfo1.get())

    BtnYes = Button(root7, text="Ναι", bg='#d68227',
                    font=('Courier', 10), fg='white', command=bind2)
    BtnYes.place(relx=0.2, rely=0.55, relwidth=0.2)

    BtnNo = Button(root7, text="Όχι", bg='#d68227',
                   font=('Courier', 10), fg='white', command=root7.destroy)
    BtnNo.place(relx=0.6, rely=0.55, relwidth=0.2)
    root7.mainloop


def noCredits():

    root = Tk()
    root.title("Πρόβλημα")
    root.geometry("440x100")
    root.resizable(width=0, height=0)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    label = Label(root, text="Έχετε μόνο "+str(u.userCredits)+" credits :-(\nΘέλετε να προσθέσετε;",
                  bg='white', fg='#d68227', font=('Courier', 10))
    label.place(relx=0.25, rely=0.1)

    BtnYes = Button(root, text="Ναι", bg='#d68227',
                    font=('Courier', 10), fg='white', command='')
    BtnYes.place(relx=0.2, rely=0.55, relwidth=0.2)

    BtnNo = Button(root, text="Όχι", bg='#d68227',
                   font=('Courier', 10), fg='white', command=root.destroy)
    BtnNo.place(relx=0.6, rely=0.55, relwidth=0.2)

    root.mainloop()


def chooseDate():

    global p, root9
    root9 = Tk()
    root9.title("Επιλογή Ημερομηνίας")
    root9.resizable(width=0, height=0)
    root9.geometry("320x260")
    cal = Calendar(root9, selectmode='day',
                   year=1996, month=4,
                   day=13)
    cal.pack(pady=5)
    p = cal.get_date()

    def bind1():
        # Checks if user has given correct id input
        temp = 0
        for g in issuedList:
            temp = g.checkIfIssuedExists(EntryInfo2) + temp
        if temp != 0: 
            g.withdrawBook(EntryInfo2, issuedList, p)
            # Make book available in inventory
            t = Inventory(g.IssuedOwner, g.IssuedBook, 1)
            t.addIssuedToInventory(inventoryList)
            u.calculateFine(g, p, 500)
            root5.wm_state('withdrawn')
            root9.wm_state('withdrawn')
            u.notifyLibrary()
            u.notifyUsers()
        else:
            messagebox.showerror(message="Δεν υπάρχει τέτοιο βιβλίο στη λίστα!", title='Σφάλμα')
            root9.wm_state('withdrawn')

    Button(root9, text="Υποβολή", bg='#d68227',
           font=('Courier', 10), fg='white', command=bind1).pack(pady=5)

    root9.mainloop()

def addCreditsScreen():
    screenCred1 = Toplevel(screenCred)
    screenCred1.title("Προσθήκη credits")
    screenCred1.geometry("500x150")
    screenCred1.resizable(width=0, height=0)

    Label(screenCred1,
            text ="Πόσα credits θέλετε να προσθέσετε?", fg='#d68227', width="300",
            height="2", font=("Courier", 16)).pack(pady=5)
    amount = int()
    amount_entry = Entry(screenCred1, textvariable=amount)
    amount_entry.pack()
    def bind99():
        # Add chosen amount to user
        u.addCredits(int(amount_entry.get()))
        # Show message
        messagebox.showinfo(message="Προσθέσατε "+str(amount_entry.get())+" credits στο λογαριασμό σας!", title='Μήνυμα')
        print(u.getName()+" credits: "+str(u.userCredits))
        screenCred1.wm_state("withdrawn")
        screenCred.wm_state("withdrawn")
    button = Button(screenCred1, text="Υποβολή", height="2", width="10", bg='white',
            fg='#d68227', font=('Courier', 10), command = bind99)
    button.pack(pady=5)
    
def giftCreditsScreen():
    screenCred2 = Toplevel(screenCred)
    screenCred2.title("Μεταφορά credits")
    screenCred2.geometry("500x150")
    screenCred2.resizable(width=0, height=0)

    Label(screenCred2,
            text ="Πόσα credits θέλετε να μεταφέρετε?", fg='#d68227', width="300",
            height="2", font=("Courier", 16)).pack(pady=5)

    amount1_entry = Entry(screenCred2)
    amount1_entry.pack()
    
    def bind88():
        # Transfer chosen amount to r1 user
        u.transferCredits(r1, int(amount1_entry.get()))
        # Show message 
        messagebox.showinfo(message="Μεταφέρατε "+str(amount1_entry.get())+" credits στον χρήστη "+r1.getName()+"!", title='Μήνυμα')
        print(u.getName()+" credits: "+str(u.userCredits))
        print(r1.getName()+" credits: "+str(r1.userCredits))
        screenCred2.wm_state("withdrawn")
        screenCred.wm_state("withdrawn")
    Button(screenCred2, text="Υποβολή", height="2", width="10", bg='white',
            fg='#d68227', font=('Courier', 10), command=bind88).pack(pady=5)
    

def creditsSystem():
    global screenCred
    screenCred = Tk()
    screenCred.geometry("600x500")
    screenCred.title("Διαχείριση Credits")
    screenCred.resizable(width=0, height=0)
    Label(screenCred, text="Διαχείριση Credits ⭐", fg='#d68227', width="300",
          height="2", font=("Courier", 24, 'bold')).pack()
    Label(screenCred, text="Έχετε "+str(u.userCredits)+" credits", fg='#d68227', width="300",
          height="2", font=("Courier", 16)).pack(pady = 5)

    Button(screenCred, text="Προσθήκη credits", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command=addCreditsScreen).pack(pady=5)

    Button(screenCred, text="Μεταφορά credits", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command=giftCreditsScreen).pack()

main_screen()