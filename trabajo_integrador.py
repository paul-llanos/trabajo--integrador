from funciones_de_validacion import validacion_numerico, validacion_porcentaje_numerico, validacion_datos_categoricos, validacion_cadena
NOMBRE_ADMINISTRADOR = "admin"
NOMBRE_SERVIDOR = "servidor"
SISTEMA_OPERATIVO = "linux"
TIPO_SERVIDOR = "base de datos"
CPU_CIRTICO = 95
CPU_ALTA = 75
RAM_CRITICA = 90
RAM_ALTA = 70
PROCESOS_CRITICOS = 150
PROCESOS_ALTOS = 110
USUARIO_MAXIMOS = 90
DISCO_LLENO = 60
DISCO_CRITICO = 20

porcentaje_total_carga = 0
riesgo_cpu_ram = ""
riesgo_procesos_usuarios = ""
riesgo_disco_firewall = ""
recomendacion_cpu_ram = ""
recomendacion_procesos_usuarios = ""
recomendacion_disco_firewall = ""
problema_ram_cpu = ""
problema_procesos_usuarios = ""
problema_disco_firewall = ""
estado_general_servidor = ""


nombre_admin_res = ""
nombre_servidor = ""
sistema_operativo = ""
tipo_servidor = ""

while nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR or sistema_operativo != SISTEMA_OPERATIVO or tipo_servidor != TIPO_SERVIDOR:

    nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")

    while not validacion_cadena(nombre_admin_res):
        print("no puede dejar el dato en blanco")
        nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")

    nombre_servidor = input("Ingrese el nombre del servidor: ")

    while not validacion_cadena(nombre_servidor):
        print("no puede dejar el dato en blanco")
        nombre_servidor = input("Ingrese el nombre del servidor: ")
    sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")

    while not validacion_datos_categoricos(sistema_operativo, "so"):
        print("ingrese correctamente el dato")
        sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")
        
    tipo_servidor = input("Ingrese el tipo de servidor [web] [base de datos] [archivos]: ")

    while not validacion_datos_categoricos(tipo_servidor, "servidor"):
        print("ingrese correctamente el dato")
        tipo_servidor = input("Ingrese el tipo de servidor: ")

    if nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR or sistema_operativo != SISTEMA_OPERATIVO or tipo_servidor != TIPO_SERVIDOR:
        print("\ncredenciales incorrectas!!!\nINTENTE NUEVAMENTE\n")
    else:
        break
    
print("\nDATOS INGRESADOS CORRECTAMENTE:\n")
print(f"administrador: {nombre_admin_res}")
print(f"servidor: {nombre_servidor}\n")
print("BIENVENIDO AL SISTEMA DE [MONITOR DE SERVIDORES]\n")
    
iniciar_sistema = input("Desea iniciar el sistema? [si] / [no]: ")
if iniciar_sistema == "si":

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


    estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")

    while not validacion_datos_categoricos(estado_firewall, "firewall"):
        print("ingrese correctamente el dato")
        estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")
        


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
   

   

    if cpu_usada > CPU_CIRTICO and ram_usada > RAM_CRITICA:
        riesgo_cpu_ram = "critico"
        problema_ram_cpu = "Sobrecarga en RAM y CPU."
        recomendacion_cpu_ram = "Reducir consumo de CPU y RAM o aumentar capacidad."

    elif cpu_usada > CPU_ALTA or ram_usada > RAM_ALTA:
        riesgo_cpu_ram = "medio"
        problema_ram_cpu = "Consumo elevado de recursos."
        recomendacion_cpu_ram = "Monitorear el uso de CPU y RAM."

    else:
        riesgo_cpu_ram = "ninguno"
        problema_ram_cpu = "El servidor se encuentra en buen estado."
        recomendacion_cpu_ram = "Mantener el servidor en estos valores."

    if procesos_activos > PROCESOS_CRITICOS and usuarios_conectados > USUARIO_MAXIMOS:
        riesgo_procesos_usuarios = "critica"
        problema_procesos_usuarios = "Demasiados procesos y usuarios conectados."
        recomendacion_procesos_usuarios = "Reducir la cantidad de procesos o limitar usuarios."

    elif procesos_activos > PROCESOS_ALTOS or usuarios_conectados > USUARIO_MAXIMOS:
        riesgo_procesos_usuarios = "medio"
        problema_procesos_usuarios = "Alta carga de procesos o usuarios."
        recomendacion_procesos_usuarios = "Monitorear el sistema y optimizar procesos."

    else:
        riesgo_procesos_usuarios = "normal"
        problema_procesos_usuarios = "El sistema funciona con carga normal."
        recomendacion_procesos_usuarios = "No se requieren acciones."
    if espacio_disco < DISCO_CRITICO:
        riesgo_disco = "critico"
        problema_disco = "Espacio de almacenamiento crítico"
        recomendacion_disco = "Liberar espacio inmediatamente"

    elif espacio_disco < DISCO_LLENO:
        riesgo_disco = "medio"
        problema_disco = "Espacio de almacenamiento reducido"
        recomendacion_disco = "Monitorear y liberar archivos"

    else:
        riesgo_disco = "normal"
        problema_disco = "El servidor se encuentra en buen estado."
        recomendacion_disco = "Mantener el servidor en estos valores."  

    if estado_firewall == "inactivo":
        riesgo_firewall = "critico"
        problema_firewall = "Posible ataque al sistema"
        recomendacion_firewall = "activar firewall y realizar un chequeo de seguridad inmediatamente"

    else:
        riesgo_firewall = "ninguno"
        problema_firewall = "El servidor se encuentra en buen estado."
        recomendacion_firewall = "Mantener el firewall activo."

    


    print("\n DIAGNOSTICO DE SERVIDOR \n")
    print("CPU y RAM:\n")
    print(f"riesgo: {riesgo_cpu_ram}")
    print(f"problema: {problema_ram_cpu}")
    print(f"recomendacion: {recomendacion_cpu_ram}")
    print("\n PROCESOS Y USUARIOS:\n")
    print(f"riesgo: {riesgo_procesos_usuarios}")
    print(f"problema: {problema_procesos_usuarios}")
    print(f"recomendacion: {recomendacion_procesos_usuarios}")
    print("\n ESPACIO DEL DISCO:\n")
    print(f"riesgo: {riesgo_disco}")
    print(f"problema: {problema_disco}")
    print(f"recomendacion: {recomendacion_disco}")
    print("\n FIREWALL:\n")
    print(f"riesgo: {riesgo_firewall}")
    print(f"problema: {problema_firewall}")
    print(f"recomendacion: {recomendacion_firewall}")

else:
    print(f"\n Saliendo del sistema...  ")

#     problemas_detectados = problema_ram_cpu + problema_procesos_usuarios + problema_disco + problema_firewall
#     recomendaciones = recomendacion_cpu_ram + recomendacion_procesos_usuarios + recomendacion_disco + recomendacion_firewall

# #     print(" PROBLEMAS DETECTADOS")
#     if problemas_detectados == "":
#         print("No se detectaron problemas")
#     else:
#         print(problemas_detectados)

#     print("\n--- RECOMENDACIONES ---")
#     if recomendaciones == "":
#         print("No se requieren acciones")
#     else:
#         print(recomendaciones)
# else:
#     print(f"\n Saliendo del sistema... ")




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

