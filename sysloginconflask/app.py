from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import obtener_conexion
from models import User

app = Flask(__name__)
app.secret_key = 'super_secreta_y_dificil_de_adivinar'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'

@login_manager.user_loader
def load_user(user_id):
    conexion = obtener_conexion()
    with conexion.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = ?", (user_id,))
        user_data = cursor.fetchone()
    conexion.close()
    
    if user_data:
        return User(user_data['id_usuario'], user_data['nombre'], user_data['email'], user_data['password'])
    return None

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        
        password_hash = generate_password_hash(password)
        
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)", 
                    (nombre, email, password_hash)
                )
            conexion.commit()
            flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.')
            return redirect(url_for('login'))
        except Exception:
            flash('Error al registrar: Es posible que el correo ya esté en uso.')
        finally:
            conexion.close()
            
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('panel'))

    if request.method == 'POST':
        email = request.form['email']
        password_ingresada = request.form['password']
        
        conexion = obtener_conexion()
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            user_data = cursor.fetchone()
        conexion.close()
        
        if user_data and check_password_hash(user_data['password'], password_ingresada):
            user = User(user_data['id_usuario'], user_data['nombre'], user_data['email'], user_data['password'])
            login_user(user)
            return redirect(url_for('panel'))
        else:
            flash('Correo o contraseña incorrectos.')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.')
    return redirect(url_for('login'))

@app.route('/panel')
@login_required
def panel():
    return render_template('panel.html', nombre=current_user.nombre)

if __name__ == '__main__':
    app.run(debug=True)