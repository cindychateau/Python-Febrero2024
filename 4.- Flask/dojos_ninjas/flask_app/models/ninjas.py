from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        #data = {Diccionario con toda la info que extraemos de DB}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def save(cls, formulario):
        #formulario = {"first_name": "Elena", "last_name": "De Troya", "age": 18, "dojo_id": 1}
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        result = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, formulario)
        return result