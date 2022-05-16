from tkinter import *
from tkcalendar import Calendar

def returnBook():

    global SubmitBtn, Canvas1, root, labelFrame

    root = Tk()
    root.title("LibConn")
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
                       font=('Courier', 10), fg='white', command=chooseDate)
    SubmitBtn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.08)

    root.mainloop()


def chooseDate():

    root = Tk()
    root.title("Επιλογή Ημερομηνίας")
    root.resizable(width=0, height=0)
    # Set geometry
    root.geometry("320x260")
    
    # Add Calendar
    cal = Calendar(root, selectmode = 'day',
                year = 1996, month = 4,
                day = 13)
    
    cal.pack(pady = 5)
    
    def grad_date():
        date.config(text = "Επιστροφή βιβλίου: " + cal.get_date())
    
    # Add Button and Label
    Button(root, text = "Υποβολή",
        command = grad_date).pack(pady = 5)
    
    date = Label(root, text = "")
    date.pack(pady = 5)
    
    # Execute Tkinter
    root.mainloop()

