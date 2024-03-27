from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Modelos
from flask_app.models.messages import Message

@app.route("/send_message", methods=['POST'])
def send_message():
    #request.form = {"content": "HOLI", "sender_id": ID EN SESION, "receiver_id": ID recibe}
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Guardamos el mensaje -> Verificar que la info sea correcta
    Message.save(request.form)
    return redirect("/dashboard")

#/delete/3
@app.route("/delete/<int:id>") #en mi URL obtengo el ID del mensaje a borrar
def delete(id): #id = 3
    form = {"id": id} #{"id": 3}
    Message.delete_message(form)
    return redirect("/dashboard")