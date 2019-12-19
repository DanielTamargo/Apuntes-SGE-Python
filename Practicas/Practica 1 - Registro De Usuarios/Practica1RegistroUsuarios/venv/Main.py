import FuncionesPR1
import EjecucionesPR1
import time
import sys
import random
import colorama

# Ejecuta el programa desde aquí

# ----------------------------------------------------  IMPORTANTE  ----------------------------------------------------
# Importante realizar estos 2 pasos:
### Utilizo colorama, y lo tienes que instalar en tu python (la librería que hay que importar después ya está improtada)
# Abrir la consola de windows e introducir: pip install colorama
### si vas a utilizar caracteres que ascii no soporte, tienes que cambiar el siguiente valor:
# External Libraries -> Python 3.8 -> Lib -> smtplib.py -> buscar: msg = _fix_eols(msg).encode('ascii') y cambiar ascii por UTF-8
### Si no cambias ascii por UTF-8, dará problemas al enviar el email
### (Aunque también he creado un método para convertir a ascii (cambia ñ por n, ¿ por ?, ¡ por !)

### Para consultar las notas, hay un archivo llamado notas.txt
# ----------------------------------------------------  DATOS BASE  ----------------------------------------------------
### Por si acaso comentas los pasos de usuario, contrasenya o email (o todos), dejo aquí los datos base que usaría,
# puedes modificarlos como quieras, por ejemplo, poner tu email para que te llegue a ti
# algunos caracteres (ñ, ¡, ¿) dan problemas al enviar el correo si dejamos la configuración de smtplib.py en ascii
usuario = "dani"
contrasenya = "test"
email = "danieltamargosaiz@gmail.com"

### Ojo, estos datos son solo los que irías pidiendo al usuario por pantalla, los datos cargados los carga desde
# el fichero datos.txt. Esos datos se muestran con el método EjecucionesPR1.lista_usuarios()
# -----------------------------------------------------  PRÁCTICA  -----------------------------------------------------

# Se podría utilizar un diccionario para acotar las declaraciones de colorama
c = dict(c=colorama.Fore.CYAN, lm=colorama.Fore.LIGHTMAGENTA_EX, r=colorama.Fore.RESET)

# Creo el switcher (aunque no lo utilizo porque ya tenía la estructura elif creada)
funciones = dict(zip([1, 2, 3, 4, 5, 6, 7, 8], [EjecucionesPR1.paripe_inicial, EjecucionesPR1.lista_usuarios, EjecucionesPR1.usuario, EjecucionesPR1.contrasenya, EjecucionesPR1.email, EjecucionesPR1.guardar_usuario, EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii, EjecucionesPR1.preguntar_mandar_email]))

print(colorama.Fore.CYAN + "Datos iniciales por si quieres enviar el email o guardar usuario sin tener que crear un usuario, contraseña e email nuevos:\n"
                           "Usuario: " + colorama.Fore.RESET + usuario + colorama.Fore.CYAN + "\nContraseña: " + colorama.Fore.RESET + contrasenya + colorama.Fore.CYAN + "\nEmail: " + colorama.Fore.RESET + email + "\n\n")

bucle = True
while bucle:

    print(colorama.Fore.CYAN + "Menú:" + colorama.Fore.RESET)
    print(colorama.Fore.LIGHTMAGENTA_EX + "1. " + colorama.Fore.RESET + "Paripé inicial.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "2. " + colorama.Fore.RESET + "Lista usuarios.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "3. " + colorama.Fore.RESET + "Nuevo usuario.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "4. " + colorama.Fore.RESET + "Generar contraseña.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "5. " + colorama.Fore.RESET + "Nuevo email.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "6. " + colorama.Fore.RESET + "Guardar usuario.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "7. " + colorama.Fore.RESET + "Convertir datos o cadena a ascii.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "8. " + colorama.Fore.RESET + "Mandar email.")
    print(colorama.Fore.LIGHTMAGENTA_EX + "9. " + colorama.Fore.RESET + "Salir.")
    numero = input("Introduce una opción: ")
    print()
    if FuncionesPR1.es_un_numero(numero):
        numero = int(numero)
        if numero == 1:
            EjecucionesPR1.paripe_inicial()
        elif numero == 2:
            EjecucionesPR1.lista_usuarios()
        elif numero == 3:
            usuario = EjecucionesPR1.usuario()
        elif numero == 4:
            contrasenya = EjecucionesPR1.contrasenya()
        elif numero == 5:
            email = EjecucionesPR1.email()
        elif numero == 6:
            if usuario == "dani":
                print(colorama.Fore.LIGHTRED_EX + "¡Primero tienes que crear un nuevo usuario!"
                      + colorama.Fore.RESET + " No puedes utilizar el usuario que viene por defecto puesto que ya está guardado.\n")
            else:
                EjecucionesPR1.guardar_usuario(usuario, contrasenya, email)
        elif numero == 7:
            print("Ascii no soporta ni las tildes, ni la ñ, ni ¡ o ¿ o ´, con este método sustituirás esos caracteres por su similar aceptable.")
            print("¿Quieres convertir usuario, email y contraseña a ascii o quieres convertir una cadena que introduzcas tu?")
            print(colorama.Fore.LIGHTMAGENTA_EX + "a) " + colorama.Fore.RESET + "Convertir datos a guardar o enviar por email.")
            print(colorama.Fore.LIGHTMAGENTA_EX + "b) " + colorama.Fore.RESET + "Convertir una cadena de texto cualquiera.")
            respuesta = ""
            respuesta = input("Opción (a/b): ")
            if respuesta is not None and respuesta != "":
                respuesta = respuesta.lower()[0]
                if respuesta == "a" or respuesta == "b":
                    print()
                    if respuesta == "a":
                        usuar_bckup = usuario
                        contr_bckup = contrasenya
                        email_bckup = email
                        print(colorama.Fore.CYAN + "Datos antes de convertir: " + colorama.Fore.RESET + usuario + ", " + contrasenya + ", " + email)
                        usuario = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(usuario)
                        contrasenya = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(contrasenya)
                        email = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(email)
                        print(colorama.Fore.CYAN + "Datos después de convertir: " + colorama.Fore.RESET + usuario + ", " + contrasenya + ", " + email)
                        if usuar_bckup == usuario and contr_bckup == contrasenya and email_bckup == email:
                            print(colorama.Fore.LIGHTMAGENTA_EX + "No ha habido ningún cambio.")
                        else:
                            print("¿Quieres mantener los cambios?.")
                            respuesta = ""
                            respuesta = input("Opción (s/n): ")
                            if respuesta is not None and respuesta != "":
                                respuesta = respuesta.lower()[0]
                                if respuesta == "s":
                                    print("Los cambios se mantendrán.")
                                elif respuesta == "n":
                                    print("Cambios revertidos.")
                                    usuario = usuar_bckup
                                    contrasenya = contr_bckup
                                    email = email_bckup
                                else:
                                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                                          + colorama.Style.RESET_ALL + " No te he entendido :( vuelve a intentarlo introduciendo s o n.\n")
                            else:
                                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                                      + colorama.Style.RESET_ALL + " ¡No has introducido nada! vuelve a intentarlo introduciendo s o n.\n")
                    else:
                        print("Introduce una cadena de texto a convertir en ascii (introduce tildes o ñ ¡ ¿)")
                        respuesta = ""
                        respuesta = input("Cadena de texto: ")
                        if respuesta is not None and respuesta != "":
                            respuesta_bckup = respuesta
                            print(colorama.Fore.CYAN + "Cadena antes de convertir: " + colorama.Fore.RESET + respuesta)
                            respuesta = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(respuesta)
                            print(colorama.Fore.CYAN + "Datos después de convertir: " + colorama.Fore.RESET + respuesta)
                            if respuesta == respuesta_bckup:
                                print(colorama.Fore.LIGHTMAGENTA_EX + "No ha habido ningún cambio." + colorama.Fore.RESET)
                        else:
                            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                                  + colorama.Style.RESET_ALL + " ¡No has introducido nada! vuelve a intentarlo introduciendo s o n.\n")
                else:
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                          + colorama.Style.RESET_ALL + " No te he entendido :( vuelve a intentarlo introduciendo a o b.\n")
            else:
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                      + colorama.Style.RESET_ALL + " ¡No has introducido nada! vuelve a intentarlo introduciendo a o b.\n")
            print()
        elif numero == 8:
            print(colorama.Fore.CYAN + "Datos actuales para mandar el email:\n"
                                     "Usuario: " + colorama.Fore.RESET + usuario + colorama.Fore.CYAN + "\nContraseña: " + colorama.Fore.RESET + contrasenya + colorama.Fore.CYAN + "\nEmail: " + colorama.Fore.RESET + email)
            if usuario == "dani" or contrasenya == "test" or email == "danieltamargosaiz@gmail.com":
                print(colorama.Fore.LIGHTRED_EX + "Cuidado. Algunos datos no han sido cambiados y son los generados inicialmente diseñados para pruebas." + colorama.Fore.RESET)
            respuesta = ""
            respuesta = input("¿Enviar el email con estos datos? (s/n): ")
            if respuesta is not None and respuesta != "":
                respuesta = respuesta.lower()[0]
                if respuesta == "s":
                    EjecucionesPR1.enviar_email(usuario, contrasenya, email)
                elif respuesta == "n":
                    print(colorama.Fore.LIGHTGREEN_EX + "Envío cancelado.\n" + colorama.Fore.RESET)
                else:
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                          + colorama.Style.RESET_ALL + " No te he entendido :( vuelve a intentarlo introduciendo s o n.\n")
            else:
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                      + colorama.Style.RESET_ALL + " ¡No has introducido nada! vuelve a intentarlo introduciendo s o n.\n")
        elif numero == 9:
            print("Fin del programa, gracias por utilizar " + colorama.Fore.LIGHTCYAN_EX + "The Best Password Generator"
                  + colorama.Fore.RESET + ".")
            bucle = False
        else:
            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                  + colorama.Style.RESET_ALL + " Introduce un número del 1 al 9.\n")
    else:
        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
              + colorama.Style.RESET_ALL + " No has introducido un número.\n")


# Paso extra 1. Una simulación de entrada y carga de la aplicación
#EjecucionesPR1.paripe_inicial()    #<- desactiva esta para no andar esperando con los time.sleep()

# Paso extra 2. Mostrar la lista de usuarios y sus datos
#EjecucionesPR1.lista_usuarios()

# Punto 1. Usuario + comprobar que sea único
#usuario = EjecucionesPR1.usuario()

# Puntos 2 y 3. Contraseña + nivel de seguridad
#contrasenya = EjecucionesPR1.contrasenya()

# Punto 4. Email + comprobar que sea válido
#email = EjecucionesPR1.email()

# Punto 5. Mostrar y guardar los datos
#EjecucionesPR1.guardar_usuario(usuario, contrasenya, email)

# Este paso extra 3 es solo si quieres usar el envío del email en ascii (recomiendo simplemente configurarlo a UTF-8
# Paso extra 3. Método adicional para evitar caracteres no soportados por ascii (ñ, ¡, ¿) (por si dejas la configuración ascii en smtplib.py)
# si los usas tienes que cambiarle los parámetros que le mandas a la función que hay debajo (preguntar_mandar_email)
#usuario_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(usuario)
#contrasenya_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(contrasenya)
#email_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(email)

# Punto 6 (opcional). Enviar correo con los datos (el método pregunta al usuario si quiere mandar el correo o no)
# OJO, tengo configurado smtplib.py como UTF-8 pero de normal viene como ASCII, si da problemas tienes que cambiar esto:
# External Libraries -> Python 3.8 -> Lib -> smtplib.py -> buscar: msg = _fix_eols(msg).encode('ascii') y cambiar ascii por UTF-8
#EjecucionesPR1.preguntar_mandar_email(usuario, contrasenya, email)
#print("Fin del programa, gracias por utilizar " + colorama.Fore.LIGHTCYAN_EX + "The Best Password Generator"
#      + colorama.Fore.RESET + ".")