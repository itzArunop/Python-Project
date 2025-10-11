import tkinter as tk
from time import strftime

#Create the main window
root = tk.Tk()
root.title("Digital Clock")

#Function to update time
def time():
    string = strftime('%I:%M:%S %p \n %D') #Format: Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000,time) #Update every 1 second

#Styling the clock
label = tk.Label(root,font=('Algerian',50,'bold'),background='yellow',foreground='black')
label.pack(anchor='center')

time() #Run the clock


root.mainloop()
