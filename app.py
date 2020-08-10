# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 02:38:54 2020

@author: Avinash Sahu
"""
from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
#import numpy as np
#import sklearn
#from sklearn.preprocessing import MinMaxScaler
#scaler = MinMaxScaler()
app = Flask(__name__)
model = pickle.load(open('titanic_rf_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Pclass = int(request.form['Pclass'])
        Age=int(request.form['age'])
        SibSp=int(request.form['sibSp'])
        Parch=int(request.form['Parch'])    
        Fare=int(request.form['Fare'])
        Sex=request.form['Sex']
        if(Sex=='M'):
                Sex_male=1
        elif(Sex=='F'):
                Sex_male=0 
        Embarked=request.form['Embarked']
        if(Embarked=='Q'):
            Embarked_Q=1
            Embarked_S=0
        elif(Embarked=='S'):
            Embarked_Q=0
            Embarked_S=1
        else:
            Embarked_Q=0
            Embarked_S=0
        #cols = [Pclass,Age,SibSp,Parch,Fare,Sex_male,Embarked_Q,Embarked_S]  
        prediction=model.predict([[Pclass,Age,SibSp,Parch,Fare,Sex_male,Embarked_Q,Embarked_S]])
        #output=round(prediction[0],2)
        if prediction==1:
            return render_template('index.html',prediction_texts="Sorry you won't survive")
        else:
            return render_template('index.html',prediction_text="You will survive")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

