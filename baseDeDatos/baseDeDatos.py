import sqlite3
from tkinter import messagebox

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