# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:19:16 2021

@author: Saja
"""

import tkinter
from diabetes import getRersults
from menuBar import mainMenue


def next_page(name, age, gender):       
        
    def exitSecondWindow():        
        window.destroy()
     
    window =tkinter.Tk()  
    mainMenue(window)
    preg_var =tkinter.StringVar(window)
    #size of the window
    window.geometry("500x700")
    #root.geometry("250x200")
    window.title("diabetic next")
    
    title = tkinter.Label(window, text="Diabetic Predictor", width=20, font=("arial", 25,"bold"),fg="red", relief="solid")   
    title.pack()
    
    if(gender == 'female') :
        pregnancies = tkinter.Label(window,text="Pregnancies Num", width=20,font=("arial",15,"bold") )   
        pregnancies.place(x=15,y=70)
     
        nums=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
        preg_var.set("Num of Preg")
        droplist=tkinter.OptionMenu(window,preg_var,*nums)
        droplist.place(x=250,y=70)
    
    GC = tkinter.Label(window, text="Glucose Const", width=20, font=("arial", 15,"bold") )   
    GC.place( x =1, y = 120)
    GCEntry= tkinter.Entry(window)
    GCEntry.insert(0,'from 0-200')    
    GCEntry.place( x =250, y = 125,height=20)
    
    BP = tkinter.Label(window, text="Blood Pressure", width=20, font=("arial", 15,"bold") )   
    BP.place( x =2, y = 160)
    BPEntry= tkinter.Entry(window)
    BPEntry.insert(0,'from 0-122')
    BPEntry.place( x =250, y = 165,height=20)
    
    STh = tkinter.Label(window, text="Skin Thickness", width=20, font=("arial", 15,"bold") )   
    STh.place( x =1, y = 200)
    SThEntry= tkinter.Entry(window)
    SThEntry.insert(0,'from 0-100')
    SThEntry.place( x =250, y = 205,height=20)

    insulin = tkinter.Label(window, text="Insulin", width=20, font=("arial", 15,"bold") )   
    insulin.place( x =-40, y = 240)
    insulinEntry= tkinter.Entry(window)
    insulinEntry.insert(0,'from 0-845')
    insulinEntry.place( x =250, y = 245,height=20)

    BMI = tkinter.Label(window, text="Body Mass Index", width=20, font=("arial", 15,"bold") )   
    BMI.place( x =10, y = 280)
    BMIEntry= tkinter.Entry(window)
    BMIEntry.insert(0,'from 0-67')
    BMIEntry.place( x =250, y = 285,height=20)

    DPF = tkinter.Label(window, text="Diabetes Pedigree ", width=20, font=("arial", 15,"bold") )   
    DPF.place( x =16, y = 320)
    DPFEntry= tkinter.Entry(window)
    DPFEntry.insert(0,'from 0.05-2.5')
    DPFEntry.place( x =250, y = 325,height=20)
    
    def getInfo():
         info =[]
         if(gender == 'female') :
             info.append(preg_var.get())
         else :
             info.append(0)
         info.append(GCEntry.get())
         info.append(BPEntry.get())
         info.append(SThEntry.get())
         info.append(insulinEntry.get())
         info.append(BMIEntry.get())
         info.append(DPFEntry.get())
         info.append(age) 
         return info
        
  
    def finalResult ():        
        getRersults(getInfo(),name,age)        
    
    btn3=tkinter.Button(window, text="Get Results",width=12, bg="red", fg="white",command=finalResult)
    btn3.place(x=90,y=560)

    btn4=tkinter.Button(window, text="Quit",width=12, bg="black", fg="white", command=exitSecondWindow )
    btn4.place(x=300,y=560)
  

