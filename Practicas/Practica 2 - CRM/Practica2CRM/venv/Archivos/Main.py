import datetime
import Clases
import Archivos.MainEjecuciones as ME
import colorama

# Diccionarios para las opciones
opciones = {
    "1": ME.menu_empleados, "2": ME.menu_clientes, "3": ME.menu_actividades, "4": ME.menu_informes, "5": ME.menu_extras,
}
sub_opciones_informe = {
    "1":ME.wip,
    "2":ME.wip,
    "3":ME.wip,
    "4":ME.wip }
sub_opciones = {
    "1":(ME.opcion_nuevo_empleado, ME.opcion_nuevo_cliente, ME.opcion_nueva_actividad, ME.pasar, ME.wip),
    "2":(ME.opcion_modificar_empleado, ME.opcion_modificar_cliente, ME.opcion_modificar_actividad, ME.pasar, ME.wip),
    "3":(ME.opcion_borrar_empleado, ME.opcion_borrar_cliente, ME.opcion_borrar_actividad, ME.pasar, ME.wip) }
c = {
    "lc": colorama.Fore.LIGHTCYAN_EX,
    "lr": colorama.Fore.LIGHTRED_EX,
    "lm": colorama.Fore.LIGHTMAGENTA_EX,
    "ly": colorama.Fore.LIGHTYELLOW_EX,
    "r": colorama.Fore.RED,
    "rst": colorama.Style.RESET_ALL,
    "*": colorama.Style.BRIGHT }

opcion = ""
while opcion != "6":
    opcion = ME.menu_principal()
    print()
    if opcion in opciones or opcion == "6":
        if opcion == "6":
            print("Programa finalizado.")
        elif opcion == "4":
            sub_opcion = opciones[opcion]()
            print()
            if sub_opcion in sub_opciones_informe:
                opcion_int = int(opcion) - 1
                sub_opciones_informe[sub_opcion]()
            else:
                print("{0}¡Ups!{1} Perdona, {2}no{3} te he entendido.".format(c["r"], c["rst"], c["r"], c["rst"]))
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




