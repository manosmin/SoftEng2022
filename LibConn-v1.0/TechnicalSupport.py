from tkinter import *
import itertools

class TechnicalSupport:
    id_iter = itertools.count()

    def __init__(self, techRating, techSolution, techProblem):
        self.bookBid = next(TechnicalSupport.id_iter)
        self.techRating = techRating
        self.techSolution = techSolution
        self.techProblem = techProblem

    def setTechSuppRating(self, a):
        self.techRating = a 
    def getTechSuppRating(self):
        return self.techRating
    def getRole(self):
        return
    def showSolution(self):
        return self.techSolution


def destroy():
    screenTech1.wm_state('withdrawn')
    screenTech2.wm_state('withdrawn')
    screenTech3.wm_state('withdrawn')
    screenTech4.wm_state('withdrawn')
    screenTech5.wm_state('withdrawn')

def getRole():
    global screenTech1
    screenTech1 = Toplevel(screenTech)
    screenTech1.title("Επιλογή Ρόλου")
    screenTech1.geometry("600x500")
    Label(screenTech, text="Επιλέξτε τον ρόλο σας:", fg='#d68227', width="300",
          height="2", font=("Courier", 20, 'bold')).pack()
    Button(screenTech, text="Αναγνώστης", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12)).pack()
    Button(screenTech, text="Βιβλιοθήκη", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12)).pack()
    
def problem():
    global screenTech2
    screenTech2 = Tk()
    screenTech2.title("Επιλογή Προβλήματος")
    screenTech2.geometry("600x500")
    Label(screenTech2, text="Επιλέξτε το πρόβλημα σας:", fg='#d68227', width="300",
          height="2", font=("Courier", 20, 'bold')).pack()
    Button(screenTech2, text="Πρόβλημα 1", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = showSolution).pack()
    Button(screenTech2, text="Πρόβλημα 2", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = showSolution).pack()
    Button(screenTech2, text="Πρόβλημα 3", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = showSolution).pack()
    Button(screenTech2, text="Πρόβλημα 4", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = showSolution).pack()

def showSolution():
    global screenTech3
    screenTech3 = Tk()
    screenTech3.title("Λύσεις")
    screenTech3.geometry("600x500")
    Label(screenTech3, text="Επιλέξτε μια ενδεικτική λύση:", fg='#d68227', width="300",
          height="2", font=("Courier", 20, 'bold')).pack()
    Button(screenTech3, text="Λύση 1", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = sendMessage).pack()
    Button(screenTech3, text="Λύση 2", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = sendMessage).pack()
    Button(screenTech3, text="Λύση 3", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = sendMessage).pack()
    Button(screenTech3, text="Λύση 4", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = sendMessage).pack()
    
def sendMessage():
    global screenTech4
    screenTech4 = Tk()
    screenTech4.title("Αποστολή Μηνύματος")
    screenTech4.geometry("600x500")
    E1 = Entry(screenTech4, bd =5, width = 40)
    E1.pack()
    Label(screenTech4, text="Στείλτε ένα μήνυμα αναλύοντας το πρόβλημα σας:", fg='#d68227', width="300",
          height="2", font=("Courier", 10, 'bold')).pack()
    Button(screenTech4, text="Υποβολή", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = techSuppRating).pack()
    
def techSuppRating():
    global screenTech5
    screenTech5 = Tk()
    screenTech5.title("Βαθμολογία")
    screenTech5.geometry("600x500")
    Label(screenTech5, text="Βαθμολογήστε την υπηρεσία μας! (1-10)", fg='#d68227', width="300",
          height="2", font=("Courier", 10, 'bold')).pack()
    E2 = Entry(screenTech5, bd =5, width = 40)
    E2.pack()
    Button(screenTech5, text="Υποβολή", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = destroy).pack()

def techSupport():
    global screenTech
    screenTech = Tk()
    screenTech.geometry("600x500")
    screenTech.title("Τεχνική Υποστήριξη")
    screenTech.resizable(width=0, height=0)
    Label(screenTech, text="Επιλέξτε τον ρόλο σας:", fg='#d68227', width="300",
          height="2", font=("Courier", 20, 'bold')).pack()
    Button(screenTech, text="Αναγνώστης", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = problem).pack()
    Button(screenTech, text="Βιβλιοθήκη", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command = problem).pack()
    