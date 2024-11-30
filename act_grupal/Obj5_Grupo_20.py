# Nombre y apellido: Leandro Gabirel Paz
# Legajo: 112275


from tkinter import *
from tkinter import messagebox

def obtener_usuarios_claves():
    return {
        "Nahuel": "nahue1234",
        "Luciano": "luciano2024",
        "Francisco": "fran888",
        "Leandro": "lean2000",
        "Jhonny": "jony12345"
    }

def creacion_ventana(dic_usuarios):
    raiz = Tk()
    raiz.title("Login Grupo 20")
    raiz.resizable(0, 0)  # No permite expandir la ventana
    raiz.geometry("300x130")
#    raiz.iconbitmap("/home/leo/Escritorio/Cosas_de_leo__NO_VER/Facultad/Fund_prog_Guarna/clase_11/interface/act_grupal/IMG_Grupo_20.ico")
    raiz.configure(bg="lightblue")

    mi_frame = Frame(raiz, bg="lightblue")
    mi_frame.grid(row=0, column=0, padx=10, pady=10)

    frame_botones = Frame(raiz, bg="lightblue")
    frame_botones.grid(row=2, column=0, padx=5, pady=5)

    cuadro_usuario = Entry(mi_frame)
    cuadro_usuario.grid(row=0, column=1, padx=10, pady=10)
    cuadro_usuario.config(justify="center")

    cuadro_clave = Entry(mi_frame, show="*")
    cuadro_clave.grid(row=1, column=1, padx=10, pady=10)
    cuadro_clave.config(justify="center")

    label_usuario = Label(mi_frame, text="Usuario Alumno: ")
    label_usuario.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    label_clave = Label(mi_frame, text="Clave: ")
    label_clave.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    boton_enviar = Button(frame_botones, text="Ingresar", command=lambda: validacion_datos(
        dic_usuarios, cuadro_usuario.get(), cuadro_clave.get()))
    boton_enviar.grid(row=0, column=0, padx=5)

    boton_nuevo_usuario = Button(
        frame_botones, text="Nuevo usuario", command=lambda: ventana_registro(dic_usuarios))
    boton_nuevo_usuario.grid(row=0, column=1, padx=5)

    raiz.mainloop()


def validacion_datos(dic, cuadro_usuario, cuadro_clave):
    if cuadro_Usuario in dic and dic[cuadro_Usuario] == cuadro_clave:
        messagebox.showinfo("Datos recibidos", "Usuario y Clave Correctos")
    else:
        messagebox.showerror(
            "Error", "Algunos de los datos ingresados es Incorrecto.")


def registrar_usuario(dic_usuarios, cuadro_usuario, cuadro_clave, ventana):
    if cuadro_usuario in dic_usuarios:
        messagebox.showwarning("Error", "El usuario ya existe")
    else:
        dic_usuarios[cuadro_usuario] = cuadro_clave
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
        ventana.destroy()


def ventana_registro(dic_usuarios):
    ventana_registro = Toplevel()
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("300x130")
    ventana_registro.resizable(False, False)
    ventana_registro.configure(bg="lightblue")
    ventana_registro.iconbitmap(
        "/home/leo/Escritorio/Cosas_de_leo__NO_VER/Facultad/Fund_prog_Guarna/clase_11/interface/act_grupal/IMG_Grupo_20.ico")

    mi_frame = Frame(ventana_registro, bg="lightblue")
    mi_frame.grid(row=0, column=0, padx=10, pady=10)

    label_usuario = Label(mi_frame, text="Nuevo Usuario:")
    label_usuario.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    nuevo_usuario = Entry(mi_frame)
    nuevo_usuario.grid(row=0, column=1, padx=10, pady=10)
    nuevo_usuario.config(justify="center")

    label_clave = Label(mi_frame, text="Nueva Clave:")
    label_clave.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    nueva_clave = Entry(mi_frame, show="*")
    nueva_clave.grid(row=1, column=1, padx=10, pady=10)
    nueva_clave.config(justify="center")

    frame_botones = Frame(ventana_registro, bg="lightblue")
    frame_botones.grid(row=2, column=0, padx=5, pady=5)

    boton_registrar = Button(frame_botones, text="Registrar", command=lambda: registrar_usuario(
        dic_usuarios, nuevo_usuario.get(), nueva_clave.get(), ventana_registro))
    boton_registrar.grid(row=0, column=0, padx=3, pady=3)


def main():
    dic_usuarios = obtener_usuarios_claves()
    creacion_ventana(dic_usuarios)


main()
