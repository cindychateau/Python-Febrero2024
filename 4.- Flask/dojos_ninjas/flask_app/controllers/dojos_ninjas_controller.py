from flask import Flask, redirect, request, render_template
from flask_app import app

#Modelos
from flask_app.models.dojos import Dojo
#PENDIENTE: import Ninja

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    lista_dojos = Dojo.get_all() #Lista de objetos Dojo
    return render_template("dojos.html", dojos=lista_dojos)

@app.route("/create/dojo", methods=['POST'])
def create_dojo():
    #request.form = {"nombre": "Python"}
    Dojo.save(request.form)
    return redirect("/dojos")

@app.route("/ninjas")
def new_ninja():
    #Genere una lista de dojos
    return render_template("ninjas.html") #enviar la lista de dojos