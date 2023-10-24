from controlador_base_datos import crear_conexion_local
from mysql.connector import Error

def registrar_anuncio(categoria,titulo,explicacion,precio,habitaciones,salas,banos,metros,edad,acondicionado,wifi,television,amueblada,cochera,estado,personas,zona,colonia,calle,mapa,fotoPropiedad,nombreContacto,emailContacto,telefonoContacto,redSocialContacto,fotoContacto,documentosContacto):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        direccion = calle + ", " + colonia
        c.execute("INSERT INTO solicitud_anuncio (Categoria,Titulo,Descripcion,Precio,NoHabitaciones,NoSalas,NoBanios,Metros2,Antiguedad,Refrigeradora,WIFI,Television,Amueblada,Cochera,Estado,NoPersonas,ZonaEstado,Direccion,UrlMapa,Fotos,nombre,email,telefono,redSocial,imagen,documentos) VALUES ('{categoria}','{titulo}','{explicacion}','{precio}','{habitaciones}','{salas}','{banos}','{metros}','{edad}','{acondicionado}','{wifi}','{television}','{amueblada}','{cochera}','{estado}','{personas}','{zona}','{direccion}','{mapa}','{fotoPropiedad}','{nombreContacto}','{emailContacto}','{telefonoContacto}','{redSocialContacto}','{fotoContacto}','{documentosContacto}')")
        conn.commit()
        conn.close()
        return True
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def crear_conexion():
    return crear_conexion_local()

if __name__ == '__main__':
    print("Este archivo no debe ejecutarse directamente")