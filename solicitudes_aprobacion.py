import os
from controlador_base_datos import crear_conexion_local
from mysql.connector import Error

def registrar_anuncio(idUser,categoria,titulo,explicacion,precio,habitaciones,salas,banos,metros,edad,acondicionado,wifi,television,amueblada,cochera,estado,personas,zona,colonia,calle,mapa,fotoPropiedad,nombreContacto,emailContacto,telefonoContacto,redSocialContacto,fotoContacto,documentosContacto):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        direccion = calle + ", " + colonia
        c.execute(f"INSERT INTO solicitudes_anuncio (ID_usuario,Categoria,Titulo,Descripcion,Precio,NoHabitaciones,NoSalas,NoBanios,Metros2,Antiguedad,Refrigeradora,WIFI,Television,Amueblada,Cochera,Estado,NoPersonas,ZonaEstado,Direccion,UrlMapa,Fotos,nombre,email,telefono,redSocial,imagen,documentos) VALUES ('{idUser}','{categoria}','{titulo}','{explicacion}','{precio}','{habitaciones}','{salas}','{banos}','{metros}','{edad}','{acondicionado}','{wifi}','{television}','{amueblada}','{cochera}','{estado}','{personas}','{zona}','{direccion}','{mapa}','{fotoPropiedad}','{nombreContacto}','{emailContacto}','{telefonoContacto}','{redSocialContacto}','{fotoContacto}','{documentosContacto}')")
        conn.commit()
        conn.close()
        return True
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    
def obtener_solicitud(id_solicitud):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM solicitudes_anuncio WHERE ID = {}".format(id_solicitud))
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    
def crea_dict_solicitudes(rows=None):
    if rows is None:
        solicitudes = obtener_solicutudes()
    else:
        solicitudes = rows
    dict_solicitudes = {}
    for solicitud in solicitudes:
        casa = {
            "ID": solicitud[0],
            "ID_usuario" : solicitud[1],
            "Titulo" : solicitud[2],
            "Descripcion": solicitud[3],
            "Categoria" : solicitud[4],
            "Precio" : solicitud[5],
            "Metros2" : solicitud[6],
            "Direccion" : solicitud[7],
            "NoHabitaciones" : solicitud[8],
            "NoSalas" : solicitud[9],
            "NoBanios" : solicitud[10],
            "NoPersonas" : solicitud[11],
            "ZonaEstado" : solicitud[12],
            "Antiguedad" : solicitud[13],
            "Estado" : solicitud[14],
            "Amueblada" : solicitud[15],
            "Cochera" : solicitud[16],
            "WIFI" : solicitud[17],
            "Television" : solicitud[18],
            "Refrigeradora" : solicitud[19],
            "Banos" : "Si" if solicitud[10] != 0 else "No",
            "Fotos" : solicitud[20],
            "Mapa" : solicitud[21],
            "Fecha" : solicitud[22],
            "nombreUsuario" : solicitud[23],
            "telefonoUsuario" : solicitud[24],
            "emailUsuario" : solicitud[25],
            "redSocialUsuario" : solicitud[26],
            "imagenUsuario" : solicitud[27],
            "documentosUsuario" : solicitud[28],
        }
        dict_solicitudes[solicitud[0]] = casa
    return dict_solicitudes

def aprobar_solicitud(id_solicitud):
    solicitud = obtener_dict_solicitudes()[int(id_solicitud)]
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute(f"INSERT INTO propiedades (ID_dueno,Titulo,Descripcion,Categoria,Precio,Metros2,Direccion,NoHabitaciones,NoSalas,NoBanios,NoPersonas,ZonaEstado,Antiguedad,Estado,Amueblada,Cochera,WIFI,Television,Refrigeradora,Fotos,UrlMapa,FechaCreacion,Activacion) VALUES ('{solicitud['ID_usuario']}','{solicitud['Titulo']}','{solicitud['Descripcion']}','{solicitud['Categoria']}','{solicitud['Precio']}','{solicitud['Metros2']}','{solicitud['Direccion']}','{solicitud['NoHabitaciones']}','{solicitud['NoSalas']}','{solicitud['NoBanios']}','{solicitud['NoPersonas']}','{solicitud['ZonaEstado']}','{solicitud['Antiguedad']}','{solicitud['Estado']}','{solicitud['Amueblada']}','{solicitud['Cochera']}','{solicitud['WIFI']}','{solicitud['Television']}','{solicitud['Refrigeradora']}','{solicitud['Fotos']}','{solicitud['Mapa']}','{solicitud['Fecha']}',True)")
        conn.commit()
        c.execute(f"DELETE FROM solicitudes_anuncio WHERE ID = {id_solicitud}")
        conn.commit()
        conn.close()
        return True
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def rechazar_solicitud(id_solicitud):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute(f"DELETE FROM solicitudes_anuncio WHERE ID = {id_solicitud}")
        conn.commit()
        conn.close()
        return True
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def obtener_solicutudes():
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM solicitudes_anuncio")
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    
def obtener_dict_solicitudes():
    return crea_dict_solicitudes()

# Esta funcion almacena los archivos en la carpeta de archivos local
def guarda_archivos_local(files):
    # if isinstance(archivos,list):
    #     archivos = archivos[0]
    #     try:
    #         with open(os.path.join(app.config['UPLOAD_FOLDER'], nombre), "wb") as archivo:
    #             archivo.write(archivos)
    #         return True
    #     except Error as err:
    #         print("Algo salio mal: {}".format(err))
    #         return False
    # else:
    #     try:
    #         for file in archivos:
    #             file.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre))
    #         return True
    #     except Error as err:
    #         print("Algo salio mal: {}".format(err))
    #         return False
    if isinstance(files,list):
        for file in files:
            file.save("static/files/" + file.filename)
        return True
    else:
        files.save("static/files/" + files.filename)
        return True

def crear_conexion():
    return crear_conexion_local()

if __name__ == '__main__':
    print("Este archivo no debe ejecutarse directamente")