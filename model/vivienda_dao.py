from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS viviendas(
        id_vivienda INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100),
        informacion VARCHAR(100),
        precio INTEGER,
        valoracion INTEGER
    )'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creó la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya estaba creada'
        messagebox.showwarning(titulo, mensaje)

def actualizar_tabla():
    conexion = ConexionDB()
    try:
        conexion.cursor.execute("ALTER TABLE viviendas ADD COLUMN valoracion INTEGER")
        conexion.cerrar()
    except:
        pass  # Si la columna ya existe, simplemente la ignoramos

        

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE viviendas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla se borró con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)


class Vivienda:
    def __init__(self, nombre, informacion, precio, valoracion=None):
        self.id_vivienda = None
        self.nombre = nombre
        self.informacion = informacion
        self.precio = precio
        self.valoracion = valoracion
    
    def __str__(self):
        return f'Vivienda[{self.nombre}, {self.informacion}, {self.precio}, {self.valoracion}]'


def guardar(vivienda):
    conexion = ConexionDB()

    sql = f"""INSERT INTO viviendas (nombre, informacion, precio, valoracion)
              VALUES ('{vivienda.nombre}', '{vivienda.informacion}', '{vivienda.precio}', '{vivienda.valoracion}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        titulo = 'Conexión al Registro'
        mensaje = f'Error al guardar la vivienda: {str(e)}'
        messagebox.showerror(titulo, mensaje)

def editar(vivienda, id_vivienda):
    conexion = ConexionDB()

    sql = f"""UPDATE viviendas
              SET nombre = '{vivienda.nombre}', informacion = '{vivienda.informacion}',
                  precio = '{vivienda.precio}', valoracion = '{vivienda.valoracion}'
              WHERE id_vivienda = {id_vivienda}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        titulo = 'Edición de datos'
        mensaje = f'Error al editar la vivienda: {str(e)}'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()

    lista_viviendas = []
    sql = 'SELECT * FROM viviendas'

    try:
        conexion.cursor.execute(sql)
        lista_viviendas = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as e:
        titulo = 'Conexión al Registro'
        mensaje = f'Error al listar las viviendas: {str(e)}'
        messagebox.showwarning(titulo, mensaje)

    return lista_viviendas



def eliminar(id_vivienda):
    conexion = ConexionDB()

    sql = f'DELETE FROM viviendas WHERE id_vivienda = {id_vivienda}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo= 'Eliminar datos'
        mensaje = 'No se ha podido eliminar el registro'
        messagebox.showerror(titulo,mensaje)

