import tkinter as tk
from tkinter import ttk, messagebox
from model.vivienda_dao import listar, editar, Vivienda
from PIL import Image, ImageTk

class ValorarViviendas(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        
        self.campos_valorar()

    def campos_valorar(self):
        # Configuración de grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        # Label de seleccionar vivienda
        self.label_seleccionar = tk.Label(self, text='Seleccionar Vivienda:')
        self.label_seleccionar.config(font=('Arial', 12, 'bold'))
        self.label_seleccionar.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        # ComboBox de viviendas
        self.viviendas = listar()
        self.vivienda_nombres = [vivienda[1] for vivienda in self.viviendas]
        self.vivienda_seleccionada = tk.StringVar()
        self.combo_viviendas = ttk.Combobox(self, textvariable=self.vivienda_seleccionada, values=self.vivienda_nombres)
        self.combo_viviendas.config(width=50, font=('Arial', 12))
        self.combo_viviendas.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        # Label de valorar
        self.label_valorar = tk.Label(self, text='Valoración (1-5):')
        self.label_valorar.config(font=('Arial', 12, 'bold'))
        self.label_valorar.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        # Entry de valoración
        self.valoracion = tk.IntVar()
        self.entry_valoracion = tk.Entry(self, textvariable=self.valoracion)
        self.entry_valoracion.config(width=50, font=('Arial', 12))
        self.entry_valoracion.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        # Boton Valorar
        self.boton_valorar = tk.Button(self, text="Valorar", command=self.valorar_vivienda)
        self.boton_valorar.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='#DAD5D6', bg='#158645',
                                  cursor='hand2', activebackground='#35DB6F')
        self.boton_valorar.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        # Contenedor para la imagen
        container = tk.Frame(self, bg="white", highlightbackground="gray", highlightcolor="gray", highlightthickness=1, bd=0)
        container.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Agregar imagen
        imagen = Image.open("img/Valoraciones.webp")
        imagen = imagen.resize((300, 300))
        imagen = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(container, image=imagen, bg="white")
        label_imagen.image = imagen  # Conservar una referencia a la imagen para evitar que sea recolectada por el recolector de basura
        label_imagen.pack(padx=10, pady=10)
        # Estilos visuales
        container.config(borderwidth=5, relief="groove", padx=5, pady=5)

    def valorar_vivienda(self):
        try:
            nombre_vivienda = self.vivienda_seleccionada.get()
            valoracion = self.valoracion.get()
            if not (1 <= valoracion <= 5):
                raise ValueError("La valoración debe estar entre 1 y 5")

            for vivienda in self.viviendas:
                if vivienda[1] == nombre_vivienda:
                    vivienda_a_valorar = Vivienda(vivienda[1], vivienda[2], vivienda[3])
                    vivienda_a_valorar.valoracion = valoracion  # Suponiendo que la clase Vivienda tiene este atributo
                    editar(vivienda_a_valorar, vivienda[0])
                    break

            messagebox.showinfo("Valoración", "Valoración guardada exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "No se ha podido valorar la vivienda")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x200")  # Ajusta la ventana a un tamaño adecuado
    app = ValorarViviendas(root=root)
    app.mainloop()
