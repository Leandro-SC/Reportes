import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Declarar constantes
server = os.getenv("SERVER")
bd = os.getenv("BD")
usuario = os.getenv("USUARIO")
contrasena = os.getenv("PASSWORD")


def establecerConexion():
    try:
        # Establecer la conexión
        conexion = mysql.connector.connect(
            user=usuario, password=contrasena, host=server, database=bd
        )
        print("Conexión exitosa")
        return conexion
    except mysql.connector.Error as error:
        print("Error al establecer la conexión a la base de datos:", error)
        return None


def ejecutarConsulta(conexion, query):
    try:
        cursor = conexion.cursor()
        cursor.execute(query)
        consulta = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)
        print(consulta)
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta:", error)


def conectarBaseComercial(query):
    conexion = establecerConexion()
    if conexion:
        ejecutarConsulta(conexion, query)


def unirTablas(*args):
    arr_tablas = []
    for tabla in args:
        arr_tablas.append(tabla)
    
    return pd.concat(arr_tablas)


query_nomina = "SELECT * FROM nomina_abonado"
conectarBaseComercial(query_nomina)
