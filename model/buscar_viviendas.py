import tkinter as tk
from tkinter import ttk, messagebox
from model.vivienda_dao import listar

class BuscarViviendas(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.label_precio_min = tk.Label(self, text="Precio mínimo:")
        self.label_precio_min.grid(row=0, column=0, padx=10, pady=10)

        self.precio_min = tk.StringVar()
        self.entry_precio_min = tk.Entry(self, textvariable=self.precio_min)
        self.entry_precio_min.grid(row=0, column=1, padx=10, pady=10)

        self.label_precio_max = tk.Label(self, text="Precio máximo:")
        self.label_precio_max.grid(row=1, column=0, padx=10, pady=10)

        self.precio_max = tk.StringVar()
        self.entry_precio_max = tk.Entry(self, textvariable=self.precio_max)
        self.entry_precio_max.grid(row=1, column=1, padx=10, pady=10)

        self.label_valoracion_min = tk.Label(self, text="Valoración mínima:")
        self.label_valoracion_min.grid(row=2, column=0, padx=10, pady=10)

        self.valoracion_min = tk.StringVar()
        self.entry_valoracion_min = tk.Entry(self, textvariable=self.valoracion_min)
        self.entry_valoracion_min.grid(row=2, column=1, padx=10, pady=10)

        self.boton_buscar = tk.Button(self, text="Buscar", command=self.buscar_viviendas)
        self.boton_buscar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.tabla_resultados = ttk.Treeview(self, columns=("Nombre", "Información", "Precio", "Valoración"))
        self.tabla_resultados.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.tabla_resultados.heading('#0', text="ID")
        self.tabla_resultados.heading('#1', text="Nombre")
        self.tabla_resultados.heading('#2', text="Información")
        self.tabla_resultados.heading('#3', text="Precio")
        self.tabla_resultados.heading('#4', text="Valoración")

        self.tabla_resultados.column("#0", width=60)  # Ancho de la columna "ID"
        self.tabla_resultados.column("#1", width=130)  # Ancho de la columna "Nombre"
        self.tabla_resultados.column("#2", width=340)  # Ancho de la columna "Información"
        self.tabla_resultados.column("#3", width=80)  # Ancho de la columna "Precio"
        self.tabla_resultados.column("#4", width=70)  # Ancho de la columna "Valoración"

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla_resultados.yview)
        self.scroll.grid(row=4, column=2, sticky='nse')
        self.tabla_resultados.configure(yscrollcommand=self.scroll.set)

    def buscar_viviendas(self):  
        try:
            precio_min = self.precio_min.get()
            precio_max = self.precio_max.get()
            valoracion_min = self.valoracion_min.get()
            
            if precio_min:
                precio_min = float(''.join(filter(str.isdigit, precio_min)))
            else:
                precio_min = float('-inf')  
            
            if precio_max:
                precio_max = float(''.join(filter(str.isdigit, precio_max)))
            else:
                precio_max = float('inf')  
            
            if valoracion_min:
                valoracion_min = int(valoracion_min)
            else:
                valoracion_min = 0  
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos para los precios y la valoración.")
            return

        viviendas = listar()

        resultados = []
        for vivienda in viviendas:
            precio = int(''.join(filter(str.isdigit, str(vivienda[3].split()[0]))))
            valoracion = 0
            if vivienda[4] is not None and vivienda[4] != 'None':
                valoracion = int(vivienda[4])
            if precio_min <= precio <= precio_max and valoracion >= valoracion_min:
                resultados.append(vivienda)

        self.actualizar_tabla(resultados)

        if not resultados:
            messagebox.showinfo("Resultados", "No se encontraron viviendas que coincidan con los criterios de búsqueda.")

    def actualizar_tabla(self, viviendas):
        self.tabla_resultados.delete(*self.tabla_resultados.get_children())
        for vivienda in viviendas:
            self.tabla_resultados.insert('', 'end', text=vivienda[0], values=(vivienda[1], vivienda[2], vivienda[3], vivienda[4]))

if __name__ == '__main__':
    root = tk.Tk()
    app = BuscarViviendas(root=root)
    app.mainloop()
