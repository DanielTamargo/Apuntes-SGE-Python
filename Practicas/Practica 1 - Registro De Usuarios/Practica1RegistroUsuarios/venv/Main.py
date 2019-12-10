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
# Paso extra 1. Una simulación de entrada y carga de la aplicación
EjecucionesPR1.paripe_inicial()    #<- desactiva esta para no andar esperando con los time.sleep()

# Paso extra 2. Mostrar la lista de usuarios y sus datos
EjecucionesPR1.lista_usuarios()

# Punto 1. Usuario + comprobar que sea único
usuario = EjecucionesPR1.usuario()

# Puntos 2 y 3. Contraseña + nivel de seguridad
contrasenya = EjecucionesPR1.contrasenya()

# Punto 4. Email + comprobar que sea válido
email = EjecucionesPR1.email()

# Punto 5. Mostrar y guardar los datos
EjecucionesPR1.guardar_usuario(usuario, contrasenya, email)

# Este paso extra 3 es solo si quieres usar el envío del email en ascii (recomiendo simplemente configurarlo a UTF-8
# Paso extra 3. Método adicional para evitar caracteres no soportados por ascii (ñ, ¡, ¿) (por si dejas la configuración ascii en smtplib.py)
# si los usas tienes que cambiarle los parámetros que le mandas a la función que hay debajo (preguntar_mandar_email)
usuario_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(usuario)
contrasenya_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(contrasenya)
email_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(email)

# Punto 6 (opcional). Enviar correo con los datos (el método pregunta al usuario si quiere mandar el correo o no)
# OJO, tengo configurado smtplib.py como UTF-8 pero de normal viene como ASCII, si da problemas tienes que cambiar esto:
# External Libraries -> Python 3.8 -> Lib -> smtplib.py -> buscar: msg = _fix_eols(msg).encode('ascii') y cambiar ascii por UTF-8
EjecucionesPR1.preguntar_mandar_email(usuario, contrasenya, email)
print("Fin del programa, gracias por utilizar " + colorama.Fore.LIGHTCYAN_EX + "The Best Password Generator"
      + colorama.Fore.RESET + ".")