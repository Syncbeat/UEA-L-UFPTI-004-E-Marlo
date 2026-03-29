from conexion.conexion import obtener_conexion

class ProductoService:
    @staticmethod
    def listar_todos():
        db = obtener_conexion()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        res = cursor.fetchall()
        db.close()
        return res

    @staticmethod
    def insertar(nombre, precio, stock):
        db = obtener_conexion()
        cursor = db.cursor()
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, precio, stock))
        db.commit()
        db.close()

    @staticmethod
    def eliminar(id_producto):
        db = obtener_conexion()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        db.commit()
        db.close()