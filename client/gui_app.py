import tkinter as tk
from tkinter import ttk,messagebox
from model.vivienda_dao import crear_tabla, borrar_tabla
from model.vivienda_dao import Vivienda, guardar, listar,editar,eliminar


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width= 300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label ='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label = 'Crear Registro en DB', command=crear_tabla)
    menu_inicio.add_command(label = 'Eliminar Registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label = 'Salir', command = root.destroy)





class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()
        #self.config( bg='green')
        self.id_vivienda = None

        self.campos_vivienda()
        self.deshabilitar_campos()
        self.tabla_viviendas()
        

    def campos_vivienda(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text = 'Nombre: ')
        self.label_nombre.config(font = ('Arial',12, 'bold'))
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.label_info = tk.Label(self, text = 'Información: ')
        self.label_info.config(font = ('Arial',12, 'bold'))
        self.label_info.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.label_precio = tk.Label(self, text = 'Precio: ')
        self.label_precio.config(font = ('Arial',12, 'bold'))
        self.label_precio.grid(row = 2, column = 0,padx = 10, pady = 10)

        #Entrys de cada campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width = 50, font = ('Arial',12))
        self.entry_nombre.grid(row = 0, column = 1,padx = 10, pady = 10,columnspan = 2)

        self.mi_info = tk.StringVar()
        self.entry_info = tk.Entry(self,textvariable=self.mi_info)
        self.entry_info.config(width = 50, font = ('Arial',12))
        self.entry_info.grid(row = 1, column = 1,padx = 10, pady = 10,columnspan = 2)

        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self,textvariable=self.mi_precio)
        self.entry_precio.config(width = 50, font = ('Arial',12))
        self.entry_precio.grid(row = 2, column = 1,padx = 10, pady = 10,columnspan = 2)

        #Boton Nuevo
        self.boton_nuevo = tk.Button(self, text="Nuevo", command = self.habilitar_campos)
        self.boton_nuevo.config(width = 20,font = ('Arial',12, 'bold'),
                        fg = '#DAD5D6', bg = '#158645',
                        cursor = 'hand2', activebackground= '#35DB6F')
        self.boton_nuevo.grid(row = 3, column = 0,padx = 10, pady = 10)

        #Boton Guardar
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width = 20,font = ('Arial',12, 'bold'),
                        fg = '#DAD5D6', bg = '#1658A2',
                        cursor = 'hand2', activebackground= '#3586DF')
        self.boton_guardar.grid(row = 3, column = 1,padx = 10, pady = 10)

        #Boton Cancelar
        self.boton_cancelar = tk.Button(self, text="Cancelar", command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20,font = ('Arial',12, 'bold'),
                        fg = '#DAD5D6', bg = '#BD152E',
                        cursor = 'hand2', activebackground= '#E15370')
        self.boton_cancelar.grid(row = 3, column = 2,padx = 10, pady = 10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_info.set('')
        self.mi_precio.set('')


        self.entry_nombre.config(state='normal')
        self.entry_info.config(state='normal')
        self.entry_precio.config(state='normal')
            
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_vivienda = None

        self.mi_nombre.set('')
        self.mi_info.set('')
        self.mi_precio.set('')


        self.entry_nombre.config(state='disabled')
        self.entry_info.config(state='disabled')
        self.entry_precio.config(state='disabled')
            
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):


        vivienda = Vivienda(
            self.mi_nombre.get(),
            self.mi_info.get(),
            self.mi_precio.get(),
        )

        if self.id_vivienda == None:
            guardar(vivienda)
        else:
            editar(vivienda, self.id_vivienda)

            

        self.tabla_viviendas()


        self.deshabilitar_campos()

    
    def tabla_viviendas(self):
        #Recuperar la lista de viviendas
        self.lista_viviendas = listar()
        self.lista_viviendas.reverse()


        self.tabla = ttk.Treeview(self, 
        column = ('Nombre', 'Información', 'Precio'))
        self.tabla.grid(row=4,column= 0, columnspan=4, sticky = 'nse')

            # Ajuste de ancho de columnas
        self.tabla.column('#0', width=50)  # Columna ID
        self.tabla.column('#1', width=150)  # Columna Nombre
        self.tabla.column('#2', width=300)  # Columna Información
        self.tabla.column('#3', width=100)  # Columna Precio


        #Scrollbar para la tabla si excede los 10 registros
        self.scroll = ttk.Scrollbar(self,
        orient= 'vertical', command = self.tabla.yview)
        self.scroll.grid(row = 4, column = 4, sticky = 'nse')
        self.tabla.configure(yscrollcommand = self.scroll.set)



        self.tabla.heading('#0',text= 'ID')
        self.tabla.heading('#1',text= 'NOMBRE')
        self.tabla.heading('#2',text= 'INFORMACIÓN')
        self.tabla.heading('#3',text= 'PRECIO')


        #Iterar la lista de viviendas
        for p in self.lista_viviendas:
            self.tabla.insert('',0, text=p[0], 
            values = (p[1], p[2],p[3]))

        #Boton Editar
        self.boton_editar = tk.Button(self, text="Editar", command = self.editar_datos)
        self.boton_editar.config(width = 20,font = ('Arial',12, 'bold'),
                        fg = '#DAD5D6', bg = '#158645',
                        cursor = 'hand2', activebackground= '#35DB6F')
        self.boton_editar.grid(row = 5, column = 0,padx = 10, pady = 10)

        #Boton Eliminar
        self.boton_eliminar = tk.Button(self, text="Eliminar", command= self.eliminar_datos)
        self.boton_eliminar.config(width = 20,font = ('Arial',12, 'bold'),
                        fg = '#DAD5D6', bg = '#BD152E',
                        cursor = 'hand2', activebackground= '#E15370')
        self.boton_eliminar.grid(row = 5, column = 1,padx = 10, pady = 10)

    def editar_datos(self):
        try:
            self.id_vivienda = self.tabla.item(self.tabla.selection())['text']
            self.nombre_vivienda = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.información_vivienda = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.precio_vivienda = self.tabla.item(
                self.tabla.selection())['values'][2]
            
            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_vivienda)
            self.entry_info.insert(0, self.información_vivienda)
            self.entry_precio.insert(0, self.precio_vivienda)
        except:
            titulo= 'Edicion de datos'
            mensaje = 'No se ha podido editar el registro'
            messagebox.showerror(titulo,mensaje)

    def eliminar_datos(self):
        try:
            self.id_vivienda = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_vivienda)

            self.tabla_viviendas()
            self.id_vivienda = None
        except:
            titulo= 'Eliminar un Registro'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo,mensaje)




