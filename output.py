from calculos import calculo_cantidad_de_errores_del_sistema
def bienvenida_al_sistema():
    print("\nBIENVENIDO AL SISTEMA DE [ DIAGNOSTICO DE SERVIDORES ]\n------POR FAVOR INGRESE LOS DATOS DEL SU SERVIDOR--------\n")
    print(f"\n==============================")

def mostrar_exito_ingreso_de_datos(admin: str, servidor: str):
    """Confirma que el acceso fue otorgado con éxito."""
    print(f"\n==============================")
    print(f"✅ DATOS INGRESADOS CORRECTAMENTE")
    print(f"==============================")
    print(f"Administrador: {admin}")
    print(f"Servidor: {servidor}")
    print(f"==============================")
    print(f"BIENVENIDO AL SISTEMA DE [DIAGNOSTICO DE SERVIDORES]")
    print(f"==============================\n")



def mostrar_salida_del_sistema():
    print(f"\n==============================")
    print(f"\nGracias por utilizar el sistema de diagnostico de servidores")
    print(f"\n Saliendo del sistema... ")
    print(f"\n==============================")

def mostrar_datos_ingresados(cpu_usada, ram_usada, espacio_disco, usuarios_conectados, procesos_activos, sistema_operativo, estado_firewall):
        print(f"\nDATOS INGRESADOS: \n")
        print(f"uso de cpu: {cpu_usada}% ")
        print(f"uso de ram: {ram_usada}% ")
        print(f"espacio libre en disco: {espacio_disco} GB")
        print(f"cantidad de usuarios conectados: {usuarios_conectados}")
        print(f"cantidad de procesos activos: {procesos_activos}")
        print(f"sistema operativo: {sistema_operativo}")
        print(f"estado del firewall: {estado_firewall}")

def reporte_final_del_servidor(diagnostico_cpu, diagnostico_ram, diagnostico_usuarios, diagnostico_procesos, diagnostico_disco, diagnostico_firewall, diagnostico_de_vulnerabilidad,):
    total_alertas = calculo_cantidad_de_errores_del_sistema(diagnostico_cpu, diagnostico_ram, diagnostico_usuarios, diagnostico_procesos, diagnostico_disco, diagnostico_firewall, diagnostico_de_vulnerabilidad)

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

        #SOLO SE MUESTRAN LOS COMPONENTES CON RIESGO EN EL SERVIDOR
        
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
            print(f"🚨 ALERTAS DE SEGURIDAD GENERAL: {diagnostico_de_vulnerabilidad[1]}")
            print(f"Recomendación: {diagnostico_de_vulnerabilidad[2]}")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")