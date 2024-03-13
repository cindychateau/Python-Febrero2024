#Importaciones
from flask import Flask, render_template, request, redirect

#Importar la app
from flask_app import app

#Importar todos los modelos
from flask_app.models.usuarios import Usuario

#Rutas
@app.route("/")
def index():
    usuarios = Usuario.muestra_usuarios() #Lista de objetos usuario
    return render_template('index.html', users=usuarios)

@app.route("/nuevo")
def nuevo():
    return render_template('nuevo.html')

@app.route("/crear", methods=["POST"])
def crear():
    #Recibir un formulario-> request.form = {"nombre": "elena", "apellido": "de troya", "email": "email@.com"}
    Usuario.guardar(request.form)
    return redirect("/")

@app.route("/borrar/<int:id>") # /borrar/1
def borrar(id): #id = 1
    diccionario = {"id": id} #diccionario = {"id": 1}
    Usuario.borrar(diccionario)
    return redirect("/")
