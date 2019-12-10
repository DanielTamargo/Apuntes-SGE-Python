import colorama
import FuncionesPR1
import EjecucionesPR1
import smtplib
import ssl

# Uso pruebas.py para ir probando diversas partes del código

# en este caso, aunque tengo smtplib configurado como UTF-8, transformo las cadenas que ascii no soportaría a codificación tipo ascii
# (simplemente hice ese método por utilizar el replace)
email = "danieltamargosaiz@gmail.com"
usuario = "begoññññña"
contrasenya = "¡¡¡¡¡¡ññññññ¿¿¿"

cadena = "ñ ¿ ¡ ¡ ¿ ñ"
print("Cadena antes de convertir: " + cadena)
cadena = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(cadena)
print("Cadena después de convertir: " + cadena)

usuario = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(usuario)
contrasenya = EjecucionesPR1.evitar_caracteres_no_soportados_por_ascii(contrasenya)

EjecucionesPR1.enviar_email(usuario, contrasenya, email)