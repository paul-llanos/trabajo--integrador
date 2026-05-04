from funciones_de_validacion import validacion_numerico, validacion_porcentaje_numerico, validacion_datos_categoricos, validacion_cadena

NOMBRE_ADMINISTRADOR = "admin"
NOMBRE_SERVIDOR = "servidor"
SISTEMA_OPERATIVO = "linux"
TIPO_SERVIDOR = "base de datos"

CPU_MAX = 85
RAM_MAX = 85
PROCESOS_MAX = 100
USUARIO_MAX = 50
DISCO_DISPONIBLE_MIN = 60

nombre_admin_res = ""
nombre_servidor = ""
sistema_operativo = ""
tipo_servidor = ""

cpu_riesgo = ""
ram_riesgo = ""
problema_cpu = ""
problema_ram = ""
recomendacion_cpu = ""
recomendacion_ram = ""

riesgo_disco = ""
problema_disco = ""
recomendacion_disco = ""

procesos_riesgo = ""
problema_procesos = ""
recomendacion_procesos = ""

usuarios_riesgo = ""
problema_usuarios = ""
recomendacion_usuarios = ""

riesgo_firewall = ""
problema_firewall = ""
recomendacion_firewall = ""

estado_general_servidor = ""


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
print("BIENVENIDO AL SISTEMA DE [DIAGNOSTICO DE SERVIDORES]\n")
    

iniciar_sistema = input("Desea iniciar el test? [si] / [no]: ")

if iniciar_sistema == "si":
# Ingreso y validacio de datos del servidor
    cpu_usada = input("Ingrese el uso del CPU % : ")
    while not validacion_porcentaje_numerico(cpu_usada):
        print("ingrese correctamente su numero")
        cpu_usada = input("Ingrese el uso del CPU % : ")
    cpu_usada = int(cpu_usada)


    ram_usada = input("Ingrese el uso de de Memoria RAM % : ")
    while not validacion_porcentaje_numerico(ram_usada):
        print("ingrese correctamente su dato")
        ram_usada = input("Ingrese el uso de memoria RAM % : ")
    ram_usada = int(ram_usada)


    espacio_disco = input("Ingrese el espacio libre en disco [GB]: ")
    while not validacion_numerico(espacio_disco):
        print("ingrese correctamente su numero")
        espacio_disco = input("Ingrese el espacio libre en disco [GB] : ")
    espacio_disco = float(espacio_disco)


    usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")
    while not validacion_numerico(usuarios_conectados):
        print("ingrese correctamente el dato")
        usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")
    usuarios_conectados = int(usuarios_conectados)


    procesos_activos = input("Ingrese la cantidad de procesos activos: ")
    while not validacion_numerico(procesos_activos):
        print("ingrese correctamente el dato")
        procesos_activos = input("Ingrese la cantidad de procesos activos: ")
    procesos_activos = int(procesos_activos)


    estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")
    while not validacion_datos_categoricos(estado_firewall, "firewall"):
        print("ingrese correctamente el dato")
        estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")


    print("\nDATOS INGRESADOS: \n")
    print(f"uso de cpu: {cpu_usada}% ")
    print(f"uso de ram: {ram_usada}% ")
    print(f"espacio libre en disco: {espacio_disco} GB")
    print(f"cantidad de usuarios conectados: {usuarios_conectados}")
    print(f"cantidad de procesos activos: {procesos_activos}")
    print(f"sistema operativo: {sistema_operativo}")
    print(f"estado del firewall: {estado_firewall}")


    # CPU
    if cpu_usada > CPU_MAX:
        cpu_riesgo = "critico"
        problema_cpu = "sobrecarga en CPU."
        recomendacion_cpu = "Reducir consumo de CPU o aumentar capacidad."
    else:
        cpu_riesgo = "ninguno"
        problema_cpu = "ninguno."
        recomendacion_cpu = "ninguno."


    # RAM
    if ram_usada > RAM_MAX:
        ram_riesgo = "critico"
        problema_ram = "sobrecarga en RAM."
        recomendacion_ram = "Reducir consumo de RAM o aumentar capacidad."
    else:
        ram_riesgo = "ninguno"
        problema_ram = "ninguno."
        recomendacion_ram = "ninguno."


    # PROCESOS
    if procesos_activos > PROCESOS_MAX:
        procesos_riesgo = "critico"
        problema_procesos = "sobrecarga de procesos"
        recomendacion_procesos = "eliminar los procesos inactivos."
    else:
        procesos_riesgo = "ninguno"
        problema_procesos = "ninguno."
        recomendacion_procesos = "ninguno."


    # USUARIOS
    if usuarios_conectados > USUARIO_MAX:
        usuarios_riesgo = "critico"
        problema_usuarios = "sobrecarga usuarios."
        recomendacion_usuarios = "eliminar usuarios inactivos."
    else:
        usuarios_riesgo = "ninguno"
        problema_usuarios = "ninguno."
        recomendacion_usuarios = "ninguno."


    # DISCO
    if espacio_disco < DISCO_DISPONIBLE_MIN:
        riesgo_disco = "critico"
        problema_disco = "EL ALMACENAMIENTO ESTA POR AGOTARSE"
        recomendacion_disco = "Aumentar capacidad de almacenamiento o eliminar archivos."
    else:
        riesgo_disco = "ninguno"
        problema_disco = "ninguno."
        recomendacion_disco = "ninguno."


    # FIREWALL
    if not (estado_firewall == "activo"):
        riesgo_firewall = "critico"
        problema_firewall = "El firewall esta desactivado."
        recomendacion_firewall = "Activar el firewall y revisar el servidor por posibles amenazas."
    else:
        riesgo_firewall = "ninguno"
        problema_firewall = "nignuno."
        recomendacion_firewall = "ninguno."


    # REGLA DE 3 VARIABLES PARA SERVIDOR DE BASE DE DATOS
    if sistema_operativo == "linux" and tipo_servidor == "base de datos" and (cpu_riesgo == "critico" or ram_riesgo == "critico" or procesos_riesgo == "critico" or usuarios_riesgo == "critico" or riesgo_disco == "critico" or riesgo_firewall == "critico"):
        estado_general_servidor = True
    else:
        estado_general_servidor = False    
    
    if estado_general_servidor == False:

        print("\n----------------------------------------------\n")
        print("\n ESTADO GENERAL DEL SERVIDOR \n")
        print("\n----------------------------------------------\n")
        print("EL SERVIDOR SE ENCUENTRA EN BUEN ESTADO GENERAL.")
        print(f"{cpu_usada}% CPU NORMAL\n{ram_usada}% RAM NORMAL\n")
        print(f"{procesos_activos} PROCESOS ACTIVOS: NORMAL\n{usuarios_conectados} USUARIOS CONECTADOS NORMAL\n")
        print(f"{espacio_disco} GB DISCO NORMAL\n{estado_firewall} FIREWALL(antivirus) NORMAL\n")
    else:
        print("\n----------------------------------------------\n")
        print("\n Hay problemas en el servidor \n por favor reviso el diagnostico: para determinar la fuente del problema y siga las RECOMENDACIONES \n")
        print("\n----------------------------------------------\n")
        print("\n DIAGNOSTICO DE SERVIDOR \n")
        print("CPU y RAM:\n")
        print(f"CPU Riesgo: {cpu_riesgo}\nCPU Problema: {problema_cpu}\nCPU Recomendacion: {recomendacion_cpu}\n")
        print(f"RAM Riesgo: {ram_riesgo}\nRAM Problema: {problema_ram}\nRAM Recomendacion: {recomendacion_ram}\n")

        print("\n----------------------------------------------\n")
        print("Procesos y Usuarios:\n")
        print(f"PROCESOS Riesgo: {procesos_riesgo}\nPROCESOS Problema: {problema_procesos}\nPROCESOS Recomendacion: {recomendacion_procesos}\n")
        print(f"USUARIOS Riesgo: {usuarios_riesgo}\nUSUARIOS Problema: {problema_usuarios}\nUSUARIOS Recomendacion: {recomendacion_usuarios}\n")

        print("\n----------------------------------------------\n")
        print("Almacenamiento:\n")
        print(f"Riesgo: {riesgo_disco}\nProblema: {problema_disco}\nRecomendacion: {recomendacion_disco}\n")

        print("\n----------------------------------------------\n")
        print("Firewall:\n")
        print(f"Riesgo: {riesgo_firewall}\nProblema: {problema_firewall}\nRecomendacion: {recomendacion_firewall}\n")

        print("\n----------------------------------------------\n")
        print("ESTADO GENERAL DEL SERVIDOR:\n")
        print(f"{estado_general_servidor}\n")

else:
    print("\n Saliendo del sistema... ")





