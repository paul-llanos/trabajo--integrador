def calculo_cuello_de_botella(cpu_usada: float, ram_usada: float) -> float:
    """
    Calcula la diferencia entre el uso de CPU y RAM.

    Args:
        cpu_usada (float): Porcentaje de uso de la CPU.
        ram_usada (float): Porcentaje de uso de la memoria RAM.

    Returns:
        float: Diferencia absoluta entre ambos porcentajes.
    """
    if cpu_usada > ram_usada:
        cuello_de_botella = cpu_usada - ram_usada
        return cuello_de_botella
    else:
        cuello_de_botella = ram_usada - cpu_usada
        return cuello_de_botella


def calculo_intensidad_cpu_usuarios(
    cpu_usada: float, usuarios_conectados: int
) -> float:
    """
    Calcula la intensidad de uso de CPU por usuario conectado.

    Args:
        cpu_usada (float): Porcentaje de uso de la CPU.
        usuarios_conectados (int): Cantidad de usuarios conectados.

    Returns:
        float: Uso promedio de CPU por usuario conectado.
    """
    intensidad_cpu_usuarios = cpu_usada / usuarios_conectados
    return intensidad_cpu_usuarios


def calculo_de_cantidad_de_procesos_por_usuarios(
    usuarios_conectados: int, procesos_activos: int
) -> float:
    """
    Calcula la cantidad promedio de procesos activos por usuario conectado.

    Args:
        usuarios_conectados (int): Cantidad de usuarios conectados al sistema.
        procesos_activos (int): Cantidad total de procesos activos.

    Returns:
        float: Promedio de procesos activos por usuario.
    """
    if usuarios_conectados > 0:
        procesos_por_usuario = procesos_activos / usuarios_conectados
        return procesos_por_usuario


def calculo_cantidad_de_errores_del_sistema(
    diagnostico_cpu: list,
    diagnostico_ram: list,
    diagnostico_usuarios: list,
    diagnostico_procesos: list,
    diagnostico_disco: list,
    diagnostico_firewall: list,
    diagnostico_de_vulnerabilidad: list,
) -> int:
    """
    Calcula la cantidad total de errores detectados en el sistema.

    Args:
        diagnostico_cpu (list): Resultado del diagnóstico de CPU.
        diagnostico_ram (list): Resultado del diagnóstico de RAM.
        diagnostico_usuarios (list): Resultado del diagnóstico de usuarios.
        diagnostico_procesos (list): Resultado del diagnóstico de procesos.
        diagnostico_disco (list): Resultado del diagnóstico de disco.
        diagnostico_firewall (list): Resultado del diagnóstico de firewall.
        diagnostico_de_vulnerabilidad (list): Resultado del diagnóstico de vulnerabilidades.

    Returns:
        int: Cantidad total de errores detectados en todos los diagnósticos.
    """

    cantidad_de_errores_del_sistema = (
        diagnostico_cpu[3]
        + diagnostico_ram[3]
        + diagnostico_usuarios[3]
        + diagnostico_procesos[3]
        + diagnostico_disco[3]
        + diagnostico_firewall[3]
        + diagnostico_de_vulnerabilidad[3]
    )
    return cantidad_de_errores_del_sistema

