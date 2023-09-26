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
            "ID_dueno": propiedad[1],
            "Titulo" : propiedad[2],
            "Descripcion": propiedad[3],
            "Categoria" : propiedad[4],
            "Precio" : propiedad[5],
            "Metros2" : propiedad[6],
            "Direccion" : propiedad[7],
            "NoHabitaciones" : propiedad[8],
            "NoSalas" : propiedad[9],
            "NoBanios" : propiedad[10],
            "NoPersonas" : propiedad[11],
            "ZonaEstado" : propiedad[12],
            "Antiguedad" : propiedad[13],
            "Estado" : propiedad[14],
            "Amueblada" : propiedad[15],
            "Cochera" : propiedad[16],
            "WIFI" : propiedad[17],
            "Television" : propiedad[18],
            "Refrigeradora" : propiedad[19],
            "Banos" : "Si" if propiedad[10] != 0 else "No",
            "Fotos" : propiedad[20],
            "Fecha" : propiedad[21]
        }
        dict_propiedades[propiedad[0]] = casa
    return dict_propiedades

def obtener_dict_propiedades():
    return crea_dict_propiedades()

def crear_conexion():
    return crear_conexion_local()

def filtrar_propiedades(zona,precio,fecha,numHabitaciones):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM propiedades WHERE ZonaEstado = '{}' AND Precio <= {} AND NoHabitaciones = {}".format(zona,precio,numHabitaciones))
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

if __name__ == '__main__':
    print("Este archivo no se ejecuta")