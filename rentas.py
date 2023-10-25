import re
from mysql.connector import Error
from controlador_base_datos import crear_conexion_local

def insertar_renta(huespedes, llegada, salida, cliente_id, propiedad_id):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("INSERT INTO rentas(huespedes, llegada, salida, cliente_id, propiedad_id) VALUES({},'{}','{}',{},{});".format(huespedes, llegada, salida, cliente_id, propiedad_id))
        conn.commit()
        conn.close()
        return True
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False


#Obtener toda la tabla de rentas
def obtener_rentas():
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM rentas")
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    
#Obtener las rentas y detalles de propiedad de un usuario
def obtener_rentas_del_usuario(cliente_id):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM rentas LEFT JOIN propiedades ON rentas.propiedad_id = propiedades.ID WHERE cliente_id = {}".format(cliente_id))
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

#Obtener una sola renta del usuario
def obtener_renta_del_usuario(renta_id):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT * FROM rentas LEFT JOIN propiedades ON rentas.propiedad_id = propiedades.ID WHERE renta_id = {}".format(renta_id))
        rows = c.fetchall()
        conn.close()
        return rows
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

#Crear el diccionario de las rentas junto con propiedad
def crea_dict_rentas(cliente_id, rows=None):
    if rows is None:
        rentas = obtener_rentas_del_usuario(cliente_id)
    else:
        rentas = rows
    dict_rentas = {}
    for renta in rentas:
        casa = {
            "ID_renta": renta[0],
            "Huespedes": renta[1],
            "Llegada": renta[2],
            "Salida": renta[3],
            "ID_Cliente": renta[4],
            "ID_propiedad": renta[5],
            "ID": renta[6],
            "ID_dueno": renta[7],
            "Titulo" : renta[8],
            "Descripcion": renta[9],
            "Categoria" : renta[10],
            "Precio" : renta[11],
            "Metros2" : renta[12],
            "Direccion" : renta[13],
            "NoHabitaciones" : renta[14],
            "NoSalas" : renta[15],
            "NoBanios" : renta[16],
            "NoPersonas" : renta[17],
            "ZonaEstado" : renta[18],
            "Antiguedad" : renta[19],
            "Estado" : renta[20],
            "Amueblada" : renta[21],
            "Cochera" : renta[22],
            "WIFI" : renta[23],
            "Television" : renta[24],
            "Refrigeradora" : renta[25],
            "Banos" : "Si" if renta[16] != 0 else "No",
            "Fotos" : renta[26],
            "Fecha" : renta[28]
        }
        dict_rentas[renta[0]] = casa
    return dict_rentas

#Obtener el diccionario de rentas
def obtener_dict_rentas(cliente_id):
    return crea_dict_rentas(cliente_id)




def crear_conexion():
    return crear_conexion_local()

if __name__ == "__main__":
    print("Este archivo no se ejecuta")