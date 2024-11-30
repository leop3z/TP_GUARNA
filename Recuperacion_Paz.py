# Nombre y apellido: Leandro Gabirel Paz
# Legajo: 112275


from tkinter import *
from tkinter import messagebox

# Lee una línea del registro de usuarios y devuelve una tupla con los datos correspondientes
def leer(archivo):
    linea = archivo.readline()
    if linea:
        linea = linea.rstrip("\n")
    else:
        linea = ",,"
    campos = linea.split(",")
    return (campos[0], campos[1], campos[2])

# Función que crea la ventana principal
def ventana_principal():
    raiz = Tk()
    raiz.title("Login Grupo 20")
    raiz.resizable(0, 0)  # No permite expandir la ventana
    #raiz.iconbitmap("IMG_GRUPO20.ico")
    raiz.geometry("300x130")
    raiz.configure(bg="lightblue")

    raiz.grid_columnconfigure(0,weight=1)

    mi_frame = Frame(raiz, bg="lightblue")
    mi_frame.grid(row=0, column=0, padx=5, pady=5)

    frame_botones = Frame(raiz, bg="lightblue")
    frame_botones.grid(row=2, column=0)

    cuadro_usuario = Entry(mi_frame)
    cuadro_usuario.grid(row=0, column=1, padx=5, pady=5,sticky="ew")
    cuadro_usuario.config(justify="center")

    cuadro_clave = Entry(mi_frame, show="*")
    cuadro_clave.grid(row=1, column=1, padx=5, pady=5,sticky="ew")
    cuadro_clave.config(justify="center")

    cuadro_correo = Entry(mi_frame)
    cuadro_correo.grid(row=2, column=1, padx=5, pady=5,sticky="ew")
    cuadro_correo.config(justify="center")

    label_usuario = Label(mi_frame, text="Usuario Alumno: ")
    label_usuario.grid(row=0, column=0, sticky="w", padx=1, pady=5)

    label_clave = Label(mi_frame, text="Clave: ")
    label_clave.grid(row=1, column=0, sticky="w", padx=1, pady=5)

    label_correo = Label(mi_frame, text="Correo: ")
    label_correo.grid(row=2, column=0, sticky="w", padx=1)

    boton_enviar = Button(frame_botones, text="Ingresar", command=lambda: validacion_datos(cuadro_usuario.get(), cuadro_clave.get(), cuadro_correo.get()))
    boton_enviar.grid(row=0, column=0,pady=5, sticky="ew")

    boton_nuevo_usuario = Button(frame_botones, text="Nuevo usuario", command=lambda: ventana_registrar_usuario())
    boton_nuevo_usuario.grid(row=0, column=1, pady=5,sticky="ew")

    boton_cambiar_contraseña = Button(frame_botones, text="Recuperar contraseña", command=lambda: recuperar_contraseña(cuadro_usuario.get(), cuadro_correo.get()))
    boton_cambiar_contraseña.grid(row=0, column=2,pady=5,sticky="ew")

    # Botones ajustados al tamaño de las columnas de frame_botones
    frame_botones.grid_columnconfigure(0, weight=1)
    frame_botones.grid_columnconfigure(1, weight=1)
    frame_botones.grid_columnconfigure(2, weight=1)

    raiz.mainloop()

CLAVE_PROVISORIA = "Recuperacion2024."

def recuperar_contraseña(usuario,correo):
    arch_recuperacion = open("recuperacion.csv","w")
    arch_recuperacion.write(f"Correo enviado a {correo} \n Haz solicitado la recuperacion de tu contraseña, utiliza esta contraseña provisoria para poder acceder con tu usuario{CLAVE_PROVISORIA}")
    arch_recuperacion.close()
    messagebox.showinfo("Recuperar contraseña",f"Se ha enviado un correo a tu cuenta {correo}")


def validacion_datos(cuadro_usuario, cuadro_clave, cuadro_correo):
    try:
        arch_usuarios = open("usuarios.csv", "r")
        usuario, clave, correo = leer(arch_usuarios)
        usuario_encontrado = False

        while usuario != "":
            if cuadro_usuario == usuario and cuadro_clave == clave and cuadro_correo == correo and not usuario_encontrado:
                messagebox.showinfo("Exito", f"Bienvenido {usuario}")
                usuario_encontrado = True
            usuario, clave, correo = leer(arch_usuarios)

        if not usuario_encontrado:
            messagebox.showerror("Error","Datos ingresados incorrectos")

        arch_usuarios.close()

    except FileNotFoundError:
        arch = open("usuarios.csv", "w")
        messagebox.showerror("Error","Datos ingresados incorrectos")
        arch.close()


def validar_nuevo_correo(cuadro_correo):
    caracteres_permitidos = ["-", "_", ".","@"]
    dominios = ["fi.uba.ar", "gmail.com", "uba.ar"]
    correo_valido = True

    if len(cuadro_correo) < 10 or len(cuadro_correo) > 25:
        correo_valido = False

    if cuadro_correo.count("@") != 1:
        correo_valido = False
    elif cuadro_correo.count("@") == 1:
        user,dominio = cuadro_correo.split("@")
        if dominio not in dominios:
            correo_valido = False

    for letra in cuadro_correo:
        if not letra.isalnum() and letra not in caracteres_permitidos:
            correo_valido = False

    return correo_valido

"""
La clave de los usuarios debe cumplir con las siguientes condiciones:
      a. Tener como mínimo 6 y como máximo 10 caracteres
      b. Estar compuesta al menos por una letra mayúscula, una minúscula y un número
      c. Contener al menos uno de los siguientes caracteres: "-", "_", "."
      d. No puede haber caracteres adyacentes repetidos
       La evaluación debe estar resuelta de forma eficiente.
"""

def validar_clave_nuevo_usuario(cuadro_nueva_clave):
    es_valida = True
    caracteres_esp_permitidos = ["-","_","."]
    i = 0

    if len(cuadro_nueva_clave) < 6 or len(cuadro_nueva_clave) > 10:
        es_valida = False

    while i < len(cuadro_nueva_clave) and not cuadro_nueva_clave[i].isalnum():
        if not cuadro_nueva_clave[i].isupper() and not cuadro_nueva_clave[i].islower():
            es_valida = False
        elif cuadro_nueva_clave[i] not in caracteres_esp_permitidos:
            es_valida = False
        elif cuadro_nueva_clave[i] == cuadro_nueva_clave[i+1]:
            es_valida = False
    return es_valida


def usuario_existe(cuadro_usuario):
    archivo_usuarios = open("usuarios.csv", "r")
    usuario, clave, correo = leer(archivo_usuarios)
    existe = False

    while usuario != "":

        if usuario == cuadro_usuario:
            archivo_usuarios.close()
            existe = True
        usuario, clave, correo = leer(archivo_usuarios)

    archivo_usuarios.close()

    return existe

def registrar_usuario(cuadro_usuario, cuadro_clave, cuadro_correo, ventana):
    exito = True

    if cuadro_usuario == "" or cuadro_clave == "":
        messagebox.showerror("Error", "Usuario o clave vacíos.")
        exito = False

    if not validar_nuevo_correo(cuadro_correo):
        messagebox.showerror("Error", "Correo no válido.")
        exito = False

    if not validar_clave_nuevo_usuario(cuadro_clave):
        messagebox.showerror("Error","Clave no valida")
        exito = False

    if usuario_existe(cuadro_usuario):
        messagebox.showerror("Error", "El usuario ya existe.")
        exito = False

    if exito:
        archivo_usuarios = open("usuarios.csv", "a")
        archivo_usuarios.write(f"{cuadro_usuario},{cuadro_clave},{cuadro_correo}\n")
        archivo_usuarios.close()
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
        ventana.destroy()

def ventana_registrar_usuario():
    ventana_registrar_usuario = Toplevel()
    ventana_registrar_usuario.title("Registro de Usuario")
    ventana_registrar_usuario.geometry("300x130")
    ventana_registrar_usuario.resizable(False, False)
    ventana_registrar_usuario.configure(bg="lightblue")

    mi_frame = Frame(ventana_registrar_usuario, bg="lightblue")
    mi_frame.grid(row=0, column=0, padx=5, pady=5)

    label_usuario = Label(mi_frame, text="Nuevo Usuario:")
    label_usuario.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    nuevo_usuario = Entry(mi_frame)
    nuevo_usuario.grid(row=0, column=1, padx=5, pady=5)
    nuevo_usuario.config(justify="center")

    label_clave = Label(mi_frame, text="Nueva Clave:")
    label_clave.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    nueva_clave = Entry(mi_frame, show="*")
    nueva_clave.grid(row=1, column=1, padx=5, pady=5)
    nueva_clave.config(justify="center")

    label_correo = Label(mi_frame, text="Correo:")
    label_correo.grid(row=2, column=0, padx=5, pady=5)

    nuevo_correo = Entry(mi_frame)
    nuevo_correo.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    nuevo_correo.config(justify="center")

    frame_botones = Frame(ventana_registrar_usuario, bg="lightblue")
    frame_botones.grid(row=2, column=0, padx=5, pady=5)

    boton_registrar = Button(frame_botones, text="Registrar", command=lambda: registrar_usuario(nuevo_usuario.get(), nueva_clave.get(), nuevo_correo.get(), ventana_registrar_usuario))
    boton_registrar.grid(row=0, column=0, padx=3, pady=3)

def main():
    ventana_principal()

main()
