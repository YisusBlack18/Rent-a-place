from mysql.connector import Error
from controlador_base_datos import crear_conexion_local

def obtener_propiedades():
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM propiedades")
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def obtener_propiedad(id_propiedad):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM propiedades WHERE id_propiedad = {}".format(id_propiedad))
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def crea_dict_propiedades():
    propiedades = obtener_propiedades()
    dict_propiedades = {}
    for propiedad in propiedades:
        casa = {
            "ID": propiedad[0],
            "Titulo" : propiedad[1],
            "Descripcion": propiedad[2],
            "Categoria" : propiedad[3],
            "Precio" : propiedad[4],
            "Metros2" : propiedad[5],
            "Direccion" : propiedad[6],
            "NoHabitaciones" : propiedad[7],
            "NoSalas" : propiedad[8],
            "NoBanios" : propiedad[9],
            "NoPersonas" : propiedad[10],
            "ZonaEstado" : propiedad[11],
            "Antiguedad" : propiedad[12],
            "Estado" : propiedad[13],
            "Amueblada" : propiedad[14],
            "Cochera" : propiedad[15],
            "WIFI" : propiedad[16],
            "Television" : propiedad[17],
            "Refrigeradora" : propiedad[18],
            "Fotos" : propiedad[19],
        }
        dict_propiedades[propiedad[0]] = casa
    return dict_propiedades

def obtener_dict_propiedades():
    return crea_dict_propiedades()

def crear_conexion():
    return crear_conexion_local()

if __name__ == '__main__':
    print("Este archivo no se ejecuta")