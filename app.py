import os
from flask import Flask, redirect, render_template, request, session, url_for

from usuarios import validar_correo, validar_telefono, verifica_correo, verifica_login, verifica_registro, verifica_telefono

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {}

# Esta ruta es para la pagina principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'email' in session:
        email = session['email']
        return render_template('index.html', email=email)
    else:
        return render_template('index.html')

# Esta ruta es para iniciar sesión del usuario
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if verifica_login(email,password):
            session['email'] = email
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Correo o contraseña incorrectos')
    else:
        return render_template('login.html')

# Esta ruta es para cerrar la sesión del usuario
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

# Esta ruta es para registrar un usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['nombre']
        telefono = request.form['celular']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        terminos = request.form['terminos']
        if password != password2:
            return render_template('registro.html', error='Las contraseñas no coinciden')
        elif validar_correo(email):
            return render_template('registro.html', error='Formato de correo no valido')
        elif verifica_correo(email):
            return render_template('registro.html', error='Ese correo ya está en uso')
        elif validar_telefono(telefono):
            return render_template('registro.html', error='Formato de telefono no valido')
        elif verifica_telefono(telefono):
            return render_template('registro.html', error='Ese telefono ya esta en uso')
        elif terminos != 'on':
            return render_template('registro.html', error='Favor de aceptar terminos y condiciones')
        else:
            if verifica_registro(name,telefono,email,password):
                session['email'] = email
                return redirect(url_for('index'))
            else:
                return render_template('registro.html', error='Registro fallo, Servicio no disponible, intente mas tarde')
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

@app.route('/propiedades/<propiedad>')
def propiedades(propiedad='lista'):
    if propiedad != 'lista':
        if 'email' in session:
            email = session['email']
            return render_template('casaIndividual.html', email=email)
        else:
            return render_template('casaIndividual.html')
    else:
        if 'email' in session:
            email = session['email']
            return render_template('propiedades.html', email=email)
        return render_template('propiedades.html')
    

    # Este es solamente de prueba para ver como se veia, no es importante!!! 
@app.route('/casaIndividual')
def casaIndividual():
    if 'email' in session:
        email = session['email']
        return render_template('casaIndividual.html', email=email)
    else:
        return render_template('casaIndividual.html')

if __name__ == "__main__":
    app.run(debug=True)