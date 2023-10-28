import sqlite3

conexion = sqlite3.connect("bd_alumnos")

cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        fecha_nacimiento TEXT,
        direccion TEXT
    )
''')

conexion.commit()
conexion.close()
