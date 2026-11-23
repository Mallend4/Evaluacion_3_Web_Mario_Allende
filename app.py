
from flask import Flask, render_template, request

app = Flask(__name__)

print("CARPETA DE PLANTILLAS:", app.jinja_loader.searchpath)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        resultado = f"Promedio: {promedio:.1f} - {estado}"

    return render_template('ejercicio1.html',
                           resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        nombre_largo = max(nombres, key=len)
        cantidad = len(nombre_largo)

        resultado = f"El nombre con más caracteres es: {nombre_largo}. Tiene {cantidad} caracteres."

    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run()
