from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "super clave secreta"

@app.route("/")
def index():
    #Formulario
    return render_template("index.html") 

@app.route("/enviar_formulario", methods=["POST"])
def enviar_formulario():
    print(request.form)
    '''
    request.form = {
        "nombre": "Elena de Troya",
        "email": "elena@codingdojo.com"
    }
    '''
    session['nombre'] = request.form['nombre']
    return redirect("/exito")

@app.route("/exito")
def exito():
    return render_template("exito.html")



if __name__ == "__main__":
    app.run(debug=True)