import sqlite3

class Alumnos:

    def abrir(self):
        conexion = sqlite3.connect("bd_alumnos")
        return conexion

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO alumnos(nombre, fecha_nacimiento, direccion) VALUES (?, ?, ?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "SELECT nombre, fecha_nacimiento, direccion FROM alumnos WHERE codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "SELECT codigo, nombre, fecha_nacimiento, direccion FROM alumnos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "DELETE FROM alumnos WHERE codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount  # Retornamos la cantidad de filas borradas
        except:
            cone.close()

    def modificacion(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "UPDATE alumnos SET nombre=?, fecha_nacimiento=?, direccion=? WHERE codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount  # Retornamos la cantidad de filas modificadas
        except:
            cone.close()
