from calculos import calculo_cuello_de_botella, calculo_intensidad_cpu_usuarios, calculo_de_cantidad_de_procesos_por_usuarios

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

def verificacion_de_cpu(cpu_usada):
    CPU_MAX = 85
    # Índice 0: riesgo, Índice 1: problema, Índice 2: recomendacion, Índice 3: contador
    resultado_cpu = ["", "", "", 0]

    if cpu_usada > CPU_MAX:
        resultado_cpu[0] = "critico"
        resultado_cpu[1] = "sobrecarga en CPU."
        resultado_cpu[2] = "optimizar el consumo del CPU."
        resultado_cpu[3] = resultado_cpu[3] + 1  # Sumamos aquí dentro

    return resultado_cpu


def verificacion_ram(ram_usada):
    RAM_MAX = 85
    resultado_ram = ["", "", "", 0]

    if ram_usada > RAM_MAX:
        resultado_ram[0] = "critico"
        resultado_ram[1] = "sobrecarga en RAM."
        resultado_ram[2] = "optimizar el consumo de RAM."
        resultado_ram[3] = resultado_ram[3] + 1  # Sumamos aquí dentro

    return resultado_ram


def verificacion_disco(espacio_disco):
    ESPACIO_DISCO_MINIMO = 60
    resultado_disco = ["", "", "", 0]

    if espacio_disco < ESPACIO_DISCO_MINIMO:
        resultado_disco[0] = "critico"
        resultado_disco[1] = "EL ALMACENAMIENTO ESTA POR AGOTARSE."
        resultado_disco[2] = "Aumentar capacidad de almacenamiento o eliminar archivos."
        resultado_disco[3] = resultado_disco[3] + 1  # Sumamos aquí dentro

    return resultado_disco


def verificacion_procesos(procesos_activos):
    PROCESOS_MAX = 120
    resultado_procesos = ["", "", "", 0]

    if procesos_activos > PROCESOS_MAX:
        resultado_procesos[0] = "critico"
        resultado_procesos[1] = "sobrecarga en procesos."
        resultado_procesos[2] = "optimizar el consumo de procesos."
        resultado_procesos[3] = resultado_procesos[3] + 1  

    return resultado_procesos


def verificacion_usuarios(usuarios_conectados):
    USUARIOS_MAX = 50
    resultado_usuarios = ["", "", "", 0]

    if usuarios_conectados > USUARIOS_MAX:
        resultado_usuarios[0] = "critico"
        resultado_usuarios[1] = "sobrecarga en usuarios."
        resultado_usuarios[2] = "optimizar el consumo de usuarios."
        resultado_usuarios[3] = resultado_usuarios[3] + 1 

    return resultado_usuarios


def verificacion_firewall(estado_firewall):
    diagnostico_firewall = ["", "", "", 0]

    if estado_firewall != "activo":
        diagnostico_firewall[0] = "inactivo"
        diagnostico_firewall[1] = "el sistema esta desprotegido."
        diagnostico_firewall[2] = "Activar el firewall y revisar el servidor por posibles amenazas."
        diagnostico_firewall[3] = diagnostico_firewall[3] + 1  

    return diagnostico_firewall

def verificaciion_de_cuello_de_botella (cpu_usada, ram_usada, diagnostico_cpu, diagnostico_ram):
    RAM_CPU_CUELLO_DE_BOTELLA = 50
    cuello_de_botella = calculo_cuello_de_botella(cpu_usada, ram_usada)
    if cuello_de_botella > RAM_CPU_CUELLO_DE_BOTELLA:
        if cpu_usada < ram_usada:
            diagnostico_ram[0] = diagnostico_ram[0] + f" | CUIDADO"
            diagnostico_ram[1] = diagnostico_ram[1] + f" | RAM: {ram_usada}% cuello de botella respecto a CPU: {cpu_usada}% Diferencia de: {cuello_de_botella}%)"
            diagnostico_ram[2] = diagnostico_ram[2] + f" | COMPRE UN MEJOR CPU"
            diagnostico_ram[3] = diagnostico_ram[3] + 1
            
        else:
            diagnostico_cpu[0] = diagnostico_cpu[0] + f" | CUIDADO"
            diagnostico_cpu[1] = diagnostico_cpu[1] + f" |  CPU: {cpu_usada}% tiene un cuello de botella respecto a la RAM: {ram_usada}% La diferencia es de: {cuello_de_botella}% de uso)"
            diagnostico_cpu[2] = diagnostico_cpu[2] + f" | COMPRE UNA MEJOR RAM"
            diagnostico_cpu[3] = diagnostico_cpu[3] + 1
            
def verificacion_de_intensidad_de_cpu_por_usario(cpu_usada, usuarios_conectados, diagnostico_usuarios):
    intensidad_cpu_usuarios = calculo_intensidad_cpu_usuarios(cpu_usada, usuarios_conectados)
    CANTIDAD_MAXIMA_DE_CPU_POR_USUARIO = 40
    if intensidad_cpu_usuarios > CANTIDAD_MAXIMA_DE_CPU_POR_USUARIO:
        diagnostico_usuarios[0] = diagnostico_usuarios[0] + f" | CUIDADO"
        diagnostico_usuarios[1] = diagnostico_usuarios[1] + f" | Carga anormal. Cada usuario consume {intensidad_cpu_usuarios}% de CPU. Sospecha de ataque cibernetico."
        diagnostico_usuarios[2] = diagnostico_usuarios[2] + f" | investigue a ese usuario."
        diagnostico_usuarios[3] = diagnostico_usuarios[3] + 1

def verificacion_de_estado_critico_en_ram_y_disco(ram_usada, espacio_disco, diagnostico_ram, diagnostico_disco):
    # Verificamos si en la posición 0 de ambas listas ya se guardó "critico"
    
    if diagnostico_ram[0] == "critico" and diagnostico_disco[0] == "critico":
        
        # 1. Sumamos 1 al contador de cada lista (posición 3)
        diagnostico_ram[3] = diagnostico_ram[3] + 1
        diagnostico_disco[3] = diagnostico_disco[3] + 1
        
        # 2. Concatenamos las alertas usando f-strings en los casilleros correspondientes
        diagnostico_ram[0] = diagnostico_ram[0] + f" | CUIDADO"
        diagnostico_disco[0] = diagnostico_disco[0] + f" | CUIDADO"
        
        diagnostico_ram[1] = diagnostico_ram[1] + f" | cuidado tiene la ram {ram_usada}% y a su disco le quedan menos de {espacio_disco} GB su servidor puede caer"
        diagnostico_disco[1] = diagnostico_disco[1] +  f" | cuidado tiene el disco {espacio_disco} GB y a su ram {ram_usada}% su servidor puede colapsar"
        
        diagnostico_ram[2] = diagnostico_ram[2] + f" | Limite el consumo de ram por usuario."
        diagnostico_disco[2] = diagnostico_disco[2] + f" | elimine archivos temporales del usuario."

def verificacion_de_cantidad_de_procesos_por_usuario(usuarios_conectados, procesos_activos, diagnostico_procesos):
    MAXIMOS_PROCESOS_POR_USUARIO = 20
    procesos_por_usuario = calculo_de_cantidad_de_procesos_por_usuarios(usuarios_conectados, procesos_activos)
    if procesos_por_usuario > MAXIMOS_PROCESOS_POR_USUARIO:
        diagnostico_procesos[0] = diagnostico_procesos[0] + f" | CUIDADO"
        diagnostico_procesos[1] = diagnostico_procesos[1] + f" | El promedio de PROCESOS de cada usuario es {procesos_por_usuario} . Posible ataque cibernetico o fuga de hilos"
        diagnostico_procesos[2] = diagnostico_procesos[2] + f" | Haga una verificacion del servidor para estar seguro."
        diagnostico_procesos[3] = diagnostico_procesos[3] + 1

def verificacion_de_vulnerabilidad(tipo_servidor, estado_firewall, sistema_operativo):
    diagnostico_seguridad = ["", "", "", 0]
    if (tipo_servidor == "base de datos" or tipo_servidor == "archivos") and (estado_firewall == "inactivo" and sistema_operativo == "linux"):
        
        diagnostico_seguridad[0] = f"EL SERIVODR SE ENCUNETRA EN ESTADO CRÍTICO!!!"
        diagnostico_seguridad[1] = f"cuidado el servidor de tipo: {tipo_servidor} esta vulnerable a ataques en este sistema operativo {sistema_operativo} por tener el firewall inactivo."
        diagnostico_seguridad[2] = "Active el firewall perimetral de manera urgente  ."
        diagnostico_seguridad[3] = diagnostico_seguridad[3] + 1
    return diagnostico_seguridad