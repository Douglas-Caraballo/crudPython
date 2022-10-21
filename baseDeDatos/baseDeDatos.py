import sqlite3
from tkinter import messagebox
from tkinter import *
class BaseDeDatosCrud():

    def creacionBBDD():

        miConexion= sqlite3.connect("Usuarios")
        micursor = miConexion.cursor()

        try:
            micursor.execute('''
                CREATE TABLE DATOSUSUARIOS(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE_USUARIO VARCHAR(30),
                    APELLIDO VARCHAR(30),
                    PASSWORD VARCHAR(50),
                    DIRECCION VARCHAR(50),
                    COMENTARIOS VARCHAR(50)
                )''')

            messagebox.showinfo("Base de datos", "Base de datos creada de forma existosa")

        except:
            messagebox.showerror("Base de datos", "La base de datos ya existe")

    def limpiarCampos(miID,miNombre,miApellido,miPass,miDireccion,textoComentario):
        miID.set("")
        miNombre.set("")
        miApellido.set("")
        miPass.set("")
        miDireccion.set("")
        textoComentario.delete(1.0, END)

    def crear(self, miNombre,miApellido,miPass,miDireccion,CuadroTexto):
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()
        datosusuarios = miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get(),CuadroTexto.get("1.0", END)

        miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datosusuarios))
        miConexion.commit()
        messagebox.showinfo("Base de datos", "Se ha realizado el registro con éxito")

        self.limpiarCampos()
