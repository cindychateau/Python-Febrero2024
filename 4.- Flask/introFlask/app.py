#1.- pipenv install flask =o= py -m pipenv install flask =o= python -m pipenv install flask =o= python3 -m pipenv install flask
#2.- pipenv shell
#3.- python3 app.py

from flask import Flask, render_template #Importando Flask para crear mi aplicación
app = Flask(__name__)   #Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/') #Creamos una ruta que es: /
def home():
    return '¡Hola mundo, cómo estás!' #Va regresar la cadena ¡Hola mundo! como respuesta

@app.route('/hola/<nombre>') # /hola/_______ 
def hola(nombre):
    return '<h1>Hola '+nombre+'</h1>'

@app.route('/saluda/<int:num>') #SOLO ACEPTA numerales
def saluda(num):
    saludito = ''
    for x in range(num):
        saludito += ' Hola'
    return saludito

@app.route('/bienvenidos/<nombre>/<int:num>') #/bienvenidos/Elena/5
def bienvenidos(nombre, num):
    return render_template('index.html', nombre=nombre, numero=num)


if __name__ == "__main__": #Asegura que el archivo se ejecute directamente y no desde otro módulo
    app.run(debug=True) #Ejecuta la aplicación