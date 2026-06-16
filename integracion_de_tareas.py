from inputs import (
    dato_nombre_de_administrador,
    dato_de_nombre_de_servidor,
    dato_de_tipo_sistema_operativo,
    dato_tipo_de_servidor,
    iniciar_sistema,  # se lo llama pero no se lo usa en este modulo es solo para poder usarlo en el main
    dato_cpu,
    dato_ram,
    dato_usuarios_conectados,
    dato_procesos_activos,
    dato_espacio_de_disco,
    dato_estado_firewall,
)
from output import (
    bienvenida_al_sistema,
    mostrar_exito_ingreso_de_datos,
    mostrar_datos_ingresados,
    mostrar_salida_del_sistema,  # se lo llama pero no se lo usa en este modulo es solo para poder usarlo en el main
    reporte_final_del_servidor,
)
from reglas import (
    verificaion_de_credenciales,
    verificacion_de_cpu,
    verificacion_ram,
    verificacion_procesos,
    verificacion_usuarios,
    verificacion_disco,
    verificacion_firewall,
    verificaciion_de_cuello_de_botella,
    verificacion_de_intensidad_de_cpu_por_usuario,
    verificacion_de_estado_critico_en_ram_y_disco,
    verificacion_de_cantidad_de_procesos_por_usuario,
    verificacion_de_vulnerabilidad,
)
# PRIMERA ETAPA: bienvenida y login
def etapa_bienvenida_y_login() -> tuple:
    """
    Gestiona la interfaz inicial de bienvenida y el bucle de autenticación del sistema.

    Muestra el encabezado del programa y solicita interactivamente los datos de 
    credenciales y entorno técnico del servidor. El bucle se repite hasta que las 
    verificaciones de seguridad validen los datos ingresados contra el entorno predefinido.

    Returns:
        tuple: Una tupla que contiene (sistema_operativo, tipo_servidor), que representa
               el entorno de software y el rol corporativo del servidor. 
    """
    bienvenida_al_sistema()
    
    auxiliar = True
    while auxiliar:
        nombre_admin_res = dato_nombre_de_administrador()
        nombre_servidor = dato_de_nombre_de_servidor()
        sistema_operativo = dato_de_tipo_sistema_operativo()
        tipo_servidor = dato_tipo_de_servidor()

        auxiliar = verificaion_de_credenciales(
            auxiliar, nombre_admin_res, nombre_servidor, sistema_operativo, tipo_servidor
        )
        
    mostrar_exito_ingreso_de_datos(nombre_admin_res, nombre_servidor)
    return sistema_operativo, tipo_servidor

# SEGUNDA ETAPA: CARGA DE DATOS
def etapa_carga_de_datos(sistema_operativo: str) -> tuple:
    """
    Pide al usuario los números y métricas actuales del servidor.
    
    Solicita de forma interactiva el uso de CPU, RAM, espacio en disco, 
    usuarios, procesos y si el firewall está activo o no. Al final, 
    muestra en pantalla un resumen de lo que el usuario tipeó.

    Args:
        sistema_operativo (str): El sistema operativo que se obtuvo en el login 
                                 (sirve para mostrarlo en el resumen).

    Returns:
        tuple: Devuelve un paquete ordenado con las 6 métricas recolectadas:
               (cpu_usada, ram_usada, espacio_disco, usuarios_conectados, procesos_activos, estado_firewall).
    """
    print(f"\nComience a ingresar los datos del servidor\n")
    cpu_usada = dato_cpu()
    ram_usada = dato_ram()
    espacio_disco = dato_espacio_de_disco()
    usuarios_conectados = dato_usuarios_conectados()
    procesos_activos = dato_procesos_activos()
    estado_firewall = dato_estado_firewall()
    
    mostrar_datos_ingresados(
        cpu_usada, ram_usada, espacio_disco, usuarios_conectados, 
        procesos_activos, sistema_operativo, estado_firewall
    )
    
    return cpu_usada, ram_usada, espacio_disco, usuarios_conectados, procesos_activos, estado_firewall

# TERCERA ETAPA: DIAGNÓSTICO===
def etapa_ejecucion_del_diagnostico(datos_ingresados: tuple, sistema_operativo: str, tipo_servidor: str) -> tuple:
    """
    Analiza los datos recolectados usando el motor de reglas lógicas.
    
    Desempaqueta las métricas de hardware y ejecuta las reglas una por una. 
    Primero evalúa los componentes individuales (CPU, RAM, etc) y luego 
    hace los análisis cruzados (cuellos de botella, ataques concurrentes, etc.).

    Args:
        datos_ingresados (tuple): El paquete con los 6 datos de hardware de la Etapa 2.
        sistema_operativo (str): El sistema operativo obtenido en el login.
        tipo_servidor (str): El tipo de servidor obtenido en el login.

    Returns:
        tuple: Devuelve un paquete con los 7 resultados de los diagnósticos. 
               Cada resultado es una lista interna con [riesgo, problema, recomendación, cantidad de errores].
    """
    cpu_usada, ram_usada, espacio_disco, usuarios_conectados, procesos_activos, estado_firewall = datos_ingresados
    
    # Verificaciones base
    diagnostico_cpu = verificacion_de_cpu(cpu_usada)
    diagnostico_ram = verificacion_ram(ram_usada)
    diagnostico_procesos = verificacion_procesos(procesos_activos)
    diagnostico_usuarios = verificacion_usuarios(usuarios_conectados)
    diagnostico_disco = verificacion_disco(espacio_disco)
    diagnostico_firewall = verificacion_firewall(estado_firewall)

    # Verificaciones cruzadas (modificación por referencia)
    verificaciion_de_cuello_de_botella(cpu_usada, ram_usada, diagnostico_cpu, diagnostico_ram)
    verificacion_de_intensidad_de_cpu_por_usuario(cpu_usada, usuarios_conectados, diagnostico_usuarios)
    verificacion_de_estado_critico_en_ram_y_disco(ram_usada, espacio_disco, diagnostico_ram, diagnostico_disco)
    verificacion_de_cantidad_de_procesos_por_usuario(usuarios_conectados, procesos_activos, diagnostico_procesos)
    
    diagnostico_de_vulnerabilidad = verificacion_de_vulnerabilidad(tipo_servidor, estado_firewall, sistema_operativo)
    
    return (
        diagnostico_cpu, diagnostico_ram, diagnostico_usuarios, 
        diagnostico_procesos, diagnostico_disco, diagnostico_firewall, 
        diagnostico_de_vulnerabilidad
    )

# CUARTA ETAPA: REPORTE FINAL
def etapa_reporte_final(resultados_de_diagnostico: tuple) -> None:
    """
    Toma los resultados del diagnóstico y los manda a la pantalla final.
    
    Recibe el paquete completo con los 7 análisis calculados en la etapa anterior 
    y se los pasa directamente a la función encargada de dibujar el reporte 
    estético e imprimir las recomendaciones en la consola.

    Args:
        resultados_de_diagnostico (tuple): El paquete que contiene los 7 veredictos 
                                           del servidor.

    Returns:
        None: No devuelve nada, su único trabajo es pasarle los datos al módulo de salida.
    """
    reporte_final_del_servidor(resultados_de_diagnostico)