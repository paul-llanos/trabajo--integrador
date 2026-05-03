from funciones_de_validacion import validacion_numerico, validacion_porcentaje_numerico, validacion_datos_categoricos, validacion_cadena
NOMBRE_ADMINISTRADOR = "admin"
NOMBRE_SERVIDOR = "servidor"

nombre_admin_res = ""
nombre_servidor = ""

while nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR:

    nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")

    while not validacion_cadena(nombre_admin_res):
        print("no puede dejar el dato en blanco")
        nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")

    nombre_servidor = input("Ingrese el nombre del servidor: ")

    while not validacion_cadena(nombre_servidor):
        print("no puede dejar el dato en blanco")
        nombre_servidor = input("Ingrese el nombre del servidor: ")

    if nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR:
        print("\ncredenciales incorrectas!!!\nINTENTE NUEVAMENTE\n")

print("\nDATOS INGRESADOS CORRECTAMENTE:\n")
print(f"administrador: {nombre_admin_res}")
print(f"servidor: {nombre_servidor}\n")
print("BIENVENIDO AL SISTEMA DE [MONITOR DE SERVIDORES]\n")
    
iniciar_sistema = input("Desea iniciar el sistema? [si] / [no]: ")
if iniciar_sistema == "si":

      
    tipo_servidor = input("Ingrese el tipo de servidor [web] [base de datos] [archivos]: ")

    while not validacion_datos_categoricos(tipo_servidor, "servidor"):
        print("ingrese correctamente el dato")
        tipo_servidor = input("Ingrese el tipo de servidor: ")

    cpu_usada = input("Ingrese el uso del CPU % : ")
    while not validacion_porcentaje_numerico(cpu_usada):
        print("ingrese correctamente su numero")
        cpu_usada = input("Ingrese el uso del CPU % : ")
    else:
        cpu_usada = int(cpu_usada)


    ram_usada =  input("Ingrese el uso de de Memoria RAM % : ")


    while not validacion_porcentaje_numerico(ram_usada):
        print("ingrese correctamente su dato")
        ram_usada = input("Ingrese el uso de memoria RAM % : ")
    else:
        ram_usada = int(ram_usada)

    espacio_disco = input("Ingrese el espacio libre en disco [GB]: ")

    while not validacion_numerico(espacio_disco):
        print("ingrese correctamente su numero")
        espacio_disco = input("Ingrese el espacio libre en disco [GB] : ")   
    else:
        espacio_disco = float(espacio_disco)

    usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")

    while not validacion_numerico(usuarios_conectados):
        print("ingrese correctamente el dato")
        usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")
        
    else:
        usuarios_conectados = int(usuarios_conectados)

    procesos_activos = input("Ingrese la cantidad de procesos activos: ")

    while not validacion_numerico(procesos_activos):
        print("ingrese correctamente el dato")
        procesos_activos = input("Ingrese la cantidad de procesos activos: ")
        
    else:
        procesos_activos = int(procesos_activos)

    # Datos Categoricos
    sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")

    while not validacion_datos_categoricos(sistema_operativo, "so"):
        print("ingrese correctamente el dato")
        sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")

    estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")

    while not validacion_datos_categoricos(estado_firewall, "firewall"):
        print("ingrese correctamente el dato")
        estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")
        



    # Cadenas


    print("\n")
    print(f"DATOS INGRESADOS: \n")
    print(f"uso de cpu: {cpu_usada}% ")
    print(f"uso de ram: {ram_usada}% ")
    print(f"espacio libre en disco: {espacio_disco} GB")
    print(f"cantidad de usuarios conectados: {usuarios_conectados}")
    print(f"cantidad de procesos activos: {procesos_activos}")
    print(f"sistema operativo: {sistema_operativo}")
    print(f"estado del firewall: {estado_firewall}")
    print(f"tipo de servidor: {tipo_servidor}")
    print(f"nombre del servidor: {nombre_servidor}")
    print(f"nombre del Administrador responsable: {nombre_admin_res}")

    #  Nuevas variables
    porcentaje_total_carga = (cpu_usada + ram_usada) / 2

    if espacio_disco < 10 or procesos_activos > 250:
        recursos_disponibles = "Bajos"
    else:
        recursos_disponibles = "Suficientes"

    problemas_detectados = "" 
    recomendaciones = ""

    if cpu_usada > 85 and ram_usada > 80:
        problemas_detectados += "Sobrecarga."
        recomendaciones += "Reducir o aumetar recursos."
    if espacio_disco < 10 or procesos_activos > 250:
        problemas_detectados += "Sistema saturado"
        recomendaciones = "Liberar discos"
    if estado_firewall != "Activo":
        problemas_detectados += "Firewall Desactivado"
        recomendaciones += "Activar Firewall"
    if 40 <= cpu_usada <= 70 and 40 <= ram_usada <= 70:
        problemas_detectados += "La carga esta dentro de lo normal"
    if tipo_servidor == "web" and usuarios_conectados > 100 and cpu_usada > 75:
        problemas_detectados += "Alta demanda en el servidor [web]"
        recomendaciones += "Escalar recursos"
    if espacio_disco < 5 and cpu_usada > 70:
        problemas_detectados += "Hay poco espacio en disco"
        recomendaciones += "Ampliacion de almacenamiento"
    if procesos_activos > 300:
        problemas_detectados += "MUchos procesos activos"
        recomendaciones += "Optimizacion de procesos"
    if porcentaje_total_carga > 80:
        problemas_detectados += "Carga elevada"
        recomendaciones += "Revisar sistema" 

    #riesgo
    if cpu_usada > 85 or espacio_disco < 10 or estado_firewall != "activo":
        riesgo = "Alto"
    elif porcentaje_total_carga > 60:
        riesgo = "Medio"
    else:
        riesgo = "Bajo"


    if porcentaje_total_carga > 80:
        estado_general_servidor = "Critico"
    elif porcentaje_total_carga > 60:
        estado_general_servidor = "Moderadoo"
    else:
        estado_general_servidor = "Estable"

    print("Diagnostico sitema")
    print(f"Carga total: {porcentaje_total_carga}")
    print(f"estado general: {estado_general_servidor}")
    print(f"Nivel de riesgo: {riesgo}")
    print(f"Recursos: {recursos_disponibles}")

    print(" PROBLEMAS DETECTADOS")
    if problemas_detectados == "":
        print("No se detectaron problemas")
    else:
        print(problemas_detectados)

    print("\n--- RECOMENDACIONES ---")
    if recomendaciones == "":
        print("No se requieren acciones")
    else:
        print(recomendaciones)
else:
    print(f"\n Saliendo del sistema... ")




# porcetaje_total_carga = 0
# riesgo = 0
# recursos_disponibles = 0
# estado_general_servidor = 0

# promedio_carga = ( cpu + ram ) / 2
# porcentaje_total_carga = promedio_carga



# if cpu > 85 and ram > 80:
#     print("Sobre carga critica.")
# if gb < 10 or procesos_activos > 250:
#     print("Mantenimiento urgente.")
# if not (estado_firewall == "activo"):
#     print("Riesgo de seguridad.")
# if 40 <= cpu <= 70 and 40 <= ram <= 70:
#     print("Carga Normal.")
# if tipo_servidor == "web" and usuarios_conectados > 100 and cpu > 75:
#     print("Escalar recursos")

