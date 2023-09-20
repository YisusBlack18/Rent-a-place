import os
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]["password"] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')
    else:
        return render_template('login.html')

# Esta ruta es para cerrar la sesión del usuario
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        telefono = request.form['telefono']
        if username in users:
            return render_template('registro.html', error='Ese nombre de usuario ya está en uso')
        else:
            users[username] = {'username': username, 'password': password, 'name': name, 'telefono': telefono}
            session['username'] = username
            return redirect(url_for('index'))
    else:
        return render_template('registro.html')

# Esta ruta es para mostrar la lista de usuarios registrados
@app.route('/users')
def user_list():
    if len(users.keys()) > 0:
        return render_template('user_list.html', users=users)
    else:
        return render_template('404.html'), 404

# Esta ruta es para mostrar la información de un usuario en específico
@app.route('/users/<username>', methods=['GET','POST'])
def user(username):
    if request.method == 'POST':
        if request.form['action'] == 'delete':
            users.pop(username, None)
            return redirect(url_for('user_list'))
        else:
            return render_template('404.html'), 404
    if username in users:
        return render_template('user.html', user=users[username], session=session)
    else:
        return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)