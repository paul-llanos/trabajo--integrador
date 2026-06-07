def bienvenida_al_sistema():
    print("\nBIENVENIDO AL SISTEMA DE [ DIAGNOSTICO DE SERVIDORES ]\n------POR FAVOR INGRESE LOS DATOS DEL SU SERVIDOR--------\n")
    print(f"\n==============================")

def mostrar_exito_ingreso_de_datos(admin: str, servidor: str):
    """Confirma que el acceso fue otorgado con éxito."""
    print(f"\n==============================")
    print(f"✅ DATOS INGRESADOS CORRECTAMENTE")
    print(f"==============================")
    print(f"Administrador: {admin}")
    print(f"Servidor: {servidor}")
    print(f"==============================")
    print(f"BIENVENIDO AL SISTEMA DE [DIAGNOSTICO DE SERVIDORES]")
    print(f"==============================\n")



def salida_del_sistema():
    print(f"\n==============================")
    print(f"\nGracias por utilizar el sistema de diagnostico de servidores")
    print(f"\n Saliendo del sistema... ")
    print(f"\n==============================")

def mostrar_datos_ingresados(cpu_usada, ram_usada, espacio_disco, usuarios_conectados, procesos_activos, sistema_operativo, estado_firewall):
        print(f"\nDATOS INGRESADOS: \n")
        print(f"uso de cpu: {cpu_usada}% ")
        print(f"uso de ram: {ram_usada}% ")
        print(f"espacio libre en disco: {espacio_disco} GB")
        print(f"cantidad de usuarios conectados: {usuarios_conectados}")
        print(f"cantidad de procesos activos: {procesos_activos}")
        print(f"sistema operativo: {sistema_operativo}")
        print(f"estado del firewall: {estado_firewall}")