import os
from controlador_base_datos import crear_conexion_local
from mysql.connector import Error

def registrar_anuncio(categoria,titulo,explicacion,precio,habitaciones,salas,banos,metros,edad,acondicionado,wifi,television,amueblada,cochera,estado,personas,zona,colonia,calle,mapa,fotoPropiedad,nombreContacto,emailContacto,telefonoContacto,redSocialContacto,fotoContacto,documentosContacto):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        direccion = calle + ", " + colonia
        c.execute(f"INSERT INTO solicitudes_anuncio (Categoria,Titulo,Descripcion,Precio,NoHabitaciones,NoSalas,NoBanios,Metros2,Antiguedad,Refrigeradora,WIFI,Television,Amueblada,Cochera,Estado,NoPersonas,ZonaEstado,Direccion,UrlMapa,Fotos,nombre,email,telefono,redSocial,imagen,documentos) VALUES ('{categoria}','{titulo}','{explicacion}','{precio}','{habitaciones}','{salas}','{banos}','{metros}','{edad}','{acondicionado}','{wifi}','{television}','{amueblada}','{cochera}','{estado}','{personas}','{zona}','{direccion}','{mapa}','{fotoPropiedad}','{nombreContacto}','{emailContacto}','{telefonoContacto}','{redSocialContacto}','{fotoContacto}','{documentosContacto}')")
        conn.commit()
        conn.close()
        return True
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

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