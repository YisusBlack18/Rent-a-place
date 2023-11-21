import os
from flask import Flask, json, jsonify, redirect, render_template, request, session, url_for
from propiedades import filtrar_propiedades, obtener_dict_propiedades, obtener_propiedad, obtener_propiedades, obtener_propiedades_por_dueno, obtener_valores_base
from rentas import insertar_renta, obtener_dict_rentas
from datetime import datetime
from solicitudes_aprobacion import guarda_archivos_local, registrar_anuncio

from usuarios import obtener_dict_usuario, validar_correo, validar_telefono, verifica_correo, verifica_login, verifica_registro, verifica_telefono, obtener_idusuario_por_email

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {}

# Esta ruta es para la pagina principal
@app.route('/', methods=['GET', 'POST'])
def index():
    propiedades = obtener_dict_propiedades()
    if 'email' in session:
        email = session['email']
        tipo = session['tipo']
        return render_template('index.html', propiedades=propiedades, email=email, tipo=tipo)
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
            session['tipo'] = obtener_dict_usuario(obtener_idusuario_por_email(email)[0][0])['Tipo']
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
                tipo = session['tipo']
                return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno, email=email, tipo=tipo)
            else:
                return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno)
        else:
            propiedades = obtener_dict_propiedades()
            dict_valores = obtener_valores_base()
            zonas = dict_valores["zonas"]
            fechas = dict_valores["fechas"]
            if 'email' in session:
                email = session['email']
                tipo = session['tipo']
                return render_template('propiedades.html', propiedades=propiedades, zonas=zonas, fechas=fechas, email=email, tipo=tipo)
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

# Esta ruta es para mostrar la lista de todas las propiedades en la vista del Admin 
@app.route('/propiedadesAdmin', methods=['GET','POST'])
@app.route('/propiedadesAdmin/<propiedad>', methods=['GET','POST'])
def propiedadesAdmin(propiedad='lista'):
    if request.method == 'GET':
        if 'tipo' in session:
            tipoUsuario = session['tipo']
        else:
            tipoUsuario = 'Invitado'

        if tipoUsuario == 'Administrador':
            if propiedad != 'lista':
                propiedad = obtener_dict_propiedades()[int(propiedad)]
                dueno = obtener_dict_usuario(int(propiedad['ID_dueno']))
                if 'email' in session:
                    email = session['email']
                    tipo = session['tipo']
                    return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno, email=email, tipo=tipo)
                else:
                    return render_template('casaIndividual.html', propiedad=propiedad, dueno=dueno)
            else:
                propiedades = obtener_dict_propiedades()
                dict_valores = obtener_valores_base()
                zonas = dict_valores["zonas"]
                fechas = dict_valores["fechas"]
                if 'email' in session:
                    email = session['email']
                    tipo = session['tipo']
                    return render_template('propiedadesAdmin.html', propiedades=propiedades, zonas=zonas, fechas=fechas, email=email, tipo=tipo)
                return render_template('propiedadesAdmin.html', propiedades=propiedades, zonas=zonas, fechas=fechas)
        else:
            return redirect(url_for('index'))
        
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
        return render_template('propiedadesAdmin.html', propiedades=propiedades, zonas=zonas, fechas=fechas)
    
    # Esta ruta es para mostrar la lista de propiedades personales del arrendador
@app.route('/propiedadesPersonales', methods=['GET','POST'])
@app.route('/propiedadesPersonales/<propiedad>', methods=['GET','POST'])
def propiedadesPersonales(propiedad='lista'):
    if request.method == 'GET':
        if 'tipo' in session:
            tipoUsuario = session['tipo']
        else:
            tipoUsuario = 'Invitado'

        if tipoUsuario == 'Arrendador':
            if 'email' in session:
                email = session['email']
                tipo = session['tipo']
                idUsuario = obtener_idusuario_por_email(email)
                propiedades = obtener_propiedades_por_dueno(idUsuario[0][0])
                dict_valores = obtener_valores_base()
                zonas = dict_valores["zonas"]
                fechas = dict_valores["fechas"]
                return render_template('propiedadesPersonales.html', propiedades=propiedades, zonas=zonas, fechas=fechas, email=email, tipo = tipo)
        else:
            return redirect(url_for('login'))
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
        return render_template('propiedadesPersonales.html', propiedades=propiedades, zonas=zonas, fechas=fechas)

# Esta ruta es para mostrar la lista de propiedades previas
# Esto fue copiado de la ruta anterior, pero se debe modificar para que muestre las propiedades rentadas previamente
@app.route('/rentasPrevias', methods=['GET','POST'])
@app.route('/rentasPrevias/<renta>', methods=['GET','POST'])
def rentasPrevias(renta='lista'):
    if renta != 'lista':
        if 'email' in session:
            email = session['email']
            tipo = session['tipo']
            idUsuario = obtener_idusuario_por_email(email)
            propiedad = obtener_dict_rentas(idUsuario[0][0])[int(renta)]
            dueno = obtener_dict_usuario(int(propiedad['ID_dueno']))
            return render_template('casaRentada.html', propiedad=propiedad, dueno=dueno, email=email, tipo=tipo)
        else:
                return redirect(url_for('login'))
    else:
        if 'email' in session:
            email = session['email']
            tipo = session['tipo']
            idUsuario = obtener_idusuario_por_email(email)
            propiedades = obtener_dict_rentas(idUsuario[0][0])
            return render_template('rentasPrevias.html', propiedades=propiedades, email=email, tipo=tipo)
        else:
                return redirect(url_for('login'))

@app.route('/anunciar', methods=['GET', 'POST'])
@app.route('/anunciar/<resultado>', methods=['GET', 'POST'])
def anunciar(resultado='anuncio'):
    if request.method == 'GET':
        if 'email' in session:
            email = session['email']
            tipo = session['tipo']
            if resultado == 'exito':
                return render_template('anuncioExitoso.html', email=email,tipo=tipo)
            else:
                return render_template('subirPropiedad.html', email=email,tipo=tipo)
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        if 'email' in session:
            email = session['email']
            tipo = session['tipo']
        
        data = request.form
        categoria = data['alojamiento']
        titulo = data['titulo']
        explicacion = data['explicacion']
        precio = data['precio']
        habitaciones = data['habitaciones']
        salas = data['salas']
        banos = data['banos']
        metros = data['metros']
        edad = data['edadCasa']
        acondicionado = data['aireAcondicionado']
        wifi = data['wifi']
        television = data['television']
        amueblada = data['amueblada']
        cochera = data['cochera']
        estado = data['estado']
        personas = data['personas']
        zona = data['zona']
        colonia = data['colonia']
        calle = data['calle']
        mapa = data['mapaUbicacion']
        fotoPropiedad = request.files['imagenPropiedad']
        nombreContacto = data['nombreContacto']
        emailContacto = data['emailContacto']
        telefonoContacto = data['telefonoContacto']
        redSocialContacto = data['redSocialContacto']
        # fotoContacto = data['fotoContacto']
        fotoContacto = request.files['fotoContacto']
        # documentosContacto = data['documentosContacto']
        documentosContacto = request.files['documentosContacto']

        guarda_archivos_local(fotoPropiedad)
        guarda_archivos_local(fotoContacto)
        guarda_archivos_local(documentosContacto)

        if registrar_anuncio(categoria,titulo,explicacion,precio,habitaciones,salas,banos,metros,edad,acondicionado,wifi,television,amueblada,cochera,estado,personas,
                          zona,colonia,calle,mapa,fotoPropiedad.filename,nombreContacto,emailContacto,telefonoContacto,redSocialContacto,fotoContacto.filename,documentosContacto.filename):
            return redirect(url_for('anunciar', resultado='exito'))
        else:
            return render_template('subirPropiedad.html', error='Registro fallo, Servicio no disponible, intente mas tarde', email=email, tipo=tipo)

@app.route('/anuncioExistoso', methods=['GET', 'POST'])

@app.route('/rentar', methods=['GET','POST'])
@app.route('/rentar/<propiedad>', methods=['GET','POST'])
def rentar(propiedad='lista'):
    propiedad = obtener_dict_propiedades()[int(propiedad)]
    dueno = obtener_dict_usuario(int(propiedad['ID_dueno']))

    huespedes = request.form['huespedes']
    llegada= datetime.strptime(request.form['llegada'], '%Y-%m-%d')
    salida = datetime.strptime(request.form['salida'], '%Y-%m-%d')
    session['huespedes'] = huespedes
    session['llegada'] = llegada
    session['salida'] = salida
    if 'email' in session:
        email = session['email']
        tipo = session['tipo']
        return render_template('informacionRenta.html', propiedad=propiedad, dueno=dueno, email=email, tipo=tipo, huespedes=huespedes, llegada=llegada, salida=salida)
    else:
        return redirect(url_for('login'))


@app.route('/pagar', methods=['GET', 'POST'])
@app.route('/pagar/<propiedad>', methods=['GET', 'POST'])
@app.route('/pagar/<propiedad>/<rentado>', methods=['GET', 'POST'])
def pagar(propiedad='lista', rentado=False):
    id_propiedad = int(propiedad)
    propiedad = obtener_dict_propiedades()[int(propiedad)]
    email = session['email']
    tipo = session['tipo']
    id= obtener_idusuario_por_email(email)
    huespedes = session['huespedes']
    llegada = session['llegada']
    salida = session['salida']
    if(rentado==False):
        return render_template('pagoRenta.html', propiedad=propiedad, rentado=rentado, email=email, tipo=tipo)
    else:
        insertar_renta(huespedes,llegada,salida,id[0][0],id_propiedad)
        return render_template('pagoRenta.html', email=email, tipo=tipo,propiedad = propiedad, huespedes=huespedes, llegada=llegada,salida=salida)

if __name__ == "__main__":
    app.run(debug=True)