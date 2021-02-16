# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:48:02 2021

@author: Saja
"""

import tkinter
from charts import statisticss

def Pregnancies():
    statisticss('Pregnancies')
    
def Glucose():
    statisticss('Glucose')
    
def BloodPressure():
    statisticss('BloodPressure')
    
def BMI():
    statisticss('BMI')

def statisticsPage():    
    #create tkinter window
    root =tkinter.Tk()
    #size of the window
    root.geometry("400x400")
    #root.geometry("250x200")
    root.title("Diabetic Predictor")
    
    title = tkinter.Label(root, text="Diabetic Predictor", width=20, font=("arial", 25,"bold"),fg="red", relief="solid")   
    title.pack()
    
    
    btn1=tkinter.Button(root, text="Diabetes Vs.\n Pregnancies",width=20, bg="green", fg="white", command=Pregnancies)
    btn1.place(x=30,y=100)

    btn2=tkinter.Button(root, text="Diabetes Vs.\n Glucose",width=20, bg="blue", fg="white", command=Glucose)
    btn2.place(x=200,y=100)
    
    btn2=tkinter.Button(root, text="Diabetes Vs.\n BloodPressure",width=20, bg="purple4", fg="white", command=BloodPressure)
    btn2.place(x=30,y=200)
    
    btn2=tkinter.Button(root, text="Diabetes Vs.\n BMI",width=20, bg="orange", fg="white", command =BMI)
    btn2.place(x=200,y=200)


