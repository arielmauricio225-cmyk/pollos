from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return "<h1>Menú</h1>"

@app.route("/promociones")
def promociones():
    return "<h1>Promociones</h1>"

@app.route("/contacto")
def contacto():
    return "<h1>Contacto</h1>"

if __name__ == "__main__":
    app.run(debug=True)