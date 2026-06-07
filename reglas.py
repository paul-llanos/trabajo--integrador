from calculos import calculo_cuello_de_botella

def verificaion_de_credenciales(axuliar, nombre_admin_res, nombre_servidor, sistema_operativo, tipo_servidor):
    NOMBRE_ADMINISTRADOR = "admin"
    NOMBRE_SERVIDOR = "servidor"
    SISTEMA_OPERATIVO = "linux"
    TIPO_SERVIDOR = "base de datos"

    if nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR or sistema_operativo != SISTEMA_OPERATIVO or tipo_servidor != TIPO_SERVIDOR:
        print(f"\n==============================""\ncredenciales incorrectas!!!\nINTENTE NUEVAMENTE\n==============================")
    else:
        axuliar = False

    return axuliar

def verificacion_de_cpu(cpu_usada, contador):
    CPU_MAX = 85
    # Índice 0: riesgo, Índice 1: problema, Índice 2: recomendacion, Índice 3: contador
    resultado_cpu = ["", "", "", contador]

    if cpu_usada > CPU_MAX:
        resultado_cpu[0] = "critico"
        resultado_cpu[1] = "sobrecarga en CPU."
        resultado_cpu[2] = "optimizar el consumo del CPU."
        resultado_cpu[3] = contador + 1  # Sumamos aquí dentro

    return resultado_cpu


def verificacion_ram(ram_usada, contador):
    RAM_MAX = 85
    resultado_ram = ["", "", "", contador]

    if ram_usada > RAM_MAX:
        resultado_ram[0] = "critico"
        resultado_ram[1] = "sobrecarga en RAM."
        resultado_ram[2] = "optimizar el consumo de RAM."
        resultado_ram[3] = contador + 1  # Sumamos aquí dentro

    return resultado_ram


def verificacion_disco(espacio_disco, contador):
    DISCO_DISPONIBLE_MIN = 60
    resultado_disco = ["", "", "", contador]

    if espacio_disco < DISCO_DISPONIBLE_MIN:
        resultado_disco[0] = "critico"
        resultado_disco[1] = "EL ALMACENAMIENTO ESTA POR AGOTARSE."
        resultado_disco[2] = "Aumentar capacidad de almacenamiento o eliminar archivos."
        resultado_disco[3] = contador + 1  # Sumamos aquí dentro

    return resultado_disco


def verificacion_procesos(procesos_activos, contador):
    PROCESOS_MAX = 120
    resultado_procesos = ["", "", "", contador]

    if procesos_activos > PROCESOS_MAX:
        resultado_procesos[0] = "critico"
        resultado_procesos[1] = "sobrecarga en procesos."
        resultado_procesos[2] = "optimizar el consumo de procesos."
        resultado_procesos[3] = contador + 1  

    return resultado_procesos


def verificacion_usuarios(usuarios_conectados, contador):
    USUARIOS_MAX = 50
    resultado_usuarios = ["", "", "", contador]

    if usuarios_conectados > USUARIOS_MAX:
        resultado_usuarios[0] = "critico"
        resultado_usuarios[1] = "sobrecarga en usuarios."
        resultado_usuarios[2] = "optimizar el consumo de usuarios."
        resultado_usuarios[3] = contador + 1 

    return resultado_usuarios


def verificacion_firewall(estado_firewall, contador):
    resultado_firewall = ["", "", "", contador]

    if estado_firewall != "activo":
        resultado_firewall[0] = "critico"
        resultado_firewall[1] = "El firewall esta desactivado."
        resultado_firewall[
            2
        ] = "Activar el firewall y revisar el servidor por posibles amenazas."
        resultado_firewall[3] = contador + 1  

    return resultado_firewall

