from flask_app import app

#importación controlador
from flask_app.controllers import dojos_ninjas_controller

if __name__ == "__main__":
    app.run(debug=True)