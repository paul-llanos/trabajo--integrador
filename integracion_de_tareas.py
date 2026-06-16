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
    """Muestra la bienvenida y gestiona el bucle de credenciales."""
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
    """Solicita al usuario las métricas actuales del servidor."""
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


# ======================================================================
# TERCERA ETAPA: DIAGNÓSTICO===
# =========================================================================
def etapa_ejecucion_del_diagnostico(datos_ingresados: tuple, sistema_operativo: str, tipo_servidor: str) -> tuple:
    """Procesa los datos a través de las reglas lógicas individuales y cruzadas."""
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
    """Envía los resultados procesados al módulo de salida."""
    reporte_final_del_servidor(resultados_de_diagnostico)