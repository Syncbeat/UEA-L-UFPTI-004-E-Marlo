from flask import Flask, render_template, request, redirect, url_for
from conexion.conexion import obtener_conexion

app = Flask(__name__)

@app.route('/')
def index():
    #Consultar registros
    db = obtener_conexion()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    lista_usuarios = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', usuarios=lista_usuarios)

@app.route('/agregar', methods=['POST'])
def agregar_usuario():
    # Ejemplo: Insertar registros
    nombre = request.form['nombre']
    mail = request.form['mail']
    pwd = request.form['password']
    
    db = obtener_conexion()
    cursor = db.cursor()
    sql = "INSERT INTO usuarios (nombre, mail, password) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, mail, pwd))
    db.commit() # Importante para guardar cambios
    cursor.close()
    db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
