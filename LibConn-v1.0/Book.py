import itertools

class Book:
    id_iter = itertools.count()
    totalRatings = 0
    def __init__(self, bookTitle, bookAuthor, bookCategory, bookRating, bookReview):
        self.bookBid = next(Book.id_iter)
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.bookCategory = bookCategory
        self.bookRating = bookRating
        self.bookReview = bookReview
    
    def setRating(self, a):
        Book.totalRatings = Book.totalRatings + 1
        self.bookRating = (a + self.bookRating) / Book.totalRatings

    def setReview(self, a):
        self.bookReview = a
    def setAuthor(self, a):
        self.bookAuthor = a
    def setCategories (self, a):
        self.bookCategory = a
    def getRating(self):
        return self.bookRating
    def getReview(self):
        return self.bookReview
    def getCategories(self):
        return self.bookCategory
    def getAuthor(self):
        return self.bookAuthor

    def checkIfBookExists(self, bookChoice):
        # Search in bookList for book
        f = 0
        if bookChoice.get() == self.bookTitle:
            f = 1
        return f
