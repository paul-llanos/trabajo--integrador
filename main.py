from bienvenida_y_despedida import (
    bienvenida_al_sistema,
    salida_del_sistema,
    mostrar_exito_ingreso_de_datos,
    mostrar_datos_ingresados,
)
from calculos import (
    calculo_cuello_de_botella,
)
from funciones_de_validacion import (
    validacion_numerico,
    validacion_porcentaje_numerico,
    validacion_datos_categoricos,
    validacion_cadena,
)
from reglas import (
    verificaion_de_credenciales,
    verificacion_de_cpu,
    verificacion_ram,
    verificacion_procesos,
    verificacion_usuarios,
    verificacion_disco,
    verificacion_firewall,
)
from inputs import (
    dato_nombre_de_administrador,
    dato_de_nombre_de_servior,
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

# variables de credenciales

# cpu ram
RAM_CPU_CUELLO_DE_BOTELLA = 40
# procesos y usuarios
POSIBLE_ATAQUE = 40
# disco
DISCO_DISPONIBLE_MIN = 60
# contante la cantidad de procesos que puedria llegar a tener un usuario
MAX_PROCESOS_POR_USER = 20

"""VARIABLES PARA LAS REGLAS"""
# variables de entrada
nombre_admin_res = ""
nombre_servidor = ""
cpu_usada = 0
ram_usada = 0
sistema_operativo = ""
tipo_servidor = ""
usuarios_conectados = 0
procesos_activos = 0
espacio_disco = 0
estado_firewall = ""

# cpu y ram
cpu_riesgo = ""
ram_riesgo = ""
problema_cpu = ""
problema_ram = ""
recomendacion_cpu = ""
recomendacion_ram = ""
# procesos y usuarios
procesos_riesgo = ""
usuarios_riesgo = ""
problema_procesos = ""
problema_usuarios = ""
recomendacion_procesos = ""
recomendacion_usuarios = ""
# disco
riesgo_disco = ""
problema_disco = ""
recomendacion_disco = ""
# firewall
riesgo_firewall = ""
problema_firewall = ""
recomendacion_firewall = ""

# VARIABLES DE CALCULO
cuello_de_botella = 0
intensidad_cpu_usuarios = 0
alerta = ""
contador = 0

axuliar = True
bienvenida_al_sistema()

while axuliar:

    nombre_admin_res = dato_nombre_de_administrador()

    nombre_servidor = dato_de_nombre_de_servior()

    sistema_operativo = dato_de_tipo_sistema_operativo()

    tipo_servidor = dato_tipo_de_servidor()

    axuliar = verificaion_de_credenciales(
        axuliar, nombre_admin_res, nombre_servidor, sistema_operativo, tipo_servidor
    )

mostrar_exito_ingreso_de_datos(nombre_admin_res, nombre_servidor)

# preguntamos si queremos iniciar el diagnostico
iniciar_sistema = iniciar_sistema()

if iniciar_sistema == "si":
    print(f"\nComience a ingresar los datos del servidor\n")

    #  cargamos los datos y se validan que sean correctos para el diagnostico
    cpu_usada = dato_cpu()

    ram_usada = dato_ram()

    espacio_disco = dato_espacio_de_disco()

    usuarios_conectados = dato_usuarios_conectados()

    procesos_activos = dato_procesos_activos()

    estado_firewall = dato_estado_firewall()

    # mostramos los datos ingresados
    mostrar_datos_ingresados()

    # CALCULOS CPU
    diagnostigo_cpu = verificacion_de_cpu(cpu_usada)
    # CALCULOS RAM
    diagnostico_ram = verificacion_ram(ram_usada) 
    # CALCULOS PROCESOS
    diagnostico_procesos = verificacion_procesos(procesos_activos)
    # CALCULOS USUARIOS
    diagnostico_usuarios = verificacion_usuarios(usuarios_conectados)
    # CALCULO DISCO
    diagnostico_disco = verificacion_disco(espacio_disco)
    # FIREWALL
    diagnostico_procesos = verificacion_firewall(estado_firewall)

    #  CALCULAMOS  CUELLO DE BOTELLA DEL CPU Y RAM
    cuello_de_botella = calculo_cuello_de_botella(cpu_usada, ram_usada)
    # VERIFICAMOS EL CUELLO DE BOTELLA
    if cuello_de_botella > RAM_CPU_CUELLO_DE_BOTELLA:
        contador = contador + 1
        if cpu_usada > ram_usada:
            cpu_riesgo += "| CUIDADO"
            problema_cpu += f" |  CPU: {cpu_usada}% cuello de botella respecto a RAM: {ram_usada}% Diferencia de: {cuello_de_botella}% de uso)"
            recomendacion_cpu += " | COMPRE UNA MEJOR RAM"
        else:
            ram_riesgo += " | CUIDADO"
            problema_ram += f" | RAM: {ram_usada}% cuello de botella respecto a COU: {cpu_usada}% Diferencia de: {cuello_de_botella}%)"
            recomendacion_ram += " | COMPRE UN MEJOR CPU"
    # VERIFICAMOS El INTENSIDAD DE CPU QUE ESTA OCUPANDO UN USUARIO
    if usuarios_conectados > 0:
        intensidad_cpu_usuarios = cpu_usada / usuarios_conectados
        if intensidad_cpu_usuarios > 45:
            contador = contador + 1
            usuarios_riesgo += " | CUIDADO"
            problema_usuarios += f" | Carga anormal. Cada usuario consume {intensidad_cpu_usuarios}% de CPU. Sospecha de ataque cibernetico."
            recomendacion_usuarios += " | investigue a ese usuario."
    # VERIFICAMOS POSIBLE PROBLERMA DE RAM Y DISCO
    if ram_riesgo == "critico" and riesgo_disco == "critico":
        contador = contador + 1
        riesgo_disco += " | CUIDADO"
        ram_riesgo += " | CUIDADO"
        problema_ram += f" | cuidado tiene la ram {ram_usada} y a su disco le quedan menos de {espacio_disco} GB su servidor puede caer"
        problema_disco += f" | cuidado tiene el disco {espacio_disco} y a su ram le quedan menos de {ram_usada} GB su servidor puede colapsar"
        recomendacion_ram += " | Limite el consumo de ram por usuario ."
        recomendacion_disco += " | elimine archivos temporales del usuario."
    # VERIFICO POSIBLE AMENAZA SI UN USUARIO TIENE MAS PROCESOS QUE LOS PERMITIDO
    if usuarios_conectados > 0:
        procesos_por_usuario = procesos_activos / usuarios_conectados
        if procesos_por_usuario > MAX_PROCESOS_POR_USER:
            contador = contador + 1
            procesos_riesgo += " | CUIDADO"
            problema_procesos += f" |  El promedio de PROCESOS de cada usuario es {procesos_por_usuario} . Posible ataque cibernetico o fuga de hilos"
            recomendacion_procesos += (
                " | Haga una verificacion del servidor para estar seguro."
            )

        # VERIFICO SI EL SERVIDOR ES DE TIPO BASE DE DATOS O ARCHIVOS Y EL FIREWALL ESTA INACTIVO
        if (tipo_servidor == "base de datos" or tipo_servidor == "archivos") and (
            estado_firewall == "inactivo" and sistema_operativo == "linux"
        ):
            contador = contador + 1
            alerta += f"cuidado el servior de tipo: {tipo_servidor} esta vulnerable a ataques en este sistema operativo {sistema_operativo}"

    if contador == 0:
        print(f"\n----------------------------------------------\n")
        print(f"\n ✅SERVIDOR EN BUEN ESTADO✅ \n")
    else:
        print(f"\n------------------------------")
        if contador < 3:
            print(f" ⚠️ ATENCION: SERVIDOR FUERA DE LO NORMAL⚠️")
        elif contador < 5:
            print(f"  🚨ATENCION: SERVIDOR EN ALERTA🚨")
        else:
            print(f"  🔥ATENCION: SERVIDOR EN ESTADO CRITICO🔥")

        print(f"         📊DIAGNOSTICO DE SERVIDOR📊\n")
        print(f"\n------------------------------")

        # SOLO SE VAN A MOSTROS LOS RESULTADOS DE AQUELLOS QUE TIENEN RIESGO
        if cpu_riesgo != "":
            print(f"\n[ CPU ]")
            print(f"Riesgo: {cpu_riesgo}")
            print(f"Problema: {problema_cpu}")
            print(f"Recomendación: {recomendacion_cpu}")

        if ram_riesgo != "":
            print(f"\n[ RAM ]")
            print(f"Riesgo: {ram_riesgo}")
            print(f"Problema: {problema_ram}")
            print(f"Recomendación: {recomendacion_ram}")

        if procesos_riesgo != "":
            print(f"\n------------------------------")
            print(f"[  PROCESOS ]")
            print(f"Riesgo: {procesos_riesgo}")
            print(f"Problema: {problema_procesos}")
            print(f"Recomendación: {recomendacion_procesos}")

        if usuarios_riesgo != "":
            print(f"\n------------------------------")
            print(f"[ USUARIOS ]")
            print(f"Riesgo: {usuarios_riesgo}")
            print(f"Problema: {problema_usuarios}")
            print(f"Recomendación: {recomendacion_usuarios}")

        if riesgo_disco != "":
            print(f"\n------------------------------")
            print(f"[ ALMACENAMIENTO ]")
            print(f"Riesgo: {riesgo_disco}")
            print(f"Problema: {problema_disco}")
            print(f"Recomendación: {recomendacion_disco}")

        if riesgo_firewall != "":
            print(f"\n------------------------------")
            print(f"[ SEGURIDAD - FIREWALL ]")
            print(f"Riesgo: {riesgo_firewall}")
            print(f"Problema: {problema_firewall}")
            print(f"Recomendación: {recomendacion_firewall}")

        if alerta != "":
            print(f"\n!!!!!!!!!!!!!!!!!\n")
            print(f"ALERTAS DEL SISTEMA: {alerta}")
            print(f"\n!!!!!!!!!!!!!!!!!\n")

else:
    salida_del_sistema()
