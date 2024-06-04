import os
import tkinter as tk
from tkinter import ttk
from client.gui_app import Frame, barra_menu
from model.valorar_viviendas import ValorarViviendas
from model.buscar_viviendas import BuscarViviendas
from model.vivienda_dao import actualizar_tabla
from model.stats import EstadisticasViviendas  # Importamos la pestaña de estadísticas


def main():
    root = tk.Tk()
    root.title('RRHome')

    # Obtén la ruta absoluta del directorio del script
    base_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_path, 'img', 'RRH.ico')
    root.iconbitmap(icon_path)

    root.geometry("800x600")
    root.resizable(0, 0)
    barra_menu(root)

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand='yes')

    app_frame = Frame(notebook)
    valorar_frame = ValorarViviendas(notebook)
    buscar_frame = BuscarViviendas(notebook)
    estadisticas_frame = EstadisticasViviendas(notebook)  # Agregamos la pestaña de estadísticas

    notebook.add(app_frame, text="Viviendas")
    notebook.add(valorar_frame, text="Valorar Viviendas")
    notebook.add(buscar_frame, text="Buscar Viviendas")
    notebook.add(estadisticas_frame, text="Estadísticas")  # Añadimos la pestaña de estadísticas

    actualizar_tabla()  # Asegúrate de actualizar la tabla

    root.mainloop()

if __name__ == '__main__':
    main()
