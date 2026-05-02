from funciones_de_validacion import validacion_numerico, validacion_porcentaje_numerico, validacion_datos_categoricos, validacion_cadena

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
    
tipo_servidor = input("Ingrese el tipo de servidor [web] [base de datos] [archivos]: ")

while not validacion_datos_categoricos(tipo_servidor, "servidor"):
    print("ingrese correctamente el dato")
    tipo_servidor = input("Ingrese el tipo de servidor: ")

# Cadenas
nombre_servidor = input("Ingrese el nombre del servidor: ")

while not (validacion_cadena(nombre_servidor)):
    print("no puede dejar el dato en blanco")
    nombre_servidor = input("Ingrese el nombre del servidor: ")

nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")

while not (validacion_cadena(nombre_admin_res)):
    print("no puede dejar el dato en blanco")
    nombre_admin_res = input("Ingrese el el nombre del Administrador responsable: ")
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

# # Nuevas variables

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

