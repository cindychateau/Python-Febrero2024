from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:

    def __init__(self, data):
        #data(diccionario): {"id": 1, "nombre": "Elena", "apellido", "De troya".....}
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM usuarios"
        results = connectToMySQL('crud_modularizado').query_db(query) #Lista de Diccionarios
        '''
        results = [
            {"id": 1, "nombre": "Elena", "apellido":"De Troya"....},
            {"id": 2, "nombre": "Juana", "apellido":"De Arco"....},
        ]
        '''
        usuarios = []
        for us in results:
            #us = {"id": 1, "nombre": "Elena", "apellido":"De Troya"....}
            usuario = cls(us) #Instancia en base al diccionario que recibe
            usuarios.append(usuario)
        
        return usuarios #Lista de objetos usuario
    
    @classmethod
    def guardar(cls, formulario):
        #formulario = {"nombre": "Elena", "apellido": "De Troya", "email": "elena@codingdojo.com"}
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s)"
        result = connectToMySQL('crud_modularizado').query_db(query, formulario) #ID del nuevo registro
        return result
    
    @classmethod
    def borrar(cls, diccionario):
        #diccionario = {"id": 1}
        query = "DELETE FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('crud_modularizado').query_db(query, diccionario)
        return result