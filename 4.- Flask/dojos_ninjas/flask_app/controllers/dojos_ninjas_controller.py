from flask import Flask, redirect, request, render_template
from flask_app import app

#Modelos
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

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
    lista_dojos = Dojo.get_all() #Lista instancias de Dojo
    return render_template("ninjas.html", dojos=lista_dojos) #enviar la lista de dojos

#Recibir formulario
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    #request.form = {"first_name":"Elena", "last_name": "De Troya", "age":18, "dojo_id": 1}
    Ninja.save(request.form)
    return redirect('/dojos/'+request.form['dojo_id']) #Redirecciona al dojo al que pertenece


@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {"id": id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojo.html', dojo=dojo)