import tkinter as tk
from tkinter import ttk
from model.vivienda_dao import listar

class EstadisticasViviendas(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        # Obtener datos de viviendas
        viviendas = listar()

        # Número total de viviendas
        num_total_viviendas = len(viviendas)

        # Calcular estadísticas
        precios = [int(v[3].replace('€', '').replace('.', '')) for v in viviendas if v[3]]
        valoraciones = [int(v[4]) for v in viviendas if v[4] is not None and v[4] != 'None']
        precio_promedio = sum(precios) / len(precios) if precios else 0
        valoracion_promedio = sum(valoraciones) / len(valoraciones) if valoraciones else 0

        # Mostrar estadísticas en etiquetas
        tk.Label(self, text="Estadísticas de Viviendas", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self, text=f"Número total de viviendas: {num_total_viviendas}").pack()
        tk.Label(self, text=f"Precio Promedio: €{precio_promedio:.2f}").pack()
        tk.Label(self, text=f"Valoración Promedio: {valoracion_promedio:.2f}").pack()

        # Crear tabla con distribución de precios
        tabla_precios = ttk.Treeview(self, columns=("Precio", "Cantidad"))
        tabla_precios.heading("#0", text="Rango de Precio")
        tabla_precios.heading("#1", text="Cantidad")
        tabla_precios.pack(pady=10)
        
        # Calcular y mostrar distribución de precios
        precio_range_counts = self.calcular_distribucion(precios, [350, 500, 750, 1000, 1250, 1500, 1750, 2000, float('inf')])
        for rango, cantidad in precio_range_counts.items():
            tabla_precios.insert("", "end", text=rango, values=(cantidad,))

        # Crear tabla con distribución de valoraciones
        tabla_valoraciones = ttk.Treeview(self, columns=("Valoración", "Cantidad"))
        tabla_valoraciones.heading("#0", text="Valoración")
        tabla_valoraciones.heading("#1", text="Cantidad")
        tabla_valoraciones.pack(pady=10)
        
        # Calcular y mostrar distribución de valoraciones
        valoracion_counts = {i: valoraciones.count(i) for i in range(1, 6)}
        for valoracion, cantidad in valoracion_counts.items():
            tabla_valoraciones.insert("", "end", text=valoracion, values=(cantidad,))

    def calcular_distribucion(self, data, bins):
        range_counts = {f"{bins[i]} - {bins[i+1]}": 0 for i in range(len(bins)-1)}
        for d in data:
            for i in range(len(bins)-1):
                if bins[i] <= d <= bins[i+1]:
                    range_counts[f"{bins[i]} - {bins[i+1]}"] += 1
        return range_counts

if __name__ == '__main__':
    root = tk.Tk()
    app = EstadisticasViviendas(root)
    app.mainloop()
