import FuncionesPR1
import EjecucionesPR1
import time
import sys
import random
import colorama

# Leo los datos de un fichero (y también escribo los nuevos datos en él)
# Al leer los datos, creo dos diccionarios (uno dentro de otro)
# - Diccionario1: la clave será cada usuario y el valor un Diccionario2 enlazado a ese valor
# - Diccionario2: guardará los datos, las claves serán por ejemplo los atributos, y los valores sus respectivos valores

# Notas: utilizo colorama, ya está importado en el proyecto, pero desconozco si tienes que tenerlo instalado en tu Python
# Por si acaso, he seguido estos pasos para instalarlo y añadirlo al proyecto:
# - Primero, instalar colorama en el python de tu pc con el comando:
# pip install colorama
# - Segundo, importar colorama al proyecto de PyCharm:
# Archivo -> Ajustes -> Proyecto -> Intérprete -> Clicar en el + -> Buscar y Añadir Colorama

# He refactorizado y convertido en métodos casi todos los pasos, punto por punto, pero los he movido al fichero EjecucionesPR1.py, porque en python no puedes
# Crear métodos debajo, necesita que existan encima, así que los he movido a ese otro fichero y los llamo desde aquí

# Por si acaso comentas los pasos de usuario, contrasenya o email (o todos), dejo aquí los datos base que usaría,
# puedes modificarlos como quieras, por ejemplo, poner tu email para que te llegue a ti
# algunos caracteres (ñ, ¡, ¿) dan problemas al enviar el correo si dejamos la configuración en ascii, yo la cambié a UTF-8
usuario = "dani"
contrasenya = "test"
email = "danieltamargosaiz@gmail.com"


# Paso extra 1. Una simulación de entrada y carga de la aplicación
EjecucionesPR1.paripe_inicial()          #<- desactiva esta para no andar esperando con los time.sleep()

# Paso extra 2. Mostrar la lista de usuarios y sus datos
EjecucionesPR1.lista_usuarios()

# Punto 1. Usuario
usuario = EjecucionesPR1.usuario()

# Puntos 2 y 3. Contraseña + nivel de seguridad
contrasenya = EjecucionesPR1.contrasenya()

# Punto 4. Email
email = EjecucionesPR1.email()

# Punto 5. Mostrar y guardar los datos
EjecucionesPR1.guardar_usuario(usuario, contrasenya, email)

# Este paso extra 3 es solo si quieres usar el envío del email en ascii
# Paso extra 3. Método adicional para evitar caracteres no soportados por ascii (ñ, ¡, ¿) (por si dejas la configuración ascii en smtplib.py)
usuario_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(usuario)
contrasenya_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(contrasenya)
email_ascii = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(email)

# Punto 6 (opcional). Enviar correo con los datos
# OJO, tengo configurado smtplib.py como UTF-8 pero de normal viene como ASCII, si da problemas tienes que cambiar esto:
# External Libraries -> Python 3.8 -> Lib -> smtplib.py -> buscar: msg = _fix_eols(msg).encode('ascii') y cambiar ascii por UTF-8
EjecucionesPR1.preguntar_mandar_email(usuario, contrasenya, email)
print("Fin del programa, gracias por utilizar " + colorama.Fore.LIGHTCYAN_EX + "The Best Password Generator"
      + colorama.Fore.RESET + ".")