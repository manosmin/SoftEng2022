from tkinter import *
import os

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x500")
    screen.title("Credits")
    screen.resizable(width=0, height=0)
    Label(text="Credits⭐", fg='#d68227', width="300",
          height="2", font=("Courier", 28, 'bold')).pack()
    Label(text="You have 100 credits", fg='#d68227', width="300",
          height="2", font=("Courier", 28, 'bold')).pack()
    Button(text="Add Credits", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command=add).pack()
    Button(text="Gift Credits", height="2", width="30", bg='white',
          fg='#d68227', font=('Courier', 12), command=gift).pack()

    screen.mainloop()
    
def add():
    screen1 = Toplevel(screen)
    screen1.title("Add Credits")
    screen1.geometry("600x500")
    Label(screen1,
          text ="How many credits do you want to add?", fg='#d68227', width="300",
          height="2", font=("Courier", 14, 'bold')).pack()
    amount = int()
    amount_entry = Entry(screen1, textvariable=amount)
    amount_entry.pack()
    #label1 = Label(screen1, text="Are you sure you want to add this amount?", fg='#d68227', width="300",
             #height="2", font=("Courier", 12, 'bold')).pack()
    button = Button(screen1, text="Submit", height="2", width="10", bg='white',
          fg='#d68227', font=('Courier', 10), command = label1).pack()
    
#def label1():
    #Label(screen1, text = "Are you sure you want to add this amount?", fg='#d68227', width="300",
          #height="2", font=("Courier", 12, 'bold')).pack()

def gift():
    screen2 = Toplevel(screen)
    screen2.title("Gift Credits")
    screen2.geometry("600x500")
    Label(screen2,
          text ="How many credits do you want to gift?", fg='#d68227', width="300",
          height="2", font=("Courier", 14, 'bold')).pack()
    amount1 = int()
    amount1_entry = Entry(screen2, textvariable=amount1)
    amount1_entry.pack()
    Button(screen2, text="Submit", height="2", width="10", bg='white',
          fg='#d68227', font=('Courier', 10)).pack()
          
main_screen()          
