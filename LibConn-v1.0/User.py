import itertools


class User:
    id_iter = itertools.count()

    def __init__(self, userName, userRole):
        self.userUid = next(User.id_iter)
        self.userName = userName
        self.userRole = userRole

    def setName(self, a):
        self.userName = a
    def setRole(self, a):
        self.userRole = a
    def getName(self):
        return self.userName
    def getRole(self):
        return self.userRole

    def addUserToList(self, l):
        l.append(self)

    def notifyUsers(self):
        print('Send notification to users')
        # Notify users which have book in wishlist - Step 8
        return

    def notifyLibrary(self):
        print('Send notificaton to library')
        # Notify library for book return - Step 5
        return
