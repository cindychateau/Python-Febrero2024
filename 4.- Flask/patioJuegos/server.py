from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def nivel_uno():
    return render_template("index.html", num=3)

@app.route("/play/<int:numero>")
def nivel_dos(numero):
    return render_template("index.html", num=numero)



if __name__=="__main__":
    app.run(debug=True)