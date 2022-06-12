from User import *
from tkinter import messagebox


class Reader(User):

    def __init__(self, userName, userCredits, userAge, userLocation, userFavCateg):
        self.userUid = next(User.id_iter)
        self.userName = userName
        self.userCredits = userCredits
        self.userRole = 'Reader'
        self.userAge = userAge
        self.userLocation = userLocation
        self.userFavCateg = userFavCateg
        self.userWish = []

    def setAge(self, a):
        self.userAge = a

    def setLocation(self, a):
        self.userLocation = a

    def setFavCateg(self, a):
        self.userFavCateg = a

    def getAge(self):
        return self.userAge

    def getLocation(self):
        return self.userLocation

    def getFavCateg(self):
        return self.userFavCateg

    def removeCredits(self, amount):
        self.userCredits = self.userCredits - amount

    def addCredits(self, amount):
        self.userCredits = self.userCredits + amount
        print(str(amount)+" credits added.")

    def transferCredits(self, user, amount):
        self.userCredits = self.userCredits - amount
        user.userCredits = user.userCredits + amount

    def addToWishlist(self, book):
        self.userWish.append(book)
        messagebox.showinfo(
        title='Μήνυμα', message='Το βιβλίο προστέθηκε στη wishlist!\n'+str(self.userWish))

    def calculateFine(self, issuedTo, returnTime, fine):
        # Remove credits from user ( •̀ᴗ•́ )و
        if issuedTo.IssuedTime == "1 μήνας":
            self.removeCredits(fine)
            print(self.userCredits)
            messagebox.showinfo(
                title='Μήνυμα', message='Αφαιρέθηκαν 500 credits από το λογαριασμό λόγω καθυστερημένης επιστροφής!')

    def registerReader(self, age, cre,  loc, cat):
        self.addCredits(cre)
        self.setAge(age)
        self.setLocation(loc)
        self.setFavCateg(cat)
        print('UID: '+str(self.userUid)+'\nΌνομα: '+self.getName()+'\nCredits: '+str(self.userCredits)+'\nΡόλος: '+ self.getRole()+'\nΗλικία: '+str(self.getAge())+'\nΤοποθεσία: '+self.getLocation()+'\nΑγαπημένη κατηγορία: '+self.getFavCateg())
    
