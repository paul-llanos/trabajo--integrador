from funciones_de_validacion import validacion_numerico, validacion_porcentaje_numerico

cpu_usada = input("Ingrese el uso del CPU: ")
while not validacion_porcentaje_numerico(cpu_usada):
    print("ingrese correctamente su numero")
    cpu_usada = input("Ingrese el uso del CPU: ")
else:
    cpu_usada = int(cpu_usada)


ram_usada =  input("Ingrese el uso de de Memoria RAM % : ")


while not validacion_porcentaje_numerico(ram_usada):
    print("ingrese correctamente su numero")
    ram_usada = input("Ingrese el uso de memoria RAM % : ")
    
else:
    ram_usada = int(ram_usada)

espacio_disco = input("Ingrese el espacio libre en disco [GB]: ")

while not validacion_numerico(espacio_disco):
    print("ingrese correctamente su numero")
    espacio_disco = input("Ingrese el espacio libre en disco [GB] : ")
    
else:
    espacio_disco = int(espacio_disco)

usuarios_conectados = int(input("Ingrese la cantidad de usuarios conectados: "))

while not validacion_numerico(espacio_disco):
    print("ingrese correctamente la cantidad de usuarios conectados")
    espacio_disco = input("Ingrese la cantidad de usuarios conectados: ")
    
else:
    usuarios_conectados = int(usuarios_conectados)

procesos_activos = int(input("Ingrese la cantidad de procesos activos: "))

while not validacion_numerico(procesos_activos):
    print("ingrese correctamente la cantidad de procesos activos")
    procesos_activos = input("Ingrese la cantidad de procesos activos: ")
    
else:
    procesos_activos = int(procesos_activos)

# Datos Categoricos
sistema_operativo = input("Ingrese el Sistema Operativo: [Linux] [Windows]...")
estado_firewall = input("Ingrese una opcion [Activo] [Inactivo] : ")
tipo_servidor = input("Ingrese el tipo de servidor [web] [Base de datos] [Archivos] : ")

# Cadenas
nombre_servidor = input("Ingrese el nombre del servidor: ")
nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")
# Nuevas variables
porcetaje_total_carga = 0
riesgo = 0
recursos_disponibles = 0
estado_general_servidor = 0

promedio_carga = ( cpu + ram ) / 2
porcentaje_total_carga = promedio_carga



if cpu > 85 and ram > 80:
    print("Sobre carga critica.")
if gb < 10 or procesos_activos > 250:
    print("Mantenimiento urgente.")
if not (estado_firewall == "activo"):
    print("Riesgo de seguridad.")
if 40 <= cpu <= 70 and 40 <= ram <= 70:
    print("Carga Normal.")
if tipo_servidor == "web" and usuarios_conectados > 100 and cpu > 75:
    print("Escalar recursos")

