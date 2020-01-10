import datetime
import colorama

import Arch
import venv.Archiv
#from Archivos import Clases
#from Archivos import MainEjecuciones as ME
import MainEjecuciones as ME
import Clases


# Diccionarios para las opciones
opciones = {
    "1": ME.menu_empleados, "2": ME.menu_clientes, "3": ME.menu_actividades, "4": ME.menu_informes, "5":ME.menu_oportunidades, "6":ME.menu_graficas, "7": ME.menu_extras,
}
sub_opciones = {
    "1":(ME.opcion_nuevo_empleado,
         ME.opcion_nuevo_cliente,
         ME.opcion_nueva_actividad,
         ME.opcion_nuevo_informe,
         ME.opcion_nueva_oportunidad,
         ME.opcion_grafica_empleadosyclientes,
         ME.opcion_extra_tts),
    "2":(ME.opcion_modificar_empleado,
         ME.opcion_modificar_cliente,
         ME.opcion_modificar_actividad,
         ME.opcion_modificar_informe,
         ME.opcion_modificar_oportunidad,
         ME.grafico_por_meses,
         ME.opcion_extra_vtt),
    "3":(ME.opcion_borrar_empleado,
         ME.opcion_borrar_cliente,
         ME.opcion_borrar_actividad,
         ME.opcion_borrar_informe,
         ME.opcion_borrar_oportunidad,
         ME.wip,
         ME.opcion_extra_mibot) }
c = {
    "lc": colorama.Fore.LIGHTCYAN_EX,
    "lr": colorama.Fore.LIGHTRED_EX,
    "lm": colorama.Fore.LIGHTMAGENTA_EX,
    "ly": colorama.Fore.LIGHTYELLOW_EX,
    "r": colorama.Fore.RED,
    "rst": colorama.Style.RESET_ALL,
    "*": colorama.Style.BRIGHT }

# Pequeña introducción
print(c["lm"] + c["*"] + "Cómo funciona:" + c["rst"])
print(c["lc"] + "Los empleados y clientes participan en actividades.\n"
                "Informes: enlazan una actividad con los clientes y empleados que participen en ella.\n"
                "Oportunidad: engloban un conjunto de informes (actividades).\n" + c["rst"])

# Programa
opcion = ""
while opcion != "8":
    opcion = ME.menu_principal()
    print()
    if opcion in opciones or opcion == "8":
        if opcion == "8":
            print("Programa finalizado.")
        else:
            sub_opcion = opciones[opcion]()
            print()
            if sub_opcion in sub_opciones:
                opcion_int = int(opcion) - 1
                sub_opciones[sub_opcion][opcion_int]()
            else:
                print("{0}¡Ups!{1} Perdona, {2}no{3} te he entendido.".format(c["r"], c["rst"], c["r"], c["rst"]))
    else:
        print("{0}¡Ups!{1} Perdona, {2}no{3} te he entendido.".format(c["r"], c["rst"], c["r"], c["rst"]))
    print()




