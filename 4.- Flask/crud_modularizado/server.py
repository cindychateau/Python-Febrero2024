#Importacion de app
from flask_app import app

#Importación de Controladores
from flask_app.controllers import usuarios_controller

#Ejecución app
if __name__=="__main__":
    app.run(debug=True)