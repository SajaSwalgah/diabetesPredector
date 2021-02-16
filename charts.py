# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:47:03 2021

@author: Saja
"""

import tkinter
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
# Implement the default Matplotlib key bindings.

def statisticss(var) :

    root = tkinter.Tk()
    root.wm_title("Diapetes Chart")



    dataSet = pd.read_csv('diabetes.csv')
    #print(dataSet.head())

    featuresColumns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    x=dataSet[featuresColumns]
    y= dataSet['Outcome']



    def convert():
        outcomeData =[]
        for x in range(len(y)):
            if y[x] == 0 :
                outcomeData.append('Not')
            else :
                outcomeData.append('Diabetic')
        
        ser = pd.Series(outcomeData) 
        return ser


    data = {'diabetes':convert(), var:x[var]}
    df=pd.DataFrame(data,columns=['diabetes',var])

    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    df1 = df[['diabetes',var]].groupby('diabetes').mean()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Diabetes Vs. mean of ' + var)
    


    tkinter.mainloop()

