import os
import sqlite3

class ConexionDB:
    def __init__(self):
        # Obtener la ruta del directorio del archivo actual
        base_path = os.path.dirname(os.path.abspath(__file__))
        # Construir la ruta completa al archivo de la base de datos
        db_path = os.path.join(base_path, '..', 'database', 'RRHome.db')
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
