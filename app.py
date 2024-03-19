from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import current_user
import requests
#Dependencias necesarias para el aplicativo

app = Flask(__name__)
#Variable de definicion del aplicativo

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3308/accedo_user'
# Conexion via URL a la bd mediante MySQL, OJO!!! cambiar el puerto por el default.
# La DB no cuenta con contraseña
# o el que sea necesario, en mi caso es el 3308, pero el default es 3306, sin embargo solo eliminar esa parte del codigo bastará (localhost/USER) 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Desactiva el seguimiento de modificaciones para mejorar el rendimiento

app.config['SECRET_KEY'] = 'Acc3d0'
#Clave para el manejo de sesion de usuarios de forma segura

db = SQLAlchemy(app)
#definicion de atributo para el uso de SQLALchemy

migrate = Migrate(app, db)
#definicion del atributo para el uso de Flask Migrate

login_manager = LoginManager(app)
#definicion de atributo para el uso de LoginManager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
# Cargar y devolver el usuario basado en el user_id

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
# Crear las tablas en la base de datos

def fetch_api_data():
    api_url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(api_url)
    if response.status_code == 200:
        api_data = response.json()
        return api_data
    else:
        return None
#definicion de variable para el consumo de la API

def fetch_pokemon_details(name):
    api_url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(api_url)
    if response.status_code == 200:
        api_data = response.json()
        return api_data
    else:
        return None
#definicion de variable para el consumo de datos extra de la API.

@app.route('/')
def index():
    api_data = fetch_api_data()
    first_pokemon_name = api_data['results'][0]['name']
    return render_template('index.html', api_data=api_data, pokemon_name=first_pokemon_name)
#Definicion de la ruta del archivo index.html, y la renderizacion de la API

@app.route('/pokemon/<name>')
@login_required
def pokemon_details(name):
    api_data = fetch_pokemon_details(name)
    abilities = api_data['abilities']
    image_url = api_data['sprites']['front_default']
    return render_template('pokemon_details.html', pokemon_name=name, name=name, abilities=abilities, image_url=image_url)
#Definicion de la variable con la que se extrae el nombre, habilidades, etc, de los pokemones, con un decorador que verifica si el usuario esta o no logueado

@app.errorhandler(401)
def unauthorized(error):
    return redirect(url_for('login'))
#Deteccion del aplicativo por si el usuario no esta logueado

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            pokemon_name = request.args.get('pokemon_name')
            if pokemon_name:
                return redirect(url_for('pokemon_details', name=pokemon_name))
            else:
                return redirect(url_for('index'))
        else:
            error_message = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
            return render_template('login.html', error=error_message)
    else:
        return render_template('login.html')
#Manejo de datos y credenciales del usuario

@app.route('/register.html', methods=['GET', 'POST'])
def register_html():
    return render_template('register.html')
#definicion de la ruta del archivo register.html, para la funcion de botones

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error_message = "El nombre de usuario ya está en uso. Por favor, elige otro."
            return render_template('register.html', error=error_message)
            #Verificacion de nombre de usuario ya en uso
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            error_message = "El correo electrónico ya está en uso. Por favor, usa otro."
            return render_template('register.html', error=error_message)
            #Verificacion de nombre de correo ya en uso
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        print(current_user.is_authenticated)
        return redirect(url_for('registro_exitoso'))  
    return render_template('register.html')
#funcionalidad de registro de un usuario mediante el formulario

@app.route('/registro_exitoso')
def registro_exitoso():
    return render_template('confirmation.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))  
#Redirige al usuario a la página de inicio u otra página deseada después de cerrar sesión

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
#condicion del aplicativo, determina si el aplicativo esta en correcto funcionamiento debera continuar