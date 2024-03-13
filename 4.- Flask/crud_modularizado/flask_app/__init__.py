#Importar flask
from flask import Flask

#Inicialización de app
app = Flask(__name__)

#Declaramos llave secreta
app.secret_key = "La llave secreta de sesión"