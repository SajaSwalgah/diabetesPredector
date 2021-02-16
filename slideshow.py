# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:26:57 2021

@author: Saja
"""


import tkinter
from PIL import Image, ImageTk


x=1
def slideShow(windowName):
    load1=Image.open("diabetes.jpg").resize((500, 250), Image.ANTIALIAS)
    load2=Image.open("diabetess.jpg").resize((500, 250), Image.ANTIALIAS)
    load3=Image.open("facts.png").resize((500, 250), Image.ANTIALIAS)
    load4=Image.open("advices.jpg").resize((500, 250), Image.ANTIALIAS)

    image1=ImageTk.PhotoImage(load1)
    image2=ImageTk.PhotoImage(load2)
    image3=ImageTk.PhotoImage(load3)
    image4=ImageTk.PhotoImage(load4)

    slideShow=tkinter.Label(windowName,font="bold")
    slideShow.pack()
   
    def move():
        global x
        if x==5:
            x=1
        if x==1:
            slideShow.config(image=image1)
        elif x==2:
            slideShow.config(image=image2)
        elif x==3:
            slideShow.config(image=image3)
        elif x==4:
            slideShow.config(image=image4)
        
        x+=1
        windowName.after(3000,move) 
    
    move()