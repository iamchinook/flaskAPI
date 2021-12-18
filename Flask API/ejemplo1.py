from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return "<h1>Hola, buenos días</h1>"

@app.route("/ingreso")
def ingreso():
    return "<h2>Ingreso</h2>"


# Rutas Dinámicas
@app.route("/usuarios/<nombre>")
def saludar(nombre):
    return "<h2>El largo del nombre {} es {}".format(nombre, len(nombre))

@app.route("/edad/<nombre>/<edad>")
def edad(nombre, edad):
    return "<h2>{} tiene {} años".format(nombre, edad)

@app.route("/sumar/<n1>/<n2>")
def sumar(n1, n2):
    resultado = int(n1) + int(n2)
    return "<h2>{} más {} es {}".format(n1, n2, resultado)

# Arreglar errores con debug
if __name__ == '__main__':
    app.run(debug=True)
