from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Importamos TODOS los modelos
from flask_app.models.users import User
from flask_app.models.recipes import Recipe

@app.route("/new")
def new_recipe():
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    return render_template("new.html")

@app.route("/create", methods=['POST'])
def create_recipe():
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Validar que la info de receta es correcta
    if not Recipe.validate_recipe(request.form):
        return redirect("/new")

    #Guardar la receta
    Recipe.save(request.form)
    #Redireccionar a dashboard
    return redirect("/dashboard")

@app.route("/edit/<int:id>")
def edit_recipe(id):
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #ID de la receta
    data_receta = {"id": id}
    #Instancia de receta
    recipe = Recipe.get_by_id(data_receta)

    return render_template("edit.html", recipe=recipe)

@app.route("/update", methods=["POST"])
def update_recipe():
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Recibimos request.form = {}
    #Validar que la info de receta es correcta
    if not Recipe.validate_recipe(request.form):
        return redirect("/edit/"+request.form['id'])
    
    Recipe.update(request.form)
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete_recipe(id):
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    data_receta = {"id": id}
    #Método que elimine un registro en base al id
    Recipe.delete(data_receta)
    return redirect("/dashboard")