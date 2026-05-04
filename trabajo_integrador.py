from funciones_de_validacion import validacion_numerico, validacion_porcentaje_numerico, validacion_datos_categoricos, validacion_cadena
"""VARIABLES CONTANTES"""
# variables de credenciales
NOMBRE_ADMINISTRADOR = "admin"
NOMBRE_SERVIDOR = "servidor"
SISTEMA_OPERATIVO = "linux"
TIPO_SERVIDOR = "base de datos"

# cpu ram
CPU_MAX = 85
RAM_MAX = 85
RAM_CPU_CUELLO_DE_BOTELLA = 40
# procesos y usuarios
PROCESOS_MAX = 120
USUARIO_MAX = 50
POSIBLE_ATAQUE = 40 
# disco
DISCO_DISPONIBLE_MIN = 60
# contante la cantidad de procesos que puedria llegar a tener un usuario
MAX_PROCESOS_POR_USER = 20

"""VARIABLES PARA LAS REGLAS"""
# variables de entrada
nombre_admin_res = ""
nombre_servidor = ""
cpu_usada = 0
ram_usada = 0
sistema_operativo = ""
tipo_servidor = ""
usuarios_conectados = 0
procesos_activos = 0
espacio_disco = 0
estado_firewall = ""

# cpu y ram
cpu_riesgo = ""
ram_riesgo = ""
problema_cpu = ""
problema_ram = ""
recomendacion_cpu = ""
recomendacion_ram = ""
# procesos y usuarios
procesos_riesgo = ""
usuarios_riesgo = ""
problema_procesos = ""
problema_usuarios = ""
recomendacion_procesos = ""
recomendacion_usuarios = ""
# disco
riesgo_disco = ""
problema_disco = ""
recomendacion_disco = ""
# firewall
riesgo_firewall = ""
problema_firewall = ""
recomendacion_firewall = ""

# VARIABLES DE CALCULO
cuello_de_botella = 0
intensidad_cpu_usuarios = 0
alerta = ""
contador = 0

while nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR or sistema_operativo != SISTEMA_OPERATIVO or tipo_servidor != TIPO_SERVIDOR:

    nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")
    while not validacion_cadena(nombre_admin_res):
        print(f"no puede dejar el dato en blanco")
        nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")

    nombre_servidor = input("Ingrese el nombre del servidor: ")
    while not validacion_cadena(nombre_servidor):
        print(f"no puede dejar el dato en blanco")
        nombre_servidor = input("Ingrese el nombre del servidor: ")

    sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")
    while not validacion_datos_categoricos(sistema_operativo, "so"):
        print(f"ingrese correctamente el dato")
        sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")
        
    tipo_servidor = input("Ingrese el tipo de servidor [web] [base de datos] [archivos]: ")
    while not validacion_datos_categoricos(tipo_servidor, "servidor"):
        print(f"ingrese correctamente el dato")
        tipo_servidor = input("Ingrese el tipo de servidor: ")

    if nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR or sistema_operativo != SISTEMA_OPERATIVO or tipo_servidor != TIPO_SERVIDOR:
        print(f"\ncredenciales incorrectas!!!\nINTENTE NUEVAMENTE\n")
    else:
        break

print(f"\nDATOS INGRESADOS CORRECTAMENTE:\n")
print(f"administrador: {nombre_admin_res}")
print(f"servidor: {nombre_servidor}\n")
print(f"BIENVENIDO AL SISTEMA DE [DIAGNOSTICO DE SERVIDORES]\n")

# preguntamos si queremos iniciar el diagnostico
iniciar_sistema = input("Desea iniciar el test? [si] / [no]: ")

if iniciar_sistema == "si":
#  cargamos los datos y se validan que sean correctos para el diagnostico
    cpu_usada = input("Ingrese el uso del CPU % : ")
    while not validacion_porcentaje_numerico(cpu_usada):
        print(f"ingrese correctamente su numero")
        cpu_usada = input("Ingrese el uso del CPU % : ")
    cpu_usada = int(cpu_usada)

    ram_usada = input("Ingrese el uso de de Memoria RAM % : ")
    while not validacion_porcentaje_numerico(ram_usada):
        print(f"ingrese correctamente su dato")
        ram_usada = input("Ingrese el uso de memoria RAM % : ")
    ram_usada = int(ram_usada)

    espacio_disco = input("Ingrese el espacio libre en disco [GB]: ")
    while not validacion_numerico(espacio_disco):
        print(f"ingrese correctamente su numero")
        espacio_disco = input("Ingrese el espacio libre en disco [GB] : ")
    espacio_disco = float(espacio_disco)

    usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")
    while not validacion_numerico(usuarios_conectados):
        print(f"ingrese correctamente el dato")
        usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")
    usuarios_conectados = int(usuarios_conectados)

    procesos_activos = input("Ingrese la cantidad de procesos activos: ")
    while not validacion_numerico(procesos_activos):
        print(f"ingrese correctamente el dato")
        procesos_activos = input("Ingrese la cantidad de procesos activos: ")
    procesos_activos = int(procesos_activos)

    estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")
    while not validacion_datos_categoricos(estado_firewall, "firewall"):
        print(f"ingrese correctamente el dato")
        estado_firewall = input("Ingrese una opcion [activo] [inactivo]: ")
# mostramos los datos ingresados
    print(f"\nDATOS INGRESADOS: \n")
    print(f"uso de cpu: {cpu_usada}% ")
    print(f"uso de ram: {ram_usada}% ")
    print(f"espacio libre en disco: {espacio_disco} GB")
    print(f"cantidad de usuarios conectados: {usuarios_conectados}")
    print(f"cantidad de procesos activos: {procesos_activos}")
    print(f"sistema operativo: {sistema_operativo}")
    print(f"estado del firewall: {estado_firewall}")

    # CALCULOS CPU
    if cpu_usada > CPU_MAX:
        cpu_riesgo = "critico"
        problema_cpu = "sobrecarga en CPU."
        recomendacion_cpu = "optimizar el consumo del CPU."
        contador = contador + 1

    # CALCULOS RAM
    if ram_usada > RAM_MAX:
        ram_riesgo = "critico"
        problema_ram = "sobrecarga en RAM."
        recomendacion_ram = "Reducir consumo de RAM."
        contador = contador + 1
    
    # CALCULOS PROCESOS
    if procesos_activos > PROCESOS_MAX:
        procesos_riesgo = "critico"
        problema_procesos = "sobrecarga de procesos"
        recomendacion_procesos = "eliminar los procesos inactivos."
        contador = contador + 1
 
    # CALCULOS USUARIOS
    if usuarios_conectados > USUARIO_MAX:
        usuarios_riesgo = "critico"
        problema_usuarios = "sobrecarga usuarios."
        recomendacion_usuarios = "eliminar usuarios inactivos."
        contador = contador + 1

    # CALCULO DISCO
    if espacio_disco < DISCO_DISPONIBLE_MIN:
        riesgo_disco = "critico"
        problema_disco = "EL ALMACENAMIENTO ESTA POR AGOTARSE"
        recomendacion_disco = "Aumentar capacidad de almacenamiento o eliminar archivos."
        contador = contador + 1
    
    # FIREWALL
    if not (estado_firewall == "activo"):
        riesgo_firewall = "critico"
        problema_firewall = "El firewall esta desactivado."
        recomendacion_firewall = "Activar el firewall y revisar el servidor por posibles amenazas."
        contador = contador + 1

#  CALCULAMOS  CUELLO DE BOTELLA DEL CPU Y RAM
    if cpu_usada > ram_usada:
        cuello_de_botella = cpu_usada - ram_usada
    else:
        cuello_de_botella = ram_usada - cpu_usada

    if cuello_de_botella > RAM_CPU_CUELLO_DE_BOTELLA:
        contador = contador + 1
        if cpu_usada > ram_usada:
            cpu_riesgo += "| CUIDADO"
            problema_cpu += f" |  CPU: {cpu_usada}% cuello de botella respecto a RAM: {ram_usada}% Diferencia de: {cuello_de_botella}% de uso)"
            recomendacion_cpu += " | COMPRE UNA MEJOR RAM"
        else:
            ram_riesgo += " | CUIDADO"
            problema_ram += f" | RAM: {ram_usada}% cuello de botella respecto a COU: {cpu_usada}% Diferencia de: {cuello_de_botella}%)"
            recomendacion_ram += " | COMPRE UN MEJOR CPU"
    # VERIFICAMOS POSIBLE AMENAZA PRO  EXCEDERSE CON EL USO CPU INDIVIDUAL
    if usuarios_conectados > 0:
        intensidad_cpu_usuarios = cpu_usada / usuarios_conectados
        if intensidad_cpu_usuarios > 45:
            contador = contador + 1
            problema_usuarios += f"ALERTA: Carga anómala. Cada usuario consume {intensidad_cpu_usuarios}% de CPU. Posible proceso colgado."
# VERIFICAMOS POSIBLE PROBLRMA DE RAM Y DISCO
    if ram_riesgo == "critico" and riesgo_disco == "critico":
        usuarios_riesgo += f" | cuidado tiene la ram {ram_usada} y a su disco le quedan menos de {espacio_disco} GB su servidor puede caer"

    # VERIFICO POSIBLE AMENA SI UN USUARIO TIENE MAS PROCESOS QUE LOS PERMITIDO
    if usuarios_conectados > 0:
        procesos_por_usuario = procesos_activos / usuarios_conectados
        if procesos_por_usuario > MAX_PROCESOS_POR_USER:
            contador = contador + 1
            usuarios_riesgo += " | CUIDADO"
            problema_usuarios += f" |  El usuario promedio tiene {procesos_por_usuario} procesos. Posible ataque cibernetico o fuga de hilos."

    # VERIFICO SI EL SERVIDOR ES DE TIPO BASE DE DATOS O ARCHIVOS Y EL FIREWALL ESTA INACTIVO
        if (tipo_servidor == "base de datos" or tipo_servidor == "archivos") and (estado_firewall == "inactivo" and sistema_operativo == "windows"):
            contador = contador + 1
            alerta += f"cuidado el servior de tipo: {tipo_servidor} esta vulnerable a ataques de {sistema_operativo}"
        
    
    if contador == 0:
        print(f"\n----------------------------------------------\n")
        print(f"\n SERVIDOR EN BUEN ESTADO \n")
    else:
        print(f"\n------------------------------")
        if contador < 3:
            print(f"  ATENCION: SERVIDOR FUERA DE LO NORMAL")
        elif contador < 5:
            print(f"  ATENCION: SERVIDOR EN ALERTA")
        else:
            print(f"  ATENCION: SERVIDOR EN ESTADO CRITICO")
        
        print(f"         DIAGNOSTICO DE SERVIDOR\n")
        print(f"\n------------------------------")

    # SOLO SE VAN A MOSTROS LOS RESULTADOS DE AQUELLOS QUE TIENEN RIESGO
        if cpu_riesgo != "" or "CUIDADO" in cpu_riesgo:
            print(f"\n[ CPU ]")
            print(f"Riesgo: {cpu_riesgo}")
            print(f"Problema: {problema_cpu}")
            print(f"Recomendación: {recomendacion_cpu}")

        
        if ram_riesgo != "" or "CUIDADO" in ram_riesgo:
            print(f"\n[ RAM ]")
            print(f"Riesgo: {ram_riesgo}")
            print(f"Problema: {problema_ram}")
            print(f"Recomendación: {recomendacion_ram}")

        
        if procesos_riesgo != "" or usuarios_riesgo != "" or "ALERTA" in problema_usuarios:
            print(f"\n------------------------------")
            print(f"[ PROCESOS Y USUARIOS ]")
            if procesos_riesgo != "":
                print(f"PROCESOS: {procesos_riesgo} | {problema_procesos}")
            if usuarios_riesgo != "" or "ALERTA" in problema_usuarios:
                print(f"USUARIOS: {usuarios_riesgo} | {problema_usuarios}")
            print(f"Recomendación: {recomendacion_procesos} / {recomendacion_usuarios}")

        
        if riesgo_disco != "":
            print(f"\n------------------------------")
            print(f"[ ALMACENAMIENTO ]")
            print(f"Riesgo: {riesgo_disco}")
            print(f"Problema: {problema_disco}")
            print(f"Recomendación: {recomendacion_disco}")

        
        if riesgo_firewall != "":
            print(f"\n------------------------------")
            print(f"[ SEGURIDAD - FIREWALL ]")
            print(f"Riesgo: {riesgo_firewall}")
            print(f"Problema: {problema_firewall}")
            print(f"Recomendación: {recomendacion_firewall}")

       
        if alerta != "":
            print(f"\n!!!!!!!!!!!!!!!!!")
            print(f"ALERTAS DEL SISTEMA: {alerta}")

else:
    print(f"\n Saliendo del sistema... ")