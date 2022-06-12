import itertools
from tkinter import messagebox


class Issued:
    id_iter = itertools.count()

    def __init__(self, IssuedName, IssuedOwner, IssuedBook, IssuedTime):
        self.IssuedId = next(Issued.id_iter)
        self.IssuedName = IssuedName
        self.IssuedOwner = IssuedOwner
        self.IssuedBook = IssuedBook
        self.IssuedTime = IssuedTime

    def withdrawBook(self, userChoice, issList, returnTime):
        for self in issList:
            if self.IssuedId == int(userChoice.get()):
                # Remove book from issuedList
                issList.remove(self)
                print(len(issList))
                messagebox.showinfo(
                    title='Μήνυμα', message='Το βιβλίο πρέπει να επιστραφεί στη βιβλιοθήκη '+self.IssuedOwner+' στις ' + returnTime + '.')

    def checkIfIssuedExists(self, issuedChoice):
        # Search in issuedList for issued
        f = 0
        if issuedChoice.get() == str(self.IssuedId):
            f = 1
        return f
