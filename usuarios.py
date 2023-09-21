import re
from mysql.connector import Error
from controlador_base_datos import crear_conexion_local

def verifica_login(correo,password):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT email, password FROM usuarios WHERE email = '{}' AND password = '{}'".format(correo,password))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def verifica_registro(nombre,telefono,email,password):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("INSERT INTO usuarios (nombre,telefono,email,password) VALUES ('{}','{}','{}','{}')".format(nombre,telefono,email,password))
        conn.commit()
        conn.close()
        return True
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    
def verifica_correo(entrada):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT email FROM usuarios WHERE email = '{}'".format(entrada))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    

def validar_correo(correo):
    # Definir la expresión regular para validar el formato de un correo electrónico
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Realizar la validación utilizando la expresión regular y el método search de re
    resultado = re.search(patron, correo)
    # Devolver True si el correo electrónico es válido, False en caso contrario
    return resultado is not None

def verifica_telefono(entrada):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT telefono FROM usuarios WHERE telefono = '{}'".format(entrada))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def validar_telefono(telefono):
    patron = r'^\+?1?\d{9,15}$'
    resultado = re.match(patron, telefono)
    if resultado:
        return True
    else:
        return False

def crear_conexion():
    return crear_conexion_local()

if __name__ == "__main__":
    print("Este archivo no se ejecuta")