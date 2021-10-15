# este escrip cria uma API para colocar um modelo em produção utilizando o framework flask

# importando as bibliotecas
import numpy as np
import os
from flask import Flask, request, render_template, make_response
from sklearn.externals import joblib


app = Flask(__name__, static_url_path='/static')
model = joblib.load(open('modelo.pkl', 'rb'))

@app.route('/')
def display_gui():
    return render_template('template.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    Pregnancies = request.form['Pregnancies']
    Glucose = request.form['Glucose']
    BloodPressure = request.form['BloodPressure']
    SkinThickness = request.form['SkinThickness']
    Insulin = request.form['Insulin']
    BMI = request.form['BMI']
    DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction']
    Age = request.form['Age']

    teste = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    print(":::::: Dados Teste ::::::")
    print("Pregnancies: {}".format(Pregnancies))
    print("Glucose: {}".format(Glucose))
    print("BloodPressure: {}".format(BloodPressure))
    print("SkinThickness: {}".format(SkinThickness))
    print("Insulin: {}".format(Insulin))
    print("BMI: {}".format(BMI))
    print("DiabetesPedigreeFunction: {}".format(DiabetesPedigreeFunction))
    print("Age: {}".format(Age))

    classe = model.predict(teste)[0]
    print("Classe Predita: {}".format(str(classe)))
    
    return render_template('template.html', classe=str(classe))
if __name__ =="__main__":
    port = int(os.environ.get('PORT, 5500'))
    app.run(hust='0.0.0.0', port=port)




