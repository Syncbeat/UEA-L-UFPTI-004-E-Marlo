import mariadb
import sys

def obtener_conexion():
    try:
        conexion = mariadb.connect(
            user="root",
            password="662607015",
            host="localhost",
            port=3306,
            database="login_web"
        )
        return conexion
    except mariadb.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        sys.exit(1)