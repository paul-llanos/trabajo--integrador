from funciones_de_validacion import (
    validacion_numerico,
    validacion_porcentaje_numerico,
    validacion_datos_categoricos,
    validacion_cadena,
    validadcion_de_incio_de_diagnostico,
)


def dato_nombre_de_administrador() -> str:
    """
    Solicita al usuario el nombre del administrador responsabley valida que
    cumpla con los requisitos mínimos de longitud y contenido.

    Mantiene un bucle  que insiste en la petición si el usuario
    ingresa un texto inválido, vacío o con menos de 6 caracteres útiles.

    Returns:
        str: El nombre del administrador validado.
    """
    nombre_admin_res = input("Administrador responsable: ")
    
    while not validacion_cadena(nombre_admin_res):
        print("no puede dejar el dato en blanco o con menos de 6 caracteres")
        nombre_admin_res = input("Ingrese el nombre del Administrador responsable: ")
        
    return nombre_admin_res


def dato_de_nombre_de_servidor() -> str:
    """
    Solicita al usuario el nombre del servidor  y valida que cumpla con los
    requisitos mínimos de longitud y contenido.

    Mantiene un bucle interactivo que insiste en la petición si el usuario
    ingresa un texto inválido, vacío o con menos de 6 caracteres .

    Returns:
        str: El nombre del servidor validado.
    """
    nombre_servidor = input("Ingrese el nombre del servidor: ")
    
    while not validacion_cadena(nombre_servidor):
        print("no puede dejar el dato en blanco o con menos de 6 caracteres")
        nombre_servidor = input("Ingrese el nombre del servidor: ")
        
    return nombre_servidor

def dato_tipo_de_servidor() -> str:
    """
    Solicita al usuario el tipo de servidor y valida que
    corresponda a una de las categorías permitidas.

    Returns:
        str: Tipo de servidor validado. Los valores permitidos
        son "web", "base de datos" o "archivos".
    """
    tipo_servidor = input(
        "Ingrese el tipo de servidor [web] [base de datos] [archivos]: "
    )
    while not validacion_datos_categoricos(tipo_servidor, "servidor"):
        print(f"ingrese correctamente el dato")
        tipo_servidor = input("Ingrese el tipo de servidor: ")
    return tipo_servidor


def dato_de_tipo_sistema_operativo() -> str:
    """
    Solicita al usuario el tipo de sistema operativo y valida
    que corresponda a una de las opciones permitidas.

    Returns:
        str: Sistema operativo validado. Los valores permitidos
        son "linux" o "windows".
    """
    sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")
    while not validacion_datos_categoricos(sistema_operativo, "so"):
        print(f"ingrese correctamente el dato")
        sistema_operativo = input("Ingrese el Sistema Operativo: [linux] [windows]: ")
    return sistema_operativo


def iniciar_sistema() -> str:
    """
    Solicita al usuario si desea iniciar el diagnóstico del sistema
    y valida que la respuesta sea correcta.

    Returns:
        str: Respuesta validada del usuario. Los valores permitidos
        son "si" o "no".
    """
    iniciar_sistema = input("DESEA INICIAR EL TEST? [si] / [no]: ")
    while not validadcion_de_incio_de_diagnostico(iniciar_sistema):
        print(f"ingrese correctamente el dato")
        iniciar_sistema = input("DESEA INICIAR EL TEST? [si] / [no]: ")
    return iniciar_sistema


def dato_cpu() -> float:
    """
    Solicita al usuario el porcentaje de uso de la CPU por consola,
    validando que el ingreso sea un número correcto entre 0 y 100.
    
    La función mantiene un bucle interactivo que insiste en la petición
    hasta que el usuario introduce un formato numérico válido.

    Returns:
        float: El porcentaje de uso de la CPU validado y convertido a tipo flotante.
    """
    cpu_usada = input("Ingrese el uso del CPU % : ")

    while not validacion_porcentaje_numerico(cpu_usada):
        print("Ingrese correctamente su numero")
        cpu_usada = input("Ingrese el uso del CPU % : ")
    cpu_usada = float(cpu_usada)
    return cpu_usada

def dato_ram() -> float:
    """
    Solicita al usuario el porcentaje de utilización de la memoria RAM
    del servidor y verifica que el valor ingresado sea válido.

    Returns:
        int: Porcentaje de uso de la memoria RAM.
    """
    ram_usada = input("Ingrese el uso de de Memoria RAM % : ")
    while not validacion_porcentaje_numerico(ram_usada):
        print(f"ingrese correctamente su dato")
        ram_usada = input("Ingrese el uso de memoria RAM % : ")
    ram_usada = float(ram_usada)
    return ram_usada


def dato_espacio_de_disco() -> float:
    """
    Solicita al usuario el espacio libre disponible en disco y valida
    que el valor ingresado sea numérico.

    Returns:
        float: Cantidad de espacio libre en disco expresada en gigabytes (GB).
    """
    espacio_disco = input("Ingrese el espacio libre en disco [GB]: ")
    while not validacion_numerico(espacio_disco):
        print(f"ingrese correctamente su numero")
        espacio_disco = input("Ingrese el espacio libre en disco [GB] : ")
    espacio_disco = float(espacio_disco)
    return espacio_disco


def dato_usuarios_conectados() -> int:
    """
    Solicita al usuario la cantidad de usuarios conectados al sistema
    y valida que el valor ingresado sea numérico.

    Returns:
        int: Cantidad de usuarios conectados al sistema.
    """
    usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")
    while not validacion_numerico(usuarios_conectados):
        print(f"ingrese correctamente el dato")
        usuarios_conectados = input("Ingrese la cantidad de usuarios conectados: ")
    usuarios_conectados = int(usuarios_conectados)
    return usuarios_conectados


def dato_procesos_activos() -> int:
    """
    Solicita al usuario la cantidad de procesos activos del sistema
    y valida que el valor ingresado sea numérico.

    Returns:
        int: Cantidad de procesos activos registrados en el sistema.
    """
    procesos_activos = input("Ingrese la cantidad de procesos activos: ")
    while not validacion_numerico(procesos_activos):
        print(f"ingrese correctamente el dato")
        procesos_activos = input("Ingrese la cantidad de procesos activos: ")
    procesos_activos = int(procesos_activos)
    return procesos_activos


def dato_estado_firewall() -> str:
    """
    Solicita al usuario el estado del firewall y valida que el valor
    ingresado corresponda a una de las opciones permitidas.

    Returns:
        str: Estado del firewall validado. Los valores permitidos
        son "activo" o "inactivo".
    """
    estado_firewall = input("Ingrese el estado del firewall [activo] [inactivo]: ")
    while not validacion_datos_categoricos(estado_firewall, "firewall"):
        print(f"ingrese correctamente el dato")
        estado_firewall = input("Ingrese el estado del firewall [activo] [inactivo]: ")
    return estado_firewall
