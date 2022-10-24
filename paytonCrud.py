from tkinter import *
from baseDeDatos.baseDeDatos import *
from tkinter import messagebox


#-------------------------- Funcion------------------------------------

def salirDelSistema():
    valor = messagebox.askquestion("Salir", "Desea salir de la aplicacion")

    if valor=="yes":
        raiz.destroy()

#---------------------------- interface ----------------------------------------------

raiz = Tk()

#--------------Barra de menu--------------------------
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Crear base de datos",command=lambda:BaseDeDatosCrud.creacionBBDD())
bbddMenu.add_command(label="Salir", command=lambda:salirDelSistema())

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Limpiar Campos", command=lambda:BaseDeDatosCrud.limpiarCampos(miID,miNombre,miApellido,miPass,miDireccion,textoComentario))

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Limpiar", menu=borrarMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-------------- Campos --------------------------------

frameCampos = Frame(raiz)
frameCampos.pack()

miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()
#miComentario= StringVar()

cuadroID = Entry(frameCampos, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(frameCampos, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido = Entry(frameCampos, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass = Entry(frameCampos, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroDireccion = Entry(frameCampos, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

"""cuadroComentario = Entry(frameCampos, textvariable=miComentario)
cuadroComentario.grid(row=5,column=1,padx=10,pady=10)"""

textoComentario = Text(frameCampos, width=16, height=5)
textoComentario.grid(row=5, column=1,padx=10, pady=10)
scrollVert = Scrollbar(frameCampos,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#-----------------------Labels---------------------------------------

idLabel = Label(frameCampos, text="ID")
idLabel.grid(row=0,column=0,sticky="e", padx=10, pady=10)

nombreLabel = Label(frameCampos,text="Nombre")
nombreLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(frameCampos, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(frameCampos, text="Contraseña")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(frameCampos, text="Dirección")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel = Label(frameCampos, text="Comentarios")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#------------------------Botones--------------------------------------

frameBotones = Frame(raiz)
frameBotones.pack()

botonCrear = Button(frameBotones, text= "Crear", command=lambda:BaseDeDatosCrud.crear(miNombre,miApellido,miPass,miDireccion,textoComentario))
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(frameBotones, text= "Buscar", command=lambda:BaseDeDatosCrud.leer(miID,miNombre,miApellido,miPass,miDireccion,textoComentario))
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10 )

botonActualizar = Button(frameBotones, text= "Actualizar", command=lambda:BaseDeDatosCrud.actualizar(miID,miNombre,miApellido,miPass,miDireccion,textoComentario))
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonEliminar = Button(frameBotones, text="Eliminar", command=lambda:BaseDeDatosCrud.eliminar(miID,miNombre,miApellido,miPass,miDireccion,textoComentario))
botonEliminar.grid(row=1, column=4, sticky="e", padx=10, pady=10)

raiz.mainloop()