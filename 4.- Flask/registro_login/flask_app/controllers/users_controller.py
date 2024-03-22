from flask import Flask, render_template, redirect, request, session
from flask_app import app

#Importamos TODOS los modelos
from flask_app.models.users import User

#Importamos BCrypt -> Encriptar la contraseña
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    #request.form = {"first_name": "Elena", "last_name": "De Troya"......}

    #Validar que la info sea correcta
    if not User.validate_user(request.form):
        #No es válida info, redirecciono al formulario
        return redirect("/")
    
    #Encriptamos la contra
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    #Generamos un diccionario con toda la info Y LA CONTRA encriptada
    form = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pass_encrypt
    }

    nuevo_id = User.save(form) #Recibiendo el ID del nuevo Usuario
    session['user_id'] = nuevo_id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
