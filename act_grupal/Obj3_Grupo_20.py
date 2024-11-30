#Padron: 112275       Nombre y apellido: Leandro Gabriel Paz

from tkinter import *

def creacion_ventana():
    raiz = Tk()

    raiz.title("Login Grupo 20")
    raiz.resizable(0, 0)  # No permite expandir la ventana
    raiz.geometry("300x130")

    raiz.iconbitmap("/home/leo/Escritorio/Cosas_de_leo__NO_VER/Facultad/Fund_prog_Guarna/clase_11/interface/act_grupal/IMG_Grupo_20.ico")

    raiz.configure(bg="lightblue")
    
    frame = Frame(raiz, background="lightblue")
    frame.pack(pady=10)

    etiqueta_usuario = Label(frame, text="Usuario Alumno: ", fg="white", bg="black")
    etiqueta_usuario.grid(row=0, column=0, sticky="E")
    etiqueta_contraseña = Label(frame, text="Clave: ", fg="white", bg="black")
    etiqueta_contraseña.grid(row=1, column=0, sticky="E")
    
    cuadro_usuario = Entry(frame)
    cuadro_usuario.grid(row=0, column=1, padx=10,pady=10)
    cuadro_contraseña = Entry(frame, show="*")
    cuadro_contraseña.grid(row=1, column=1, padx=10,pady=10)

    boton_envio = Button(raiz,text="Enviar")
    boton_envio.pack(pady=5)
    raiz.mainloop()


def main():
    creacion_ventana()
main()
