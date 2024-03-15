from flask_app.config.mysqlconnection import connectToMySQL

class Salon:

    def __init__(self, data):
        #data = {INFO} diccionario consulta
        self.id = data['id']
        self.nombre_salon = data['nombre_salon']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def muestra_salones(cls):
        query = "SELECT * FROM salones"
        results = connectToMySQL('esquema_salones').query_db(query) #Lista de Diccionarios
        '''
        results = [
            {"id": 1, "nombre_salon": "Java".....},
            {"id": 2, "nombre_salon": "Python".....},
            {"id": 3, "nombre_salon": "Fundamentos".....},
        ]
        '''
        salones = []
        for salon in results:
            #salon = {"id": 1, "nombre_salon": "Java".....}
            salones.append(cls(salon)) # cls(salon)-> crea la instancia en base al diccionario. salones.append agrega a la lista esa instancia
        return salones