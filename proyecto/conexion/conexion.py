import mariadb
import sys

def obtener_conexion():
    try:
        conn = mariadb.connect(
            user="root",
            password="TU_CONTRASEÑA", # La que pusiste en el paso anterior
            host="127.0.0.1",
            port=3306,
            database="tu_base_de_datos"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error: {e}")
        return None