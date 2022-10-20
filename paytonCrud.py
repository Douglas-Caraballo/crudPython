from tkinter import *
from tkinter import messagebox
import sqlite3

#---------------------------- interface ----------------------------------------------

raiz = Tk()

#--------------Barra de menu--------------------------
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Crear base de datos")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Limpiar Campos")

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Limpiar", menu=borrarMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-------------- Campos --------------------------------

frameCampos = Frame(raiz)
frameCampos.pack()







raiz.mainloop()