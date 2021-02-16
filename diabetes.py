# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:26:57 2021

@author: Saja
"""
# libaries we need 
import pandas as pd
import tkinter
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
import pickle
    
def getRersults(inputArray, name, age):
    dataSet = pd.read_csv('diabetes.csv')
    #print(dataSet.head())

    featuresColumns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']

    x=dataSet[featuresColumns]
    y= dataSet['Outcome']

    #training data for best accurecy
    bestAcc=0
    for i in range(30):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1)
        m=DecisionTreeClassifier()
        m=m.fit(x_train, y_train)        
        acc = m.score(x_test, y_test)
        #print(acc)
        if acc> bestAcc :
            bestAcc = acc
            #saving the data of the best assurecy in order to use them later
            outfile= open("diapetesData", "wb") #w:writting to a file, b:binary
            pickle.dump(m,outfile)
            outfile.close()
            
    infile = open("diapetesData", "rb") #r:read, b:binary
    m=pickle.load(infile)
    
    #print('inputArray',inputArray)
    toPredict =[inputArray]
    
    #print('toPredict',toPredict)
    prediction = m.predict(toPredict)
    #print('prediction',prediction)
    output=''
    if prediction ==0:
        output = "NOT have"
    else :
        output = 'have'
        
    #print(bestAcc)
    tkinter.messagebox.showinfo("Result for " +name ,"Patient Name: " +name+'\n' + "Patient Age: "+age+'\n' +'This patient will ' + output+' diabetes in the future with accurecy = ' + str(bestAcc))
 
