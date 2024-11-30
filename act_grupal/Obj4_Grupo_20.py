#Padron: 112275       Nombre y apellido: Leandro Gabriel Paz

from tkinter import *
from tkinter import messagebox

def creacion_ventana():
    raiz = Tk()

    raiz.title("Login Grupo 20")
    raiz.resizable(0, 0)  # No permite expandir la ventana
    raiz.geometry("300x130")

    raiz.iconbitmap("IMG_Grupo_20.ico")

    raiz.configure(bg="lightblue")
    
    frame = Frame(raiz, background="lightblue")
    frame.pack(pady=10)

    etiqueta_usuario = Label(frame, text="Usuario Alumno: ", fg="white", bg="black")
    etiqueta_usuario.grid(row=0, column=0, sticky="E")
    etiqueta_contraseña = Label(frame, text="Clave: ", fg="white", bg="black")
    etiqueta_contraseña.grid(row=1, column=0, sticky="E")

    nombre_usuario = StringVar()
    clave_usuario = StringVar()


    cuadro_usuario = Entry(frame)
    cuadro_usuario.grid(row=0, column=1, padx=10,pady=10)
    cuadro_contraseña = Entry(frame, show="*")
    cuadro_contraseña.grid(row=1, column=1, padx=10,pady=10)
   
    frame_botones = Frame(raiz, background="lightblue")
    frame_botones.pack(padx=5)

    boton_enviar = Button(frame_botones, text="Ingresar", command=lambda: validacion_datos(dic, cuadro_usuario, cuadro_contraseña))
    boton_enviar.grid(row=0, column=0, padx=10)

    boton_registrar = Button(frame_botones, text="Registrar nuevo usuario", command=ventana_registrar_nuevo_usuario)
    boton_registrar.grid(row=0, column=1, padx=10)

    raiz.mainloop()


dic = {
    "Nahuel":"nahue1234",
    "Luciano": "luciano2024",
    "Francisco" : "fran888",
    "Leandro":"lean2000",
    "Jhonny":"jony12345"
}


def validacion_datos(dic,cuadro_usuario,cuadro_contraseña):

    usuario = cuadro_usuario.get()
    contraseña = cuadro_contraseña.get()
    
    if usuario in dic and dic[usuario] == contraseña:
        messagebox.showinfo("Datos recibidos", "Usuario y Clave Correctos")
    else:
        messagebox.showerror("Error", "Algunos de los datos ingresados es Incorrecto.")

    cuadro_usuario.delete(0, END)
    cuadro_contraseña.delete(0, END)


def ventana_registrar_nuevo_usuario():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Registrar nuevo usuario")
    nueva_ventana.resizable(False,False)
    nueva_ventana.geometry("300x130")
    nueva_ventana.configure(bg="lightblue")

    etiqueta_nuevo_usuario = Label(nueva_ventana, text="Nuevo usuario: ", fg="white", bg="black")
    etiqueta_nuevo_usuario.grid(row=0, column=0, sticky="E")
    etiqueta_nueva_contraseña = Label(nueva_ventana, text="Clave: ", fg="white", bg="black")
    etiqueta_nueva_contraseña.grid(row=1, column=0, sticky="E")
    
    cuadro_nuevo_usuario = Entry(nueva_ventana)
    cuadro_nuevo_usuario.grid(row=0, column=1, padx=10,pady=10)
    cuadro_nueva_contraseña = Entry(nueva_ventana, show="*")
    cuadro_nueva_contraseña.grid(row=1, column=1, padx=10,pady=10)
    
    boton_registrar_nuevo_usuario = Button(nueva_ventana, text="Nuevo usuario", command=lambda: registrar_usuario(cuadro_nuevo_usuario, cuadro_nueva_contraseña, nueva_ventana))
    boton_registrar_nuevo_usuario.grid(row=2, column=1, padx=5)


def registrar_usuario(cuadro_nuevo_usuario, cuadro_nueva_contraseña, ventana):
    nuevo_usuario = cuadro_nuevo_usuario.get()
    nueva_contraseña = cuadro_nueva_contraseña.get()

    if nuevo_usuario in dic:
        messagebox.showerror("Error", "El usuario ya existe")
    elif not nuevo_usuario or not nueva_contraseña:
        messagebox.showerror("Error", "Debes completar ambos campos")
    else:
        dic[nuevo_usuario] = nueva_contraseña
        messagebox.showinfo("Exito","El usuario fue agregado con exito")
        ventana.destroy()
    
def main():
    creacion_ventana()
main()
