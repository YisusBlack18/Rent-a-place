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




def crear_conexion():
    return crear_conexion_local()

if __name__ == "__main__":
    print("Este archivo no se ejecuta")