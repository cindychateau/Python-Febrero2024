from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:

    def __init__(self, data):
        #data? diccionario con toda la info de mi instancia
        self.id = data['id']
        self.nombre_completo = data['nombre_completo']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.salon_id = data['salon_id']

        #Relación con Salón
        self.nombre_salon = data['nombre_salon']
    
    @classmethod
    def guardar_usuario(cls, formulario):
        #formulario = {"nombre_completo": "Elena de T", "email": "elena@e.com", "salon_id":2}
        query = "INSERT INTO usuarios(nombre_completo, email, salon_id) VALUES(%(nombre_completo)s, %(email)s, %(salon_id)s) "
        result = connectToMySQL('esquema_salones').query_db(query, formulario)
        return result

    #Metodo que obtenga TODOS los usuarios
