import itertools
from tkinter import messagebox
from Issued import *


class Inventory:
    id_iter = itertools.count()

    def __init__(self, InventoryOwner, InventoryBook, InventoryAvail):
        self.InventoryId = next(Inventory.id_iter)
        self.InventoryOwner = InventoryOwner
        self.InventoryBook = InventoryBook
        self.InventoryAvail = InventoryAvail

    def setAvail(self, a):
        self.InventoryAvail = a 
    
    def issueBook(self, user, invList, issList, book, userChoice, bookHi, timeChoice, call1):
        if user.userCredits > 100:
            for self in invList:
                if self.InventoryBook == book.get():
                    if self.InventoryId == int(userChoice.get()):
                        if self.InventoryAvail == 1:
                            # Remove book from available
                            self.setAvail(0)
                            print(self.InventoryId, self.InventoryAvail,
                                self.InventoryBook, self.InventoryOwner)
                            # Remove 100 credits from user
                            user.removeCredits(100)
                            print(user.userCredits)
                            # Create issued object
                            e = Issued(user.userName, self.InventoryOwner,
                                    self.InventoryBook, timeChoice.get())
                            # Add to issued
                            issList.append(e)
                            # Add to book history 
                            bookHi.append(e)
                            # Print issuedList length after issuing
                            print(len(issList))
                            print(e.IssuedName, e.IssuedOwner,
                                e.IssuedBook, e.IssuedTime)
                            messagebox.showinfo(
                                title='Μήνυμα', message='Ο δανεισμός του βιβλίου '+e.IssuedBook+' από τη βιβλιοθήκη '+e.IssuedOwner+' έγινε με επιτυχία!')
        else:
            call1()
        return e
    
    def addIssuedToInventory(self, invList):
            invList.append(self)