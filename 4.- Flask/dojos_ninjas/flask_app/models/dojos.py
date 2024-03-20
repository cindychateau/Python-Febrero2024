from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data):
        #data = {id: 1, name: "Java", created......}
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Una lista con todos los ninjas
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query) #Lista de Diccionarios
        '''
        results = [
            {id: 1, nombre: Java, created_at:0000-00-00, updated_at: 0000-00-00},
            {id: 2, nombre: MERN, created_at:0000-00-00, updated_at: 0000-00-00},
            {id: 3, nombre: Python, created_at:0000-00-00, updated_at: 0000-00-00},
        ]
        '''
        dojos = []
        for d in results:
            #d = {id: 1, nombre: Java, created_at:0000-00-00, updated_at: 0000-00-00}
            dojos.append(cls(d)) #cls(d) -> Crea instancia de Dojo. append-> agrega la instancia a la lista
        return dojos
    
    @classmethod
    def save(cls, formulario):
        #formulario = {"nombre": "Fundamentos de la Web"}
        query = "INSERT INTO dojos (nombre) VALUES (%(nombre)s)"
        result = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, formulario)
        return result

    #Método que me regrese también la lista de ninjas