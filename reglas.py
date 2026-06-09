from calculos import calculo_cuello_de_botella, calculo_intensidad_cpu_usuarios, calculo_de_cantidad_de_procesos_por_usuarios

def verificaion_de_credenciales(axuliar: bool, nombre_admin_res: str, nombre_servidor: str, sistema_operativo: str, tipo_servidor: str) -> bool: 
    
    """Verifica si las credenciales coinciden con el entorno predefinido.

    Args:
        axuliar (bool): Bandera de control para el bucle del menú.
        nombre_admin_res (str): Nombre del administrador responsable.
        nombre_servidor (str): Nombre del servidor a diagnosticar.
        sistema_operativo (str): Sistema operativo del entorno.
        tipo_servidor (str): Rol o tipo de servidor.

    Returns:
        bool: Retorna False si son correctas, True de lo contrario.
   
     """
    NOMBRE_ADMINISTRADOR = "admin"
    NOMBRE_SERVIDOR = "servidor"
    SISTEMA_OPERATIVO = "linux"
    TIPO_SERVIDOR = "base de datos"

    if nombre_admin_res != NOMBRE_ADMINISTRADOR or nombre_servidor != NOMBRE_SERVIDOR or sistema_operativo != SISTEMA_OPERATIVO or tipo_servidor != TIPO_SERVIDOR:
        print(f"\n==============================""\ncredenciales incorrectas!!!\nINTENTE NUEVAMENTE\n==============================")
    else:
        axuliar = False

    return axuliar

def verificacion_de_cpu(cpu_usada: int) -> list:

    """
    Evalúa el porcentaje de uso de la CPU y determina si supera el límite crítico establecido.
    
    Args:
        cpu_usada (int): Porcentaje de uso actual de la CPU (1-100).
        
    Returns:
        list: Estructura indexada [riesgo, problema, recomendación, contador_alertas].
    """
    
    CPU_MAX = 85
    resultado_cpu = ["", "", "", 0]

    if cpu_usada > CPU_MAX:
        resultado_cpu[0] = "critico"
        resultado_cpu[1] = "sobrecarga en CPU."
        resultado_cpu[2] = "optimizar el consumo del CPU."
        resultado_cpu[3] = resultado_cpu[3] + 1  # sumamamos el contador de riesgo en la posicion 3

    return resultado_cpu


def verificacion_ram(ram_usada: int) -> list:

    """
    Evalúa el porcentaje de uso de la memoria RAM para identificar saturaciones.
    
    Args:
        ram_usada (int): Porcentaje de uso actual de la memoria RAM (1-100).
        
    Returns:
        list: Estructura indexada [riesgo, problema, recomendación, contador_alertas].
    """

    RAM_MAX = 85
    resultado_ram = ["", "", "", 0]

    if ram_usada > RAM_MAX:
        resultado_ram[0] = "critico"
        resultado_ram[1] = "sobrecarga en RAM."
        resultado_ram[2] = "optimizar el consumo de RAM."
        resultado_ram[3] = resultado_ram[3] + 1  

    return resultado_ram


def verificacion_disco(espacio_disco: float) -> list:

    """
    Evalúa los Gigabytes disponibles en el disco rígido para prevenir pérdidas de servicio.
    
    Args:
        espacio_disco (float): Espacio libre en disco medido en GB.
        
    Returns:
        list: Estructura indexada [riesgo, problema, recomendación, contador_alertas].
    """

    ESPACIO_DISCO_MINIMO = 60
    resultado_disco = ["", "", "", 0]

    if espacio_disco < ESPACIO_DISCO_MINIMO:
        resultado_disco[0] = "critico"
        resultado_disco[1] = "EL ALMACENAMIENTO ESTA POR AGOTARSE."
        resultado_disco[2] = "Aumentar capacidad de almacenamiento o eliminar archivos."
        resultado_disco[3] = resultado_disco[3] + 1  

    return resultado_disco


def verificacion_procesos(procesos_activos: int) -> list:

    """
    Monitorea la cantidad total de procesos  y verifica si hay sobrecarga en ejecución simultánea.
    
    Args:
        procesos_activos (int): Cantidad de procesos activos concurrentes.
        
    Returns:
        list: Estructura indexada [riesgo, problema, recomendación, contador_alertas].
    """

    PROCESOS_MAX = 120
    resultado_procesos = ["", "", "", 0]

    if procesos_activos > PROCESOS_MAX:
        resultado_procesos[0] = "critico"
        resultado_procesos[1] = "sobrecarga en procesos."
        resultado_procesos[2] = "optimizar el consumo de procesos."
        resultado_procesos[3] = resultado_procesos[3] + 1  

    return resultado_procesos


def verificacion_usuarios(usuarios_conectados: int) -> list:
    """
    Verifica si la cantidad de usuarios conectados supera el límite
    máximo permitido por el sistema.

    Args:
        usuarios_conectados (int): Cantidad de usuarios conectados.

    Returns:
        list: Resultado del diagnóstico con el formato
        [riesgo, problema, recomendacion, contador_alertas].
    """
    USUARIOS_MAX = 50
    resultado_usuarios = ["", "", "", 0]

    if usuarios_conectados > USUARIOS_MAX:
        resultado_usuarios[0] = "critico"
        resultado_usuarios[1] = "sobrecarga en usuarios."
        resultado_usuarios[2] = "optimizar el consumo de usuarios."
        resultado_usuarios[3] = resultado_usuarios[3] + 1 

    return resultado_usuarios


def verificacion_firewall(estado_firewall: str) -> list:
    """
    Verifica si el firewall del servidor se encuentra activo.

    Args:
        estado_firewall (str): Estado actual del firewall. Los valores
        esperados son "activo" o "inactivo".

    Returns:
        list: Resultado del diagnóstico con el formato
        [riesgo, problema, recomendacion, contador_alertas].
    """
    diagnostico_firewall = ["", "", "", 0]

    if estado_firewall != "activo":
        diagnostico_firewall[0] = "inactivo"
        diagnostico_firewall[1] = "el sistema esta desprotegido."
        diagnostico_firewall[2] = "Activar el firewall y revisar el servidor por posibles amenazas."
        diagnostico_firewall[3] = diagnostico_firewall[3] + 1  

    return diagnostico_firewall

def verificaciion_de_cuello_de_botella (cpu_usada: int, ram_usada: int  , diagnostico_cpu: list, diagnostico_ram: list) -> None:
    """
    Verifica si existe un cuello de botella significativo entre
    el uso de CPU y RAM, y actualiza el diagnóstico correspondiente.

    Se considera cuello de botella cuando la diferencia entre el
    porcentaje de uso de CPU y RAM supera el umbral establecido.

    Args:
        cpu_usada (int): Porcentaje de uso de la CPU.
        ram_usada (int): Porcentaje de uso de la memoria RAM.
        diagnostico_cpu (list): Diagnóstico actual de la CPU con el formato
            [riesgo, problema, recomendacion, contador_alertas].
        diagnostico_ram (list): Diagnóstico actual de la RAM con el formato
            [riesgo, problema, recomendacion, contador_alertas].

    Returns:
        None: La función actualiza los diagnósticos recibidos por parámetro.
    """
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
            
def verificacion_de_intensidad_de_cpu_por_usario(cpu_usada: int, usuarios_conectados: int, diagnostico_usuarios: list) -> None:
    """
    Verifica si el consumo promedio de CPU por usuario supera el
    límite permitido y actualiza el diagnóstico de usuarios.

    Args:
        cpu_usada (int): Porcentaje de uso de la CPU.
        usuarios_conectados (int): Cantidad de usuarios conectados.
        diagnostico_usuarios (list): Diagnóstico de usuarios con el formato
            [riesgo, problema, recomendacion, contador_alertas].

    Returns:
        None: La función actualiza el diagnóstico recibido por parámetro.
    """
    intensidad_cpu_usuarios = calculo_intensidad_cpu_usuarios(cpu_usada, usuarios_conectados)
    CANTIDAD_MAXIMA_DE_CPU_POR_USUARIO = 40
    if intensidad_cpu_usuarios > CANTIDAD_MAXIMA_DE_CPU_POR_USUARIO:
        diagnostico_usuarios[0] = diagnostico_usuarios[0] + f" | CUIDADO"
        diagnostico_usuarios[1] = diagnostico_usuarios[1] + f" | Carga anormal. Cada usuario consume {intensidad_cpu_usuarios}% de CPU. Sospecha de ataque cibernetico."
        diagnostico_usuarios[2] = diagnostico_usuarios[2] + f" | investigue a ese usuario."
        diagnostico_usuarios[3] = diagnostico_usuarios[3] + 1

def verificacion_de_estado_critico_en_ram_y_disco(ram_usada: int, espacio_disco: float, diagnostico_ram: list, diagnostico_disco: list) -> None:
    """
    Verifica si la memoria RAM y el almacenamiento se encuentran
    simultáneamente en estado crítico y actualiza los diagnósticos
    correspondientes.

    Si ambos componentes presentan un estado crítico, se incrementa
    la cantidad de errores y se agregan advertencias, problemas y
    recomendaciones adicionales a cada diagnóstico.

    Args:
        ram_usada (int): Porcentaje de uso de la memoria RAM.
        espacio_disco (float): Espacio libre disponible en disco expresado en GB.
        diagnostico_ram (list): Diagnóstico de memoria RAM con el formato
            [riesgo, problema, recomendacion, contador_alertas].
        diagnostico_disco (list): Diagnóstico de almacenamiento con el formato
            [riesgo, problema, recomendacion, contador_alertas].

    Returns:
        None: La función actualiza los diagnósticos recibidos por parámetro.
    """
    
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

def verificacion_de_cantidad_de_procesos_por_usuario(usuarios_conectados: int, procesos_activos: int, diagnostico_procesos: list) -> None:
    """
    Verifica si la cantidad promedio de procesos por usuario supera
    el límite permitido y actualiza el diagnóstico de procesos.

    Calcula el promedio de procesos activos por usuario conectado y,
    en caso de exceder el valor máximo establecido, registra una alerta
    por posible actividad anómala en el servidor.

    Args:
        usuarios_conectados (int): Cantidad de usuarios conectados.
        procesos_activos (int): Cantidad total de procesos activos.
        diagnostico_procesos (list): Diagnóstico de procesos con el formato
            [riesgo, problema, recomendacion, contador_alertas].

    Returns:
        None: La función actualiza el diagnóstico recibido por parámetro.
    """
    MAXIMOS_PROCESOS_POR_USUARIO = 20
    procesos_por_usuario = calculo_de_cantidad_de_procesos_por_usuarios(usuarios_conectados, procesos_activos)
    if procesos_por_usuario > MAXIMOS_PROCESOS_POR_USUARIO:
        diagnostico_procesos[0] = diagnostico_procesos[0] + f" | CUIDADO"
        diagnostico_procesos[1] = diagnostico_procesos[1] + f" | El promedio de PROCESOS de cada usuario es {procesos_por_usuario} . Posible ataque cibernetico o fuga de hilos"
        diagnostico_procesos[2] = diagnostico_procesos[2] + f" | Haga una verificacion del servidor para estar seguro."
        diagnostico_procesos[3] = diagnostico_procesos[3] + 1

def verificacion_de_vulnerabilidad(tipo_servidor: str, estado_firewall: str, sistema_operativo: str) -> list:
    """
    Verifica si el servidor presenta una vulnerabilidad crítica
    relacionada con su tipo, sistema operativo y estado del firewall.

    Se considera una situación crítica cuando un servidor de tipo
    "base de datos" o "archivos" utiliza Linux y tiene el firewall
    desactivado.

    Args:
        tipo_servidor (str): Tipo de servidor. Puede ser "web",
            "base de datos" o "archivos".
        estado_firewall (str): Estado del firewall. Puede ser
            "activo" o "inactivo".
        sistema_operativo (str): Sistema operativo del servidor.
            Puede ser "linux" o "windows".

    Returns:
        list: Resultado del diagnóstico con el formato
            [riesgo, problema, recomendacion, cantidad_errores].
    """
    diagnostico_seguridad = ["", "", "", 0]
    if (tipo_servidor == "base de datos" or tipo_servidor == "archivos") and (estado_firewall == "inactivo" and sistema_operativo == "linux"):
        
        diagnostico_seguridad[0] = f"EL SERVIDOR SE ENCUNETRA EN ESTADO CRÍTICO!!!"
        diagnostico_seguridad[1] = f"El servidor de tipo {tipo_servidor} presenta una vulnerabilidad crítica al ejecutar {sistema_operativo} con el firewall inactivo."
        diagnostico_seguridad[2] = "Active el firewall perimetral de manera urgente  ."
        diagnostico_seguridad[3] = diagnostico_seguridad[3] + 1
    return diagnostico_seguridad