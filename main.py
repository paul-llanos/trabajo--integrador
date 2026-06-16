from integracion_de_tareas import (
    etapa_bienvenida_y_login,
    etapa_carga_de_datos,
    etapa_ejecucion_del_diagnostico,
    etapa_reporte_final,
    iniciar_sistema,
    mostrar_salida_del_sistema,
)


    
#  PRIMERA ETAPA: BIENVENIDA Y LOGIN
sistema_operativo, tipo_servidor = etapa_bienvenida_y_login()
        
# Menú de decisión para iniciar el escaneo
if iniciar_sistema() == "si":
            
    # SEGUNDA ETAPA: CARGA DE DATOS
    datos_ingresados = etapa_carga_de_datos(sistema_operativo)
            
    # 3. DIAGNÓSTICO (Ejecución del motor de reglas)
    resultados_de_diagnostico = etapa_ejecucion_del_diagnostico(datos_ingresados, sistema_operativo, tipo_servidor)
            
    # 4. REPORTE FINAL
    etapa_reporte_final(resultados_de_diagnostico)
            
else:
    mostrar_salida_del_sistema()