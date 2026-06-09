from inputs import (
    dato_nombre_de_administrador,
    dato_de_nombre_de_servidor,
    dato_de_tipo_sistema_operativo,
    dato_tipo_de_servidor,
    iniciar_sistema,
    dato_cpu,
    dato_ram,
    dato_usuarios_conectados,
    dato_procesos_activos,
    dato_espacio_de_disco,
    dato_estado_firewall,
)
from output import (
    bienvenida_al_sistema,
    mostrar_salida_del_sistema,
    mostrar_exito_ingreso_de_datos,
    mostrar_datos_ingresados,
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
    verificacion_de_intensidad_de_cpu_por_usario,
    verificacion_de_estado_critico_en_ram_y_disco,
    verificacion_de_cantidad_de_procesos_por_usuario,
    verificacion_de_vulnerabilidad,
)

axuliar = True
# MOSTRAMOS LA BIENVENIDA AL SISTEMA
bienvenida_al_sistema()

while axuliar:
    # INGRESAMOS LAS CREDENCIALES DE INGRESO
    nombre_admin_res = dato_nombre_de_administrador()

    nombre_servidor = dato_de_nombre_de_servidor()

    sistema_operativo = dato_de_tipo_sistema_operativo()

    tipo_servidor = dato_tipo_de_servidor()

    axuliar = verificaion_de_credenciales(
        axuliar, nombre_admin_res, nombre_servidor, sistema_operativo, tipo_servidor
    )
# VALIDAMOS LAS CREDENCIALES INGRESADAS
mostrar_exito_ingreso_de_datos(nombre_admin_res, nombre_servidor)

# PREGUNTAMOS SI QUEREMOS INICIAR EL SISTEMA
iniciar_diagnostico = iniciar_sistema()
# INICIAMOS EL SISTEMA
if iniciar_diagnostico == "si":
    print(f"\nComience a ingresar los datos del servidor\n")

    #  CARGAMOS LOS DATOS Y VALIDAMOS
    cpu_usada = dato_cpu()

    ram_usada = dato_ram()

    espacio_disco = dato_espacio_de_disco()

    usuarios_conectados = dato_usuarios_conectados()

    procesos_activos = dato_procesos_activos()

    estado_firewall = dato_estado_firewall()

    # MOSTRAMOS LOS DATOS INGRESADOS
    mostrar_datos_ingresados(
        cpu_usada,
        ram_usada,
        espacio_disco,
        usuarios_conectados,
        procesos_activos,
        sistema_operativo,
        estado_firewall,
    )

    # DIAGNOSTIGO CPU
    diagnostico_cpu = verificacion_de_cpu(cpu_usada)
    # DIAGNOSTIGO RAM
    diagnostico_ram = verificacion_ram(ram_usada)
    # DIAGNOSTIGO PROCESOS
    diagnostico_procesos = verificacion_procesos(procesos_activos)
    # DIAGNOSTIGO USUARIOS
    diagnostico_usuarios = verificacion_usuarios(usuarios_conectados)
    # DIAGNOSTIGO DISCO
    diagnostico_disco = verificacion_disco(espacio_disco)
    # DIAGNOSTIGO FIREWALL
    diagnostico_firewall = verificacion_firewall(estado_firewall)

    # VERIFICAMOS EL CUELLO DE BOTELLA
    verificaciion_de_cuello_de_botella(
        cpu_usada, ram_usada, diagnostico_cpu, diagnostico_ram
    )
    # VERIFICAMOS LA INTENSIDAD DE CPU QUE ESTA OCUPANDO UN USUARIO
    verificacion_de_intensidad_de_cpu_por_usario(
        cpu_usada, usuarios_conectados, diagnostico_usuarios
    )
    # VERIFICAMOS POSIBLE PROBLERMA DE RAM Y DISCO POR ESTADO CRITICO EN AMBOS CASOS
    verificacion_de_estado_critico_en_ram_y_disco(
        ram_usada, espacio_disco, diagnostico_ram, diagnostico_disco
    )
    # VERIFICACION POSIBLE AMENAZA SI UN USUARIO TIENE MAS PROCESOS DE LO NORMAL
    verificacion_de_cantidad_de_procesos_por_usuario(
        usuarios_conectados, procesos_activos, diagnostico_procesos
    )
    # VERIFICO SI HAY VULNERABILIDAD SI  EL SERVIDOR ES DE TIPO BASE DE DATOS O ARCHIVOS Y EL FIREWALL ESTA INACTIVO
    diagnostico_de_vulnerabilidad = verificacion_de_vulnerabilidad(
        tipo_servidor, estado_firewall, sistema_operativo
    )
    # MOSTRAMOS EL DIAGNOSTICO FINAL
    reporte_final_del_servidor(
        diagnostico_cpu,
        diagnostico_ram,
        diagnostico_usuarios,
        diagnostico_procesos,
        diagnostico_disco,
        diagnostico_firewall,
        diagnostico_de_vulnerabilidad,
    )

else:
    mostrar_salida_del_sistema()
