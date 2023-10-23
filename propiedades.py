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

def crea_dict_propiedades(rows=None):
    if rows is None:
        propiedades = obtener_propiedades()
    else:
        propiedades = rows
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

def filtrar_propiedades(zona,precio,fecha,numHabitaciones,buscar):
    resultados={}
    try:
        conn = crear_conexion()
        c = conn.cursor()
        # Construir la consulta SQL base
        query = "SELECT * FROM propiedades WHERE 1"
        # Agregar condiciones según los argumentos proporcionados
        if zona != "zona":
            query += " AND ZonaEstado = '{}'".format(zona)
        if precio != None:
            precio2=int(precio - 10000)
            query += " AND Precio BETWEEN {} AND {}".format(precio2,precio)
        if fecha != None and fecha != 'fechas':
            query += " AND FechaCreacion = '{}'".format(fecha)
        if numHabitaciones != "numHabitaciones":
            if numHabitaciones == "5":
                query += " AND NoHabitaciones >= 5"
            else:
                query += " AND NoHabitaciones = {}".format(numHabitaciones)
        if buscar != None:
            query += " AND (Titulo LIKE '%{}%' OR Categoria LIKE '%{}%')".format(buscar,buscar)
        # Ejecutar la consulta
        c.execute(query)
        rows = c.fetchall()
        conn.close()
        # Crear un diccionario con los valores obtenidos
        resultados = crea_dict_propiedades(rows)
        return resultados
    except Error as err:
        print("Algo salió mal: {}".format(err))
        return resultados


def obtener_valores_base():
    try:
        dict_valores = {}
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT DISTINCT ZonaEstado FROM propiedades")
        rows = c.fetchall()
        agrega_dict_valores(dict_valores,'zonas',rows)
        c.execute("SELECT DISTINCT FechaCreacion FROM propiedades")
        rows = c.fetchall()
        agrega_dict_valores(dict_valores,'fechas',rows)
        c.execute("SELECT DISTINCT Categoria FROM propiedades")
        agrega_dict_valores(dict_valores,'categorias',rows)
        conn.close()
        return dict_valores
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def agrega_dict_valores(dicc,id,rows):
    dicc[id] = []
    for row in rows:
        dicc[id].append(row[0])
    return dicc


if __name__ == '__main__':
    print("Este archivo no se ejecuta")