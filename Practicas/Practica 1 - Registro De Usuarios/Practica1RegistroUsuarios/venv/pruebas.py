import colorama
import FuncionesPR1
import EjecucionesPR1
import smtplib
import ssl

print("Fin del programa, gracias por utilizar " + colorama.Fore.LIGHTCYAN_EX + "The Best Password Generator"
      + colorama.Fore.RESET + ".")

email = "danieltamargosaiz@gmail.com"
usuario = "dani"
contrasenya = "!?=_-+*^'¡"

cadena = "unoñdos¡tres¿"
cadena = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(cadena)

EjecucionesPR1.enviar_email(usuario, contrasenya, email)