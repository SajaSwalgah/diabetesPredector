# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:20:53 2021

@author: Saja
"""
import tkinter

def generalInfo():
    
    def exitWindow():
        r.destroy()
    
    
    r =tkinter.Tk()
    #size of the window
    r.geometry("1000x700" )
    #root.geometry("250x200")
    r.title("Diabetic Predictor - Information")

    title = tkinter.Label(r, text="Diabetic Predictor", width=20, font=("arial", 25,"bold"),fg="red", relief="solid")   
    title.pack()
    
    #label1 = tkinter.Label(r, text="Diabetes: ", width=20, font=("arial", 15,"bold") )   
    #label1.place(x=-28,y=70)
    
    label1 = tkinter.Label(r, text="Diabetes: is a disease in which your blood glucose, or blood sugar, levels are too high.", width=100, font=("arial", 15,"bold") ,fg="gray25")   
    label1.place(x=-125,y=70)
    
    label2 = tkinter.Label(r, text="Type 1 Diabetes, your body does not make insulin.", width=100, font=("arial", 15,"bold") ,fg="gray26")   
    label2.place(x=-300,y=110)

    label3 = tkinter.Label(r, text="Type 2 Diabetes, the more common type, your body does not make or use insulin well.", width=100, font=("arial", 15,"bold"),fg="gray27" )   
    label3.place(x=-126,y=150)
    
    label4 = tkinter.Label(r, text="Diagnosis of diabetes depends on plasma glucose, which is measurable during fasting,", width=100, font=("arial", 15,"bold") ,fg="gray28")   
    label4.place(x=-125,y=190)
    
    label5 = tkinter.Label(r, text="The normal level should be under 100mg/dL using oral glucose tolerance test.", width=100, font=("arial", 15,"bold"), fg="gray29" )   
    label5.place(x=-172,y=230)
    
    label6 = tkinter.Label(r, text="Blood pressure is the pressure your heart uses to push blood through your body.", width=100, font=("arial", 15,"bold") ,fg="gray30")   
    label6.place(x=-152,y=270)
    
    label7 = tkinter.Label(r, text="Skin thickness is the collagen content and is increased in insulin-dependent diabetes mellitus.", width=100, font=("arial", 15,"bold"),fg="gray31" )   
    label7.place(x=-100,y=310)
    
    label8 = tkinter.Label(r, text="Insulin is a hormone made in your pancreas. It helps your body use glucose (sugar) for energy.", width=100, font=("arial", 15,"bold") ,fg="gray32")   
    label8.place(x=-92,y=350)
    
    label9 = tkinter.Label(r, text="Body Mass Index is a simple calculation using a person’s height and weight. BMI = kg/m2.", width=100, font=("arial", 15,"bold") ,fg="gray33")   
    label9.place(x=-120,y=390)
    
    label10 = tkinter.Label(r, text="Diabetes pedigree function: a function which scores likelihood of diabetes based on family history.", width=100, font=("arial", 15,"bold"),fg="gray34" )   
    label10.place(x=-75,y=430)
    
    btn2=tkinter.Button(r, text="Quit",width=12, bg="black", fg="white",command=exitWindow)
    btn2.place(x=500,y=500)





  


    
