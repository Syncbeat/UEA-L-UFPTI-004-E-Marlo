import mariadb
import sys

def obtener_conexion():
    try:
        conn = mariadb.connect(
            user="root",
            password="662607015",
            host="127.0.0.1",
            port=3306,
            database="funciones_CRUD"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error conectando a MariaDB: {e}")
        sys.exit(1)