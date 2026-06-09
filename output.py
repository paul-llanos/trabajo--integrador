from calculos import calculo_cantidad_de_errores_del_sistema


def bienvenida_al_sistema() -> None:
    """
    Muestra un mensaje de bienvenida e introducción al sistema
    de diagnóstico de servidores.
    """
    print(
        "\nBIENVENIDO AL SISTEMA DE [ DIAGNOSTICO DE SERVIDORES ]\n------POR FAVOR INGRESE LOS DATOS DEL SU SERVIDOR--------\n"
    )
    print(f"\n==============================")


def mostrar_exito_ingreso_de_datos(admin: str, servidor: str) -> None:
    """
    Muestra un mensaje de confirmación indicando que los datos
    fueron ingresados correctamente y da la bienvenida al sistema.

    Args:
        admin (str): Nombre del administrador responsable.
        servidor (str): Nombre del servidor registrado.

    Returns:
        None: Esta función solo muestra información en pantalla.
    """
    print(f"\n==============================")
    print(f"✅ DATOS INGRESADOS CORRECTAMENTE")
    print(f"==============================")
    print(f"Administrador: {admin}")
    print(f"Servidor: {servidor}")
    print(f"==============================")
    print(f"BIENVENIDO AL SISTEMA DE [DIAGNOSTICO DE SERVIDORES]")
    print(f"==============================\n")


def mostrar_salida_del_sistema() -> None:
    """
    Muestra un mensaje de despedida e informa al usuario que el
    sistema de diagnóstico de servidores se está cerrando.

    Returns:
        None: Esta función solo muestra información en pantalla.
    """
    print(f"\n==============================")
    print(f"\nGracias por utilizar el sistema de diagnostico de servidores")
    print(f"\n Saliendo del sistema... ")
    print(f"\n==============================")


def mostrar_datos_ingresados(
    cpu_usada: int,
    ram_usada: int,
    espacio_disco: float,
    usuarios_conectados: int,
    procesos_activos: int,
    sistema_operativo: str,
    estado_firewall: str,
) -> None:
    """
    Muestra en pantalla los datos ingresados por el usuario para
    el diagnóstico del servidor.

    Args:
        cpu_usada (int): Porcentaje de uso de la CPU.
        ram_usada (int): Porcentaje de uso de la memoria RAM.
        espacio_disco (float): Espacio libre disponible en disco en GB.
        usuarios_conectados (int): Cantidad de usuarios conectados.
        procesos_activos (int): Cantidad de procesos activos.
        sistema_operativo (str): Sistema operativo del servidor.
        estado_firewall (str): Estado del firewall del servidor.

    Returns:
        None: Esta función solo muestra información en pantalla.
    """
    print(f"\nDATOS INGRESADOS: \n")
    print(f"uso de cpu: {cpu_usada}% ")
    print(f"uso de ram: {ram_usada}% ")
    print(f"espacio libre en disco: {espacio_disco} GB")
    print(f"cantidad de usuarios conectados: {usuarios_conectados}")
    print(f"cantidad de procesos activos: {procesos_activos}")
    print(f"sistema operativo: {sistema_operativo}")
    print(f"estado del firewall: {estado_firewall}")


def reporte_final_del_servidor(
    diagnostico_cpu: list,
    diagnostico_ram: list,
    diagnostico_usuarios: list,
    diagnostico_procesos: list,
    diagnostico_disco: list,
    diagnostico_firewall: list,
    diagnostico_de_vulnerabilidad: list,
) -> None:
    """
    Genera y muestra el reporte final del diagnóstico del servidor.

    A partir de los resultados de los distintos diagnósticos,
    determina el estado general del servidor y muestra únicamente
    los componentes que presentan alertas o riesgos.

    Args:
        diagnostico_cpu (list): Resultado del diagnóstico de CPU.
        diagnostico_ram (list): Resultado del diagnóstico de memoria RAM.
        diagnostico_usuarios (list): Resultado del diagnóstico de usuarios conectados.
        diagnostico_procesos (list): Resultado del diagnóstico de procesos activos.
        diagnostico_disco (list): Resultado del diagnóstico de almacenamiento.
        diagnostico_firewall (list): Resultado del diagnóstico del firewall.
        diagnostico_de_vulnerabilidad (list): Resultado del análisis de vulnerabilidades.

    Returns:
        None: Esta función genera y muestra el reporte en pantalla.
    """
    total_alertas = calculo_cantidad_de_errores_del_sistema(
        diagnostico_cpu,
        diagnostico_ram,
        diagnostico_usuarios,
        diagnostico_procesos,
        diagnostico_disco,
        diagnostico_firewall,
        diagnostico_de_vulnerabilidad,
    )

    if total_alertas == 0:
        print("\n----------------------------------------------\n")
        print(" ✅ SERVIDOR EN BUEN ESTADO ✅ ")
        print("\n----------------------------------------------\n")
    else:
        print("\n------------------------------")
        if total_alertas < 3:
            print(" ⚠️ ATENCION: SERVIDOR FUERA DE LO NORMAL ⚠️")
        elif total_alertas < 5:
            print("  🚨 ATENCION: SERVIDOR EN ALERTA 🚨")
        else:
            print("  🔥 ATENCION: SERVIDOR EN ESTADO CRITICO 🔥")

        print("        📊 DIAGNOSTICO DE SERVIDOR 📊\n")
        print("------------------------------")

        # SOLO SE MUESTRAN LOS COMPONENTES CON RIESGO EN EL SERVIDOR

        if diagnostico_cpu[0] != "":
            print("\n[ CPU ]")
            print(f"Riesgo: {diagnostico_cpu[0]}")
            print(f"Problema: {diagnostico_cpu[1]}")
            print(f"Recomendación: {diagnostico_cpu[2]}")

        if diagnostico_ram[0] != "":
            print("\n------------------------------")
            print("[ RAM ]")
            print(f"Riesgo: {diagnostico_ram[0]}")
            print(f"Problema: {diagnostico_ram[1]}")
            print(f"Recomendación: {diagnostico_ram[2]}")

        if diagnostico_procesos[0] != "":
            print("\n------------------------------")
            print("[ PROCESOS ]")
            print(f"Riesgo: {diagnostico_procesos[0]}")
            print(f"Problema: {diagnostico_procesos[1]}")
            print(f"Recomendación: {diagnostico_procesos[2]}")

        if diagnostico_usuarios[0] != "":
            print("\n------------------------------")
            print("[ USUARIOS ]")
            print(f"Riesgo: {diagnostico_usuarios[0]}")
            print(f"Problema: {diagnostico_usuarios[1]}")
            print(f"Recomendación: {diagnostico_usuarios[2]}")

        if diagnostico_disco[0] != "":
            print("\n------------------------------")
            print("[ ALMACENAMIENTO ]")
            print(f"Riesgo: {diagnostico_disco[0]}")
            print(f"Problema: {diagnostico_disco[1]}")
            print(f"Recomendación: {diagnostico_disco[2]}")

        if diagnostico_firewall[0] != "":
            print("\n------------------------------")
            print("[ SEGURIDAD - FIREWALL ]")
            print(f"Riesgo: {diagnostico_firewall[0]}")
            print(f"Problema: {diagnostico_firewall[1]}")
            print(f"Recomendación: {diagnostico_firewall[2]}")

        # La alerta global de seguridad del sistema
        if diagnostico_de_vulnerabilidad[0] != "":
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(
                f"🚨 ALERTAS DE SEGURIDAD GENERAL: {diagnostico_de_vulnerabilidad[1]}"
            )
            print(f"Recomendación: {diagnostico_de_vulnerabilidad[2]}")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
