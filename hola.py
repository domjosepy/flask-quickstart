from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "<p>Hola, Mundo!</p>"

@app.route("/titulo-2")
def titulo2():
    return "<h2>Mi mensaje personalizado.</h2>"

@app.route("/parrafo")
def parrafo():
    return "<p>ejercicio 2 terminado</p>"


