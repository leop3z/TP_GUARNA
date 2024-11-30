#def validar_nuevo_correo(cuadro_correo):
#    caracteres_permitidos = ["-", "_", "."]
#    dominios = ["fi.uba.ar", "gmail.com", "uba.ar"]
#    correo_valido = True
#
#    if len(cuadro_correo) < 10 or len(cuadro_correo) > 25:
#        correo_valido = False
#
#    if cuadro_correo.count("@") != 1:
#        correo_valido = False
#
#    for letra in cuadro_correo:
#        if not letra.isalnum() or letra not in caracteres_permitidos:
#            correo_valido = False
#
#    dominio = cuadro_correo.split("@")[-1]
#    if dominio not in dominios:
#        correo_valido = False
#
#    return correo_valido
#
#
#def main():
#    correo = validar_nuevo_correo("pampaenanos@gmail.com")
#    print(correo)  # Esto debería imprimir True
#
#main()
