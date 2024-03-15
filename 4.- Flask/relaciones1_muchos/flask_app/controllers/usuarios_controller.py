from flask import Flask, render_template, request, redirect

from flask_app import app

#Importamos los modelos
from flask_app.models.salones import Salon
from flask_app.models.usuarios import Usuario

#RUTAS

@app.route("/")
def index():
    #obtener todos los usuarios
    usuarios = Usuario.muestra_usuarios()
    return render_template('index.html', usuarios=usuarios) #enviar usuarios

@app.route("/nuevo")
def nuevo():
    salones = Salon.muestra_salones() #Lista de instancias de Salon
    return render_template("nuevo.html", salones=salones)

@app.route("/guardar", methods=['POST'])
def guardar():
    #Recibir la info formulario
    #request.form = {"nombre_completo": "Elena de T.", "email": "elena@cd.com", "salon_id": 1}
    Usuario.guardar_usuario(request.form)
    return redirect("/")