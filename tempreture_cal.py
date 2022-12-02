import tkinter as tk #import the module tkinter
from turtle import clear
from tkinter import *#import * to import files from your laptop


root= tk.Tk() #root 

root.title('tempreture converter')#window tilte
logo=PhotoImage(file=r'''C:\Users\User\Downloads\download (1)png.png''')# logo image file location
root.iconphoto(False,logo)

bg=PhotoImage(file=r'''C:\Users\User\Downloads\png-transparent-purple-gradient-watercolor-background-purple-gradual-change-blue-thumbnail (3).png''')#backgorund

canvas1 = tk.Canvas(root, width = 400, height = 300,relief='raised') #canvas 
canvas1.pack()
canvas1.create_image(10,80,image=bg,anchor="center")#anchor and place the image

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1) # user entry window

def temp ():  #function to convert the temprture
    x1 = entry1.get()
    
    try:
     buttonx=tk.Button (root,text=int(x1)*1.8+32 ,bg='blue',font=('arial',10,'bold')) #calculation
     canvas1.create_window(200,230,window=buttonx)
    except ValueError:
     tk.messagebox.showerror('error ⚠️','invalid input please enter valid tempreture')#message box when user input is wrong
    return

    

    

button1 = tk.Button(text='convert tempreture to Fahrenheit 🌡️', command=temp,bg='purple',font=('arial,',10,'bold'))#button  to convert
canvas1.create_window(200, 180, window=button1)


buttonexit=tk.Button(text='exit',command=quit,bg='red',font=('arial',10,'bold'))#exit button
canvas1.create_window(350,275,window=buttonexit)
    
    
button3=tk.Label(text='enter temp in degrees celcius below',bg='blue',font=('arial',8)) #asking user input
canvas1.create_window(200,110,window=button3)



root.mainloop() #mainloop to run the canvas 

