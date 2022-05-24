# Librerias
from ast import Delete
from asyncio.windows_events import NULL
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import ITALIC
from turtle import left, title
import pymysql

global nom, edi, autor, isbn, cat, lib
global usuario, contrasena, nivel, nombre, apellidos, edad
i=0

def connect():
    global bd 
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="loginPython"
    )

def ingreso_datos():
    connect()
    fcursor = bd.cursor()
    sql = "INSERT INTO registro (usuario,contrasena,nivel,nombre,apellido,edad) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
        usuario.get(), contrasena.get(), nivel.get(), nombre.get(),apellidos.get(),edad.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Registro fallido",title="Aviso")
    bd.close()

def ingreso_datos_libros():
    connect()
    fcursor = bd.cursor()
    sql = "INSERT INTO libros (nombre,editorial,autor,isbn,categoria,libreria) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
    nom.get(), edi.get(),autor.get(),isbn.get(),cat.get(),lib.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Registro fallido",title="Aviso")
    bd.close()

def borrar_datos_user():
    connect()
    print (deleted.get())
    fcursor = bd.cursor()
    sql = "DELETE FROM registro WHERE nombre = '{0}'".format(
    deleted.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Registro fallido",title="Aviso")
    bd.close()

def borrar_datos_libros():
    connect()
    fcursor = bd.cursor()
    sql = "DELETE FROM libros WHERE nombre = '{0}'".format(
    delete.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Registro fallido",title="Aviso")
    bd.close()

def modificar_datos_libros():
    global nom, edi, autor, isbn, cat, lib
    connect()
    fcursor = bd.cursor()
    sql = "UPDATE libros SET nombre='{1}',editorial='{2}',autor='{3}',isbn='{4}',categoria='{5}',libreria='{6}' WHERE nombre='{0}'".format(
    delete.get(),nom.get(),edi.get(),autor.get(),isbn.get(),cat.get(),lib.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Actualizacion exitosa", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Actualizacion fallida",title="Aviso")
    bd.close()

def modificar_datos_usuarios():
    global usuario, contrasena, nivel, nombre, apellidos, edad, deleted
    connect()
    fcursor = bd.cursor()
    sql = "UPDATE registro SET usuario='{1}',contrasena='{2}',nivel='{3}',nombre='{4}',apellido='{5}',edad='{6}' WHERE usuario='{0}'".format(
    deleted.get(),usuario.get(),contrasena.get(),nivel.get(),nombre.get(),apellidos.get(),edad.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Actualizacion exitosa", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="Actualizacion fallida",title="Aviso")
    bd.close()

def validacionDatos():
    connect()
    fcursor = bd.cursor()
    fcursor.execute("SELECT nivel FROM registro WHERE usuario='"+ usuarioNombre.get()  +"' AND contrasena = '"+ usuarioContrasena.get()  +"';")
    recursos = fcursor.fetchall()
    if recursos != pymysql.NULL:
        bd.close()
        if recursos[0][0] == 0:
            admin()
        else:
            usuario()
    else:
        messagebox.showinfo(title="Inicio de sesión incorrecto", message="usuario y contraseña incorrecto")
    bd.close()

def menu_screen():
    global principalScreen
    # Menu principal
    principalScreen = Tk()
    principalScreen.geometry("300x200")
    principalScreen.title("Bienvenido")
    # principalScreen.iconbitmap("") cambiar el icono de la ventana - solo se pueden cargar extensiones .ico

    # Para poner una imagen en la ventana
    # image = PhotoImage(file = "") Solo imagenes .gif
    # Dimension : image.subsample(#,#)
    #label = Label(image=image)
    # label.pack()

    Label(text="Acceso al sistema", bg="navy", fg="white",
          width="300", height="3", font=("Consolas", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3",
           width="30", command=inicio_sesion).pack()

    principalScreen.mainloop()

def inicio_sesion():
    global pantalla1

    pantalla1 = Toplevel(principalScreen)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de sesión")
    Label(pantalla1, text="Ingrese su usuario y contraseña a continuacion:").pack()
    Label(pantalla1, text="").pack()

    global usuarioNombre
    global usuarioContrasena

    usuarioNombre = StringVar()
    usuarioContrasena = StringVar()

    global nombreUsuarioIngresado
    global contraUsuarioIngresado

    Label(pantalla1, text="Usuario:").pack()
    nombreUsuarioIngresado = Entry(pantalla1, textvariable=usuarioNombre)
    nombreUsuarioIngresado.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña:").pack()
    contraUsuarioIngresado = Entry(pantalla1, show="*", textvariable=usuarioContrasena)
    contraUsuarioIngresado.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar sesión", command=validacionDatos).pack()

def usuario():
    global librosABCM 
    librosABCM = Tk()
    librosABCM.geometry("490x200")
    librosABCM.title("Libros")
    Label(librosABCM, text="🐙  Bienvenido a la libreria  🐙",bg="navy", fg="white",width="44", height="3",font=("Helvetica", 15)).pack()
    Button(librosABCM,text="Consulta",bg="navy", fg="white",
          width="20",border="5",overrelief="sunken", font=("Helvetica", 15),command=ventanaConsultaLibros2).place(x=130,y=100)
    librosABCM.mainloop()

def admin():
    ventana = Tk()
    ventana.geometry("490x300")
    ventana.title("Libros")
    Label(ventana, text="▌│█║▌║▌  Registros de usuarios  ▌║▌║█│▌",bg="navy", fg="white",width="44", height="2",font=("Helvetica", 15)).pack()
    Button(ventana,text="Alta",bg="navy", fg="white",
          width="19", height="1",border="5",overrelief="sunken", font=("Helvetica", 15),command=ventanaAltaUser).place(x=15,y=75)
    Button(ventana,text="Consulta",bg="navy", fg="white",
          width="19", height="1",border="5",overrelief="sunken", font=("Helvetica", 15),command=ventanaConsultaUsers).place(x=250,y=75)
    
    Label(ventana, text="▌│█║▌║▌  Registros de libros  ▌║▌║█│▌",bg="navy",fg="white",width="44", height="2",font=("Helvetica", 15)).place(x=0,y=150)
    Button(ventana,text="Alta",bg="navy", fg="white",
          width="19", height="1",border="5",overrelief="sunken", font=("Helvetica", 15),command=ventanaAltaLibros).place(x=15,y=225)
    Button(ventana,text="Consulta",bg="navy", fg="white",
          width="19", height="1",border="5",overrelief="sunken", font=("Helvetica", 15),command=ventanaConsultaLibros).place(x=250,y=225)
    
    ventana.mainloop()

def ventanaAltaUser():
    global usuario, contrasena, nivel, nombre, apellidos, edad
    ventanaAltaUser = Tk()
    ventanaAltaUser.title("Alta")
    ventanaAltaUser.geometry("250x420")
    Label(ventanaAltaUser,text="Alta de Usuario",width="44",anchor="w",padx="10",bg="navy",fg="white",font=("Console",15)).pack()
    Label(ventanaAltaUser,text="Usuario",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    usuario = Entry(ventanaAltaUser)
    usuario.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAltaUser,text="Contraseña",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    contrasena = Entry(ventanaAltaUser)
    contrasena.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAltaUser,text="Nivel",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    nivel = Entry(ventanaAltaUser)
    nivel.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAltaUser,text="Nombre(s)",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    nombre = Entry(ventanaAltaUser)
    nombre.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAltaUser,text="Apellido(s)",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    apellidos = Entry(ventanaAltaUser)
    apellidos.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAltaUser,text="Edad",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    edad = Entry(ventanaAltaUser)
    edad.pack(anchor="w",padx=10,fill="x")
    Button(ventanaAltaUser,text="Reiniciar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15)).pack(pady=10)
    Button(ventanaAltaUser,text="Guardar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15),command=ingreso_datos).pack()

def ventanaConsultaUsers():
    global deleted
    i=0
    ventanaConsultaUsers = Tk()
    ventanaConsultaUsers.geometry("565x200")
    ventanaConsultaUsers.title("Libros en stock")
    Label(ventanaConsultaUsers,text="Usuario",bg="navy",anchor="w",padx=12,fg="white",font=("Helvetica", 15)).grid(row=0,column=0)
    Label(ventanaConsultaUsers,text="Contraseña",bg="navy",anchor="w",padx=12,fg="white",font=("Helvetica", 15)).grid(row=0,column=1)
    Label(ventanaConsultaUsers,text="Nombre(s)",bg="navy",anchor="w",padx=12,fg="white",font=("Helvetica", 15)).grid(row=0,column=2)
    Label(ventanaConsultaUsers,text="Apellido(s)",bg="navy",anchor="w",padx=12,fg="white",font=("Helvetica", 15)).grid(row=0,column=3)
    Label(ventanaConsultaUsers,text="Edad",bg="navy",anchor="w",padx=25,fg="white",font=("Helvetica", 15)).grid(row=0,column=4)
    connect()
    i+=1
    fcursor = bd.cursor()
    sql = "SELECT * FROM registro"
    try:
        fcursor.execute(sql)
        for row in fcursor:
            Label(ventanaConsultaUsers,text=f"{row[0]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=0)
            Label(ventanaConsultaUsers,text=f"{row[1]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=1)
            Label(ventanaConsultaUsers,text=f"{row[3]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=2)
            Label(ventanaConsultaUsers,text=f"{row[4]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=3)
            Label(ventanaConsultaUsers,text=f"{row[5]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=4)
            i+=1
        bd.commit()
    except:
        bd.rollback()
        messagebox.showinfo(message="Error al cargar la DB",title="Aviso")
    bd.close()
    Label(ventanaConsultaUsers).grid(row=i,column=0)
    i+=1
    Label(ventanaConsultaUsers).grid(row=i,column=0)
    i+=1
    Label(ventanaConsultaUsers).grid(row=i,column=0)
    i+=1
    Label(ventanaConsultaUsers,text="Usuario",font=("Helvetica", 13)).grid(row=i,column=0,sticky=W,padx=10)
    deleted = Entry(ventanaConsultaUsers)
    i+=1
    deleted.grid(row=i,column=0,columnspan=3,ipadx=100,sticky=W,padx=10)
    Button(ventanaConsultaUsers,text="Borrar",bg="navy",fg="white",border="5",overrelief="sunken", font=("Console", 10),command=borrar_datos_user).grid(row=i,column=3,sticky=W,ipadx=15)
    Button(ventanaConsultaUsers,text="Modificar",bg="navy",fg="white",border="5",overrelief="sunken", font=("Console", 10),command=ventanaModificacionUsers).grid(row=i,column=4,sticky=W,ipadx=10)
    
    ventanaConsultaUsers.mainloop()

def ventanaAltaLibros():
    global ventanaAlta
    global nom, edi, autor, isbn, cat, lib
    ventanaAlta = Tk()
    ventanaAlta.title("Alta")
    ventanaAlta.geometry("250x420")
    Label(ventanaAlta,text="Alta de libro",width="44",anchor="w",padx="10",bg="navy",fg="white",font=("Console",15)).pack()
    Label(ventanaAlta,text="Nombre",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    nom = Entry(ventanaAlta)
    nom.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAlta,text="Editorial",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    edi = Entry(ventanaAlta)
    edi.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAlta,text="Autor",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    autor = Entry(ventanaAlta)
    autor.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAlta,text="ISBN",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    isbn = Entry(ventanaAlta)
    isbn.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAlta,text="Categoria",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    cat = Entry(ventanaAlta)
    cat.pack(anchor="w",padx=10,fill="x")
    Label(ventanaAlta,text="Libreria",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    lib = Entry(ventanaAlta)
    lib.pack(anchor="w",padx=10,fill="x")
    Button(ventanaAlta,text="Reiniciar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15)).pack(pady=10)
    Button(ventanaAlta,text="Guardar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15),command=ingreso_datos_libros).pack()

def ventanaConsultaLibros():
    global delete
    i=0
    ventanaConsultaLibros = Tk()
    ventanaConsultaLibros.geometry("651x300")
    ventanaConsultaLibros.title("Libros en stock")
    Label(ventanaConsultaLibros,text="Titulo",bg="navy",anchor="w",padx=65,fg="white",font=("Helvetica", 15)).grid(row=0,column=0)
    Label(ventanaConsultaLibros,text="Editorial",bg="navy",anchor="w",padx=20,fg="white",font=("Helvetica", 15)).grid(row=0,column=1)
    Label(ventanaConsultaLibros,text="Autor",bg="navy",anchor="w",padx=25,fg="white",font=("Helvetica", 15)).grid(row=0,column=2)
    Label(ventanaConsultaLibros,text="ISBN",bg="navy",anchor="w",padx=19,fg="white",font=("Helvetica", 15)).grid(row=0,column=3)
    Label(ventanaConsultaLibros,text="Categoria",bg="navy",anchor="w",padx=2,fg="white",font=("Helvetica", 15)).grid(row=0,column=4)
    Label(ventanaConsultaLibros,text="Libreria",bg="navy",anchor="w",padx=2,fg="white",font=("Helvetica", 15)).grid(row=0,column=5)
    connect()
    i+=1
    fcursor = bd.cursor()
    sql = "SELECT * FROM libros"
    try:
        fcursor.execute(sql)
        for row in fcursor:
            Label(ventanaConsultaLibros,text=f"{row[0]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=0)
            Label(ventanaConsultaLibros,text=f"{row[1]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=1)
            Label(ventanaConsultaLibros,text=f"{row[2]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=2)
            Label(ventanaConsultaLibros,text=f"{row[3]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=3)
            Label(ventanaConsultaLibros,text=f"{row[4]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=4)
            Label(ventanaConsultaLibros,text=f"{row[5]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=5)
            i+=1
        bd.commit()
    except:
        bd.rollback()
        messagebox.showinfo(message="Error al cargar la DB",title="Aviso")
    bd.close()
    Label(ventanaConsultaLibros).grid(row=i,column=0)
    i+=1
    Label(ventanaConsultaLibros).grid(row=i,column=0)
    i+=10
    Label(ventanaConsultaLibros).grid(row=i,column=0)
    i+=1
    Label(ventanaConsultaLibros,text="Titulo",font=("Helvetica", 13)).grid(row=i,column=0,sticky=W,padx=10)
    delete = Entry(ventanaConsultaLibros)
    i+=1
    delete.grid(row=i,column=0,columnspan=3,ipadx=100,sticky=W,padx=10)
    Button(ventanaConsultaLibros,text="Borrar",bg="navy",fg="white",border="5",overrelief="sunken", font=("Console", 10),command=borrar_datos_libros).grid(row=i,column=3,sticky=W,ipadx=15)
    Button(ventanaConsultaLibros,text="Modificar",bg="navy",fg="white",border="5",overrelief="sunken", font=("Console", 10),command=ventanaModificacionLibros).grid(row=i,column=4,sticky=W,ipadx=10)

    ventanaConsultaLibros.mainloop()

def ventanaConsultaLibros2():
    i=0
    ventanaConsultaLibros = Tk()
    ventanaConsultaLibros.geometry("651x300")
    ventanaConsultaLibros.title("Libros en stock")
    Label(ventanaConsultaLibros,text="Titulo",bg="navy",anchor="w",padx=65,fg="white",font=("Helvetica", 15)).grid(row=0,column=0)
    Label(ventanaConsultaLibros,text="Editorial",bg="navy",anchor="w",padx=20,fg="white",font=("Helvetica", 15)).grid(row=0,column=1)
    Label(ventanaConsultaLibros,text="Autor",bg="navy",anchor="w",padx=25,fg="white",font=("Helvetica", 15)).grid(row=0,column=2)
    Label(ventanaConsultaLibros,text="ISBN",bg="navy",anchor="w",padx=19,fg="white",font=("Helvetica", 15)).grid(row=0,column=3)
    Label(ventanaConsultaLibros,text="Categoria",bg="navy",anchor="w",padx=2,fg="white",font=("Helvetica", 15)).grid(row=0,column=4)
    Label(ventanaConsultaLibros,text="Libreria",bg="navy",anchor="w",padx=2,fg="white",font=("Helvetica", 15)).grid(row=0,column=5)
    connect()
    i+=1
    fcursor = bd.cursor()
    sql = "SELECT * FROM libros"
    try:
        fcursor.execute(sql)
        for row in fcursor:
            Label(ventanaConsultaLibros,text=f"{row[0]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=0)
            Label(ventanaConsultaLibros,text=f"{row[1]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=1)
            Label(ventanaConsultaLibros,text=f"{row[2]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=2)
            Label(ventanaConsultaLibros,text=f"{row[3]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=3)
            Label(ventanaConsultaLibros,text=f"{row[4]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=4)
            Label(ventanaConsultaLibros,text=f"{row[5]}",anchor="w",font=("Helvetica", 11)).grid(row=i,column=5)
            i+=1
        bd.commit()
    except:
        bd.rollback()
        messagebox.showinfo(message="Error al cargar la DB",title="Aviso")
    bd.close()

def ventanaModificacionLibros():
    global nom, edi, autor, isbn, cat, lib
    ventanaModificacion = Tk()
    ventanaModificacion.title("Alta")
    ventanaModificacion.geometry("250x420")
    Label(ventanaModificacion,text="Alta de libro",width="44",anchor="w",padx="10",bg="navy",fg="white",font=("Console",15)).pack()
    Label(ventanaModificacion,text="Nombre",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    nom = Entry(ventanaModificacion)
    nom.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Editorial",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    edi = Entry(ventanaModificacion)
    edi.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Autor",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    autor = Entry(ventanaModificacion)
    autor.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="ISBN",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    isbn = Entry(ventanaModificacion)
    isbn.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Categoria",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    cat = Entry(ventanaModificacion)
    cat.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Libreria",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    lib = Entry(ventanaModificacion)
    lib.pack(anchor="w",padx=10,fill="x")
    Button(ventanaModificacion,text="Reiniciar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15)).pack(pady=10)
    Button(ventanaModificacion,text="Guardar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15),command=modificar_datos_libros).pack()

def ventanaModificacionUsers():
    global usuario, contrasena, nivel, nombre, apellidos, edad
    ventanaModificacion = Tk()
    ventanaModificacion.title("Alta")
    ventanaModificacion.geometry("250x420")
    Label(ventanaModificacion,text="Modificacion de Usuario",width="44",anchor="w",padx="10",bg="navy",fg="white",font=("Console",15)).pack()
    Label(ventanaModificacion,text="Usuario",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    usuario = Entry(ventanaModificacion)
    usuario.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Contrasena",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    contrasena = Entry(ventanaModificacion)
    contrasena.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Nivel",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    nivel = Entry(ventanaModificacion)
    nivel.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Nombre",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    nombre = Entry(ventanaModificacion)
    nombre.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Apellido(s)",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    apellidos = Entry(ventanaModificacion)
    apellidos.pack(anchor="w",padx=10,fill="x")
    Label(ventanaModificacion,text="Edad",anchor="w",padx="10",font=("Console",12,"italic")).pack(anchor="w",padx=10)
    edad = Entry(ventanaModificacion)
    edad.pack(anchor="w",padx=10,fill="x")
    Button(ventanaModificacion,text="Reiniciar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15)).pack(pady=10)
    Button(ventanaModificacion,text="Guardar",bg="navy", fg="white",width="20",border="5",overrelief="sunken", font=("Helvetica", 15),command=modificar_datos_usuarios).pack()

menu_screen()