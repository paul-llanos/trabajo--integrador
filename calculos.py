def calculo_cuello_de_botella(cpu_usada, ram_usada):
    if cpu_usada > ram_usada:
        cuello_de_botella = cpu_usada - ram_usada
        return cuello_de_botella
    else:
        cuello_de_botella = ram_usada - cpu_usada
        return cuello_de_botella

def calculo_intensidad_cpu_usuarios(cpu_usada, usuarios_conectados):
    intensidad_cpu_usuarios = cpu_usada / usuarios_conectados
    return intensidad_cpu_usuarios

def calculo_de_cantidad_de_procesos_por_usuarios(usuarios_conectados, procesos_activos):
    if usuarios_conectados > 0:
        procesos_por_usuario = procesos_activos / usuarios_conectados
        return procesos_por_usuario

def calculo_cantidad_de_errores_del_sistema(diagnostico_cpu, diagnostico_ram, diagnostico_usuarios, diagnostico_procesos, diagnostico_disco, diagnostico_firewall, diagnostico_de_vulnerabilidad):
    cantidad_de_errores_del_sistema = diagnostico_cpu[3] + diagnostico_ram[3] + diagnostico_usuarios[3] + diagnostico_procesos[3] + diagnostico_disco[3] + diagnostico_firewall[3] + diagnostico_de_vulnerabilidad[3]
    return cantidad_de_errores_del_sistema