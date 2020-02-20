import csv

# Función para crear los logs
def generarLog(usuario):
    print("Generar log")
    # Preparamos la línea
    campos = ['']

    with open('Datos/user_logs.csv') as f:
        writer = csv.writer(f)
        writer.writerows()