from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #Mandar los mensajes temporales de validación

import re #Expresiones Regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Patrón de email

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
    
    @classmethod
    def mostrar(cls, diccionario):
        #diccionario = {"id": 1}
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('crud_modularizado').query_db(query, diccionario) #Lista de diccionarios
        '''
        result = [
            {"id": 1, "nombre": "Elena", "apellido":"De Troya"......} -> 0
        ]
        '''
        usuario = cls(result[0])
        return usuario
    
    @classmethod
    def actualizar(cls, formulario):
        #formulario = {"id": 1, "nombre": "Elena", "apellido":"De Troya".....}
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('crud_modularizado').query_db(query, formulario)
        return result
    
    @staticmethod
    def valida_usuario(formulario): #formulario = Diccionario
        is_valid = True #Asumimos que el formulario está llenado correctamente

        if len(formulario['nombre']) < 3:
            #Mensaje de error
            flash("El nombre debe de tener al menos 3 caracteres", "registro")
            is_valid = False
        
        if len(formulario['apellido']) < 3:
            flash("El apellido debe de tener al menos 3 caracteres", "registro")
            is_valid = False
        
        #Verificamos con Expresiones Regulares que el correo tenga el formato correcto
        if not EMAIL_REGEX.match(formulario['email']):
            flash("E-mail inválido", "registro")
            is_valid = False
        
        #Consultar si existe ese correo en la base de datos
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        results = connectToMySQL('crud_modularizado').query_db(query, formulario) #Lista de Dicionarios
        if len(results) >= 1:
            flash("E-mail registrado previamente", "registro")
            is_valid = False
        return is_valid
        

