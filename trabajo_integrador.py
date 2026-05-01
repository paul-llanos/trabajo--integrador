# Datos numericos
cpu = float(input("Ingrese el uso del CPU: "))
ram = float(input("Ingrese el uso de de Memoria RAM: "))
gb = int(input("Ingrese el espacio libre en disco [GB]: "))
usuarios_conectados = int(input("Ingrese la cantidad de usuarios conectados: "))
procesos_activos = int(input("Ingrese la cantidad de procesos activos: "))

# Datos Categoricos
sis_operativo = input("Ingrese el Sistema Operativo: [Linux] [Windows]...")
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

