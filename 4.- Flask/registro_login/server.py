#pipenv install flask pymysql flask-bcrypt

from flask_app import app #Importamos la app

#Importamos controladores
from flask_app.controllers import users_controller

#Ejecución de app
if __name__ == "__main__":
    app.run(debug=True) #(debug=True, port=3400)