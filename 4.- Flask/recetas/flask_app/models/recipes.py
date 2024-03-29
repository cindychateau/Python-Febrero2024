from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #Mensajes de error

class Recipe:

    def __init__(self, data):
        #data = {claves/columnas: valores}
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        #1 extra - JOIN
        self.user_name = data["user_name"]
    
    @staticmethod
    def validate_recipe(form):
        #form = {la info que el usuario ingresó} - request.form
        is_valid = True

        if len(form["name"]) < 3:
            is_valid = False
            flash("El nombre de la receta debe tener al menos 3 caracteres", "receta")
        
        if len(form["description"]) < 3:
            is_valid = False
            flash("La descripción de la receta debe tener al menos 3 caracteres", "receta")
        
        if len(form["instructions"]) < 3:
            is_valid = False
            flash("Las instrucciones de la receta deben tener al menos 3 caracteres", "receta")

        if form["date_made"] == "":
            is_valid = False
            flash("Ingresa una fecha de creación", "receta")
        
        return is_valid
    
    @classmethod
    def save(cls, form):
        #form = {la info que el usuario ingresó en el formulario} - request.form
        #form = {"name": "Spagetti", "description": "...."....}
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s)"
        result = connectToMySQL('esquema_recetas').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, users.first_name as user_name FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL('esquema_recetas').query_db(query) #Lista de diccionarios
        recipes = []
        for recipe in results:
            #recipe = {diccionario que recibo de bd - registro con columnas}
            recipes.append(cls(recipe)) #cls(recipe) - Genera la instancia en base al diccionario. recipes.append agrega esa instancia a la lista de recetas
        return recipes
    
    @classmethod
    def get_by_id(cls, data):
        #data = {"id": 2}
        query = "SELECT recipes.*, users.first_name as user_name FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s"
        result = connectToMySQL('esquema_recetas').query_db(query, data) #Lista con 1 diccionario
        recipe = cls(result[0])
        return recipe
    
    @classmethod
    def update(cls, form):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id = %(id)s"
        result = connectToMySQL('esquema_recetas').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls, data):
        #data = {"id": 2}
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL('esquema_recetas').query_db(query, data)