 # -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:21:10 2021

@author: Saja
"""


import tkinter
from secondPage import next_page
from slideshow import slideShow
from menuBar import mainMenue



def exitFirstWindow():
    root.destroy()

def secondPage():
     next_page(nameEntry.get(),ageEntry.get(),radio_var.get())
    
#create tkinter window
root =tkinter.Tk()
#size of the window
root.geometry("500x700")
#root.geometry("250x200")
root.title("Diabetic Predictor")

title = tkinter.Label(root, text="Diabetic Predictor", width=20, font=("arial", 25,"bold"),fg="red", relief="solid")   
title.pack()

name = tkinter.Label(root, text="Enter Your Name", width=20, font=("arial", 15,"bold") )   
name.place( x =10, y = 340)
nameEntry= tkinter.Entry(root)
nameEntry.place( x =250, y = 340,height=20)

age = tkinter.Label(root, text="Enter Your Age", width=20, font=("arial",15,"bold") )   
age.place(x=1,y=400)
ageEntry= tkinter.Entry(root)
ageEntry.place( x =250, y = 400,height=20)

radio_var=tkinter.StringVar(root) 
gender = tkinter.Label(root, text="Select Gender", width=20, font=("arial",15,"bold") )   
gender.place(x=-2,y=460)
maleChBox = tkinter.Radiobutton(root, text="Male",value="male", variable=radio_var)
maleChBox.place(x=250,y=460)
femaleChBox = tkinter.Radiobutton(root, text="Female", value="female", variable=radio_var)
femaleChBox.place(x=320,y=460)


btn1=tkinter.Button(root, text="Next",width=12, bg="red", fg="white",command=secondPage)
btn1.place(x=90,y=560)

btn2=tkinter.Button(root, text="Quit",width=12, bg="black", fg="white",command=exitFirstWindow)
btn2.place(x=300,y=560)



 
slideShow(root)
mainMenue(root)
root.mainloop() 


