import os
from flask import Flask, redirect, render_template, request, session, url_for
from propiedades import filtrar_propiedades, obtener_dict_propiedades, obtener_propiedad, obtener_propiedades, obtener_valores_base

from usuarios import obtener_dict_usuario, validar_correo, validar_telefono, verifica_correo, verifica_login, verifica_registro, verifica_telefono

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {}

# Esta ruta es para la pagina principal
@app.route('/', methods=['GET', 'POST'])
def index():
    propiedades = obtener_dict_propiedades()
    if 'email' in session:
        email = session['email']
        return render_template('index.html', propiedades=propiedades, email=email)
    else:
        return render_template('index.html', propiedades=propiedades)

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

# Esta ruta es para mostrar la lista de propiedades
@app.route('/propiedades', methods=['GET','POST'])
@app.route('/propiedades/<propiedad>', methods=['GET','POST'])
def propiedades(propiedad='lista'):
    if request.method == 'GET':
        if propiedad != 'lista':
            propiedad = obtener_dict_propiedades()[int(propiedad)]
            dueno = obtener_dict_usuario(int(propiedad['ID_dueno']))
            if 'email' in session:
                email = session['email']
                return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno, email=email)
            else:
                return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno)
        else:
            propiedades = obtener_dict_propiedades()
            dict_valores = obtener_valores_base()
            zonas = dict_valores["zonas"]
            fechas = dict_valores["fechas"]
            if 'email' in session:
                email = session['email']
                return render_template('propiedades.html', propiedades=propiedades, zonas=zonas, fechas=fechas, email=email)
            return render_template('propiedades.html', propiedades=propiedades, zonas=zonas, fechas=fechas)
    elif request.method == 'POST':
        zona = request.form['zona']
        precio = request.form.get('precio',type=int)
        fecha = request.form['fechas']
        numHabitaciones = request.form.get('numHabitaciones')
        buscar = request.form['buscar']
        propiedades = filtrar_propiedades(zona,precio,fecha,numHabitaciones,buscar)
        dict_valores = obtener_valores_base()
        zonas = dict_valores["zonas"]
        fechas = dict_valores["fechas"]
        return render_template('propiedades.html', propiedades=propiedades, zonas=zonas, fechas=fechas)
    
# Esta ruta es para mostrar la lista de propiedades previas
# Esto fue copiado de la ruta anterior, pero se debe modificar para que muestre las propiedades rentadas previamente
@app.route('/rentasPrevias', methods=['GET','POST'])
@app.route('/rentasPrevias/<propiedad>', methods=['GET','POST'])
def rentasPrevias(propiedad='lista'):
    if request.method == 'GET':
        if propiedad != 'lista':
            propiedad = obtener_dict_propiedades()[int(propiedad)]
            dueno = obtener_dict_usuario(int(propiedad['ID_dueno']))
            if 'email' in session:
                email = session['email']
                return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno, email=email)
            else:
                return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno)
        else:
            propiedades = obtener_dict_propiedades()
            dict_valores = obtener_valores_base()
            zonas = dict_valores["zonas"]
            fechas = dict_valores["fechas"]
            if 'email' in session:
                email = session['email']
                return render_template('rentasPrevias.html', propiedades=propiedades, zonas=zonas, fechas=fechas, email=email)
            return render_template('rentasPrevias.html', propiedades=propiedades, zonas=zonas, fechas=fechas)
    elif request.method == 'POST':
        zona = request.form['zona']
        precio = request.form.get('precio',type=int)
        fecha = request.form['fechas']
        numHabitaciones = request.form.get('numHabitaciones')
        buscar = request.form['buscar']
        propiedades = filtrar_propiedades(zona,precio,fecha,numHabitaciones,buscar)
        dict_valores = obtener_valores_base()
        zonas = dict_valores["zonas"]
        fechas = dict_valores["fechas"]
        return render_template('rentasPrevias.html', propiedades=propiedades, zonas=zonas, fechas=fechas)

@app.route('/anunciar', methods=['GET', 'POST'])
def anunciar():
    return render_template('anuncioExitoso.html')

@app.route('/rentar', methods=['GET','POST'])
def rentar():
    return render_template('informacionRenta.html')

@app.route('/pagar', methods=['GET', 'POST'])
def pagar():
    return render_template('pagoRenta.html')

@app.route('/subirPropiedadSegundoPaso', methods=['GET', 'POST'])
def subirSegundo():
    return render_template('subirPropiedadSegundoPaso.html')

if __name__ == "__main__":
    app.run(debug=True)