import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
from datetime import datetime
from PIL import Image, ImageTk
import pandas as pd
from tkinter import filedialog

from alumnos import Alumnos

class AplicacionCRUD:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Alumnos")
        self.ventana.iconbitmap("img/student.ico")
        self.ventana.configure(bg="lightblue")

        self.modo_oscuro = False  

        self.imagen_modo_oscuro = Image.open("img/modo-oscuro.png")  
        self.imagen_redimensionada = self.imagen_modo_oscuro.resize((22, 22))
        self.imagen_modo_oscuro = ImageTk.PhotoImage(self.imagen_redimensionada)

        self.boton_modo_oscuro = ttk.Button(ventana, image=self.imagen_modo_oscuro, command=self.cambiar_modo)
        self.boton_modo_oscuro.pack()
		
        self.logo = Image.open("img/logo1.png")
        fondo = Image.new("RGBA", self.logo.size, (255, 255, 255, 0))
        fondo.paste(self.logo, (0, 0), self.logo)
        self.logo = ImageTk.PhotoImage(fondo)

        self.label_logo = tk.Label(ventana, image=self.logo, bg="lightblue")
        self.label_logo.pack()

        self.label_bienvenidos = ttk.Label(ventana, text="Bienvenidos a la aplicación", style="Titulo.TLabel")
        self.label_bienvenidos.pack()

        estilo = ttk.Style()
        estilo.configure("Label.TLabel", background="lightblue", foreground="black", font=("Arial", 11))
        estilo.configure('Fondo.TFrame', background='lightblue')
        estilo.configure("TButton",
        background="green",
        foreground="green",
        font=("Arial", 12),
        borderwidth=2,
        relief="flat",
        cursor="hand2")
        estilo.configure("BoldLabel.TLabel", background="lightblue", font=("Arial", 11, "bold"))
        estilo.configure("Titulo.TLabel", background="lightblue", font=("Arial", 14, "bold"))

        self.marco_alta = ttk.Frame(ventana, style='Fondo.TFrame')

        self.barra_menu = tk.Menu(ventana)
        ventana.config(menu=self.barra_menu)

        menu_alumnos = tk.Menu(self.barra_menu, tearoff=0)
        menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Menú", menu=menu_alumnos)
        self.barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

        menu_alumnos.add_command(label="Cargar alumno", command=self.mostrar_formulario_alta)
        menu_alumnos.add_command(label="Buscar alumno", command=self.buscar_alumno_por_legajo)
        menu_alumnos.add_command(label="Modificar alumno", command=self.mostrar_formulario_modificar)
        menu_alumnos.add_command(label="Listado alumnos", command=self.mostrar_listado_alumnos)
        menu_alumnos.add_command(label="Eliminar alumno", command=self.mostrar_formulario_eliminar)
        menu_ayuda.add_command(label="Instrucciones", command=self.mostrar_ayuda)

        self.alumno1 = Alumnos()


    def cambiar_modo(self):

        if self.modo_oscuro:
            self.ventana.configure(bg="lightblue")
            self.label_logo.configure(bg="lightblue")
            estilo = ttk.Style()
            estilo.configure('Fondo.TFrame', background='lightblue')
            estilo.configure("Label.TLabel", background="lightblue", foreground="black", font=("Arial", 11))
            estilo.configure("BoldLabel.TLabel", background="lightblue", foreground="black", font=("Arial", 11, "bold"))
            estilo.configure("Titulo.TLabel", background="lightblue", foreground="black", font=("Arial", 14, "bold"))

            self.imagen_modo_oscuro = Image.open("img/modo-oscuro.png") 
            self.imagen_redimensionada = self.imagen_modo_oscuro.resize((22, 22))
            self.imagen_modo_oscuro = ImageTk.PhotoImage(self.imagen_redimensionada)
            self.boton_modo_oscuro["image"] = self.imagen_modo_oscuro
        else:
            self.ventana.configure(bg="#313d47")
            self.label_logo.configure(bg="#313d47")
            estilo = ttk.Style()
            estilo.configure('Fondo.TFrame', background='#313d47')
            estilo.configure("Label.TLabel", background="#313d47", foreground="white", font=("Arial", 11))
            estilo.configure("BoldLabel.TLabel", background="#313d47", foreground="white", font=("Arial", 11, "bold"))
            estilo.configure("Titulo.TLabel", background="#313d47", foreground="white", font=("Arial", 14, "bold"))

            self.imagen_modo_claro = Image.open("img/modo-claro.png") 
            self.imagen_redimensionada = self.imagen_modo_claro.resize((22, 22))
            self.imagen_modo_claro = ImageTk.PhotoImage(self.imagen_redimensionada)
            self.boton_modo_oscuro["image"] = self.imagen_modo_claro


        self.modo_oscuro = not self.modo_oscuro

    def mostrar_ayuda(self):

        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        self.label_bienvenidos.pack_forget()

        instrucciones = """         ▶ Alta alumno:
            1- Presionar del menú desplegable la opción "Cargar Alumno"
            2- Completar los campos Nombre, Fecha de Nacimiento y Dirección
            3- Presionar el botón [Confirmar]
            4- Se visualiza un cartel en modo de confirmación indicando que los datos fueron cargados

        ▶ Consulta por legajo:
            1- Presionar del menú desplegable la opción "Consulta por legajo"
            2- Completar el campo legajo
            3- Presionar el botón [Consultar]
            4- Se visualiza como se autocompletan todos los campos con la información del alumno

        ▶ Listado de alumnos:
            1- Presionar del menú desplegable la opción "Listado de alumnos"
            2- Presionar el botón [Listado alumnos]
            3- Se visualiza un listado de los alumnos con sus respectivos datos
            4- Haz clic en el botón [Exportar a Excel]
            5- Selecciona la ubicación donde deseas guardar el archivo y presiona el botón [Guardar]
            6- El sistema generará un archivo Excel con todos los datos de los alumnos 

        ▶ Eliminar alumno:
            1- Presionar del menú desplegable la opción "Eliminar alumno"
            2- Completar el campo legajo
            3- Presionar el botón [Borrar]
            4- Se visualiza un cartel en modo de confirmación indicando que se eliminó el alumno

        ▶ Modificar alumno:
            1- Presionar del menú desplegable la opción "Modificar alumno"
            2- Completar el campo legajo
            3- Presionar el botón [Consultar]
            4- Se visualiza como se autocompletan todos los campos con la información del alumno
            5- Modificar uno o mas campos
            6- Presionar el botón [Modificar]
            7- Se visualiza un cartel en modo de confirmación indicando que se modificó el alumno
        """

        etiqueta_instrucciones = ttk.Label(self.marco_alta, text=instrucciones, wraplength=1500, justify="left", style="Label.TLabel")
        etiqueta_instrucciones.grid(row=0, column=0, padx=0, pady=1)

        self.marco_alta.pack()


    def mostrar_formulario_alta(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        self.label_bienvenidos.pack_forget()

        label_titulo = ttk.Label(self.marco_alta, text="Cargar alumno", style="BoldLabel.TLabel", justify="center")

        label_nombre = ttk.Label(self.marco_alta, text="Nombre:", style="Label.TLabel")
        label_fecha = ttk.Label(self.marco_alta, text="Fecha de Nacimiento:", style="Label.TLabel")
        label_direccion = ttk.Label(self.marco_alta, text="Dirección:", style="Label.TLabel")

        entry_nombre = ttk.Entry(self.marco_alta)
        entry_fecha = DateEntry(self.marco_alta, date_pattern="dd/mm/yyyy", maxdate=datetime.today().date())
        entry_direccion = ttk.Entry(self.marco_alta)

        label_titulo.grid(row=0, columnspan=3,column=0, padx=5, pady=5)
        label_nombre.grid(row=1, column=0, padx=5, pady=5)
        label_fecha.grid(row=2, column=0, padx=5, pady=5)
        label_direccion.grid(row=3, column=0, padx=5, pady=5)

        entry_nombre.grid(row=1, column=1, padx=5, pady=5)
        entry_fecha.grid(row=2, column=1, padx=5, pady=5)
        entry_direccion.grid(row=3, column=1, padx=5, pady=5)

        boton_guardar = tk.Button(self.marco_alta, text="Guardar", bg="lightgreen",command=lambda: self.guardar_alumno(entry_nombre.get(), entry_fecha.get(), entry_direccion.get()))
        boton_guardar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        entry_nombre.delete(0, 'end')
        entry_fecha.delete(0, 'end')
        entry_direccion.delete(0, 'end')

        self.marco_alta.pack()

    def guardar_alumno(self, nombre, fecha, direccion):

        if nombre and fecha and direccion:
            datos = (nombre, fecha, direccion)
            resultado = self.alumno1.alta(datos)
            mb.showinfo(title= "Confirmación", message=f"Se ha dado de alta al alumno/a: {nombre}")

            self.actualizar_tabla()
        else:
            mb.showerror("Error", "Por favor, complete todos los campos.")

    def actualizar_tabla(self):

        registros = self.alumno1.recuperar_todos()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for alumno in registros:
            self.tree.insert("", 0, values=(alumno[0], alumno[1], alumno[2], alumno[3]))


    def buscar_alumno_por_legajo(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        self.label_bienvenidos.pack_forget()

        label_titulo = ttk.Label(self.marco_alta, text="Buscar alumno", style="BoldLabel.TLabel", justify="center")

        label_legajo = ttk.Label(self.marco_alta, text="Legajo del alumno:", style="Label.TLabel")
        entry_legajo = ttk.Entry(self.marco_alta)

        label_titulo.grid(row=0, columnspan=3, column=0, padx=5, pady=5)
        label_legajo.grid(row=1, column=0, padx=5, pady=5)
        entry_legajo.grid(row=1, column=1, padx=5, pady=5)

        def buscar_datos():
            legajo = entry_legajo.get()
            datos_alumno = self.alumno1.consulta((legajo,))
            if datos_alumno:
                nombre, fecha_nacimiento, direccion = datos_alumno[0]

                label_nombre = ttk.Label(self.marco_alta, text="Nombre:", style="Label.TLabel")
                entry_nombre = ttk.Entry(self.marco_alta)
                label_fecha = ttk.Label(self.marco_alta, text="Fecha de Nacimiento:", style="Label.TLabel")
                entry_fecha = ttk.Entry(self.marco_alta)
                label_direccion = ttk.Label(self.marco_alta, text="Dirección:", style="Label.TLabel")
                entry_direccion = ttk.Entry(self.marco_alta)

                label_nombre.grid(row=2, column=0, padx=5, pady=5)
                entry_nombre.grid(row=2, column=1, padx=5, pady=5)
                label_fecha.grid(row=3, column=0, padx=5, pady=5)
                entry_fecha.grid(row=3, column=1, padx=5, pady=5)
                label_direccion.grid(row=4, column=0, padx=5, pady=5)
                entry_direccion.grid(row=4, column=1, padx=5, pady=5)

                entry_nombre.insert(0, nombre)
                entry_fecha.insert(0, fecha_nacimiento)
                entry_direccion.insert(0, direccion)

                # Deshabilitar los campos
                entry_nombre.configure(state="readonly")
                entry_fecha.configure(state="readonly")
                entry_direccion.configure(state="readonly")
            else:
                mb.showerror("Error", "No se encontró al alumno con el legajo proporcionado.")

        boton_buscar = tk.Button(self.marco_alta, text="Consultar", command=buscar_datos, bg="lightgreen")
        boton_buscar.grid(row=1, column=2, padx=5, pady=5)

        self.marco_alta.pack()



    def mostrar_formulario_modificar(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        self.label_bienvenidos.pack_forget()

        label_titulo = ttk.Label(self.marco_alta, text="Modificar alumno", style="BoldLabel.TLabel", justify="center")

        label_legajo = ttk.Label(self.marco_alta, text="Legajo del alumno:", style="Label.TLabel")
        entry_legajo = ttk.Entry(self.marco_alta)
        label_titulo.grid(row=0, columnspan=3, column=0, padx=5, pady=5)
        label_legajo.grid(row=1, column=0, padx=5, pady=5)
        entry_legajo.grid(row=1, column=1, padx=5, pady=5)

        def cargar_datos():
            legajo = entry_legajo.get()
            datos_alumno = self.alumno1.consulta((legajo,))
            if datos_alumno:

                nombre, fecha_nacimiento, direccion = datos_alumno[0]
                
                label_nombre = ttk.Label(self.marco_alta, text="Nombre:", style="Label.TLabel")
                entry_nombre = ttk.Entry(self.marco_alta)
                label_fecha = ttk.Label(self.marco_alta, text="Fecha de Nacimiento:", style="Label.TLabel")
                entry_fecha = ttk.Entry(self.marco_alta)
                label_direccion = ttk.Label(self.marco_alta, text="Dirección:", style="Label.TLabel")
                entry_direccion = ttk.Entry(self.marco_alta)

                label_nombre.grid(row=2, column=0, padx=5, pady=5)
                entry_nombre.grid(row=2, column=1, padx=5, pady=5)
                label_fecha.grid(row=3, column=0, padx=5, pady=5)
                entry_fecha.grid(row=3, column=1, padx=5, pady=5)
                label_direccion.grid(row=4, column=0, padx=5, pady=5)
                entry_direccion.grid(row=4, column=1, padx=5, pady=5)

                entry_nombre.insert(0, nombre)
                entry_fecha.insert(0, fecha_nacimiento)
                entry_direccion.insert(0, direccion)

                def guardar_cambios():
                    nombre = entry_nombre.get()
                    fecha_nacimiento = entry_fecha.get()
                    direccion = entry_direccion.get()

                    if nombre and fecha_nacimiento and direccion:
                        datos_modificados = (nombre, fecha_nacimiento, direccion, legajo)
                        resultado = self.alumno1.modificacion(datos_modificados)
                        mb.showinfo(title= "Confirmación", message=f"Se ha actualizado la información del alumno/a: {nombre}")

                        self.actualizar_tabla()
                        self.marco_alta.destroy()
                    else:
                        mb.showerror("Error", "Por favor, complete todos los campos.")

                boton_guardar = tk.Button(self.marco_alta, text="Guardar Cambios", command=guardar_cambios, bg="lightgreen")
                boton_guardar.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
            else:
                mb.showerror("Error", "No se encontró al alumno con el legajo proporcionado.")

        boton_buscar = tk.Button(self.marco_alta, text="Buscar Alumno", command=cargar_datos, bg="lightgreen")
        boton_buscar.grid(row=1, column=2, padx=5, pady=5)

        self.marco_alta.pack()

    def mostrar_formulario_eliminar(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        self.label_bienvenidos.pack_forget()

        label_titulo = ttk.Label(self.marco_alta, text="Eliminar alumno", style="BoldLabel.TLabel", justify="center")

        label_legajo = ttk.Label(self.marco_alta, text="Legajo del alumno:", style="Label.TLabel")
        entry_legajo = ttk.Entry(self.marco_alta)
        label_titulo.grid(row=0, columnspan=3,column=0, padx=5, pady=5)
        label_legajo.grid(row=1, column=0, padx=5, pady=5)
        entry_legajo.grid(row=1, column=1, padx=5, pady=5)

        def eliminar_alumno():
            legajo = entry_legajo.get()
            if legajo:
                resultado = self.alumno1.baja((legajo,))
                if resultado > 0:
                    mb.showinfo("Resultado", f"Alumno con legajo {legajo} ha sido eliminado exitosamente.")
                    self.actualizar_tabla()
                    self.marco_alta.destroy()
                else:
                    mb.showerror("Error", "No se encontró al alumno con el legajo proporcionado.")
            else:
                mb.showerror("Error", "Por favor, ingrese el legajo del alumno a eliminar.")

        boton_eliminar = tk.Button(self.marco_alta, text="Eliminar Alumno", command=eliminar_alumno, bg="lightgreen")
        boton_eliminar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.marco_alta.pack()

    def mostrar_listado_alumnos(self):
        for widget in self.marco_alta.winfo_children():
            widget.destroy()

        self.label_bienvenidos.pack_forget()

        label_titulo = ttk.Label(self.marco_alta, text="Listado de alumnos", style="BoldLabel.TLabel", justify="center")

        self.tree = ttk.Treeview(self.marco_alta, columns=("#", "Legajo", "Nombre", "Fecha Nacimiento", "Dirección"))

        columnas = [
            ("#", 40),
            ("Legajo", 80),
            ("Nombre", 200),
            ("Fecha Nacimiento", 200),
            ("Dirección", 200)
        ]

        for i, (col_name, col_width) in enumerate(columnas):
            self.tree.heading("#{}".format(i), text=col_name, anchor="center")
            self.tree.column("#{}".format(i), width=col_width, anchor="center")

        y_scrollbar = ttk.Scrollbar(self.marco_alta, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=y_scrollbar.set)

        label_titulo.grid(row=0, columnspan=3, column=0, padx=5, pady=5)
        self.tree.grid(row=1, column=0, padx=5, pady=5)

        y_scrollbar.grid(row=1, column=len(columnas), sticky="ns")

        self.actualizar_tabla()

        self.marco_alta.pack()

        boton_exportar_excel = tk.Button(self.marco_alta, text="Exportar a Excel",bg="lightgreen",command=self.exportar_a_excel)
        boton_exportar_excel.grid(row=3, column=0, padx=5, pady=5)

    def exportar_a_excel(self):
            registros = self.alumno1.recuperar_todos()
            if registros:
                df = pd.DataFrame(registros, columns=["Legajo", "Nombre", "Fecha Nacimiento", "Dirección"])

                file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])

                if file_path:
                    df.to_excel(file_path, index=False)
                    mb.showinfo("Exportado", "Los datos fueron exportados a Excel con éxito.")
                else:
                    mb.showinfo("Operación cancelada", "La exportación a Excel fue cancelada.")
            else:
                mb.showinfo("Sin datos", "No hay datos para exportar.")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionCRUD(ventana)
    ventana.mainloop()
