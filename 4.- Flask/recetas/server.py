#pipenv install flask pymysql flask-bcrypt

from flask_app import app #Importamos la app

#Importamos controladores, controlador recetas
from flask_app.controllers import users_controller, recipes_controller

#Ejecución de app
if __name__ == "__main__":
    app.run(debug=True) #(debug=True, port=3400)