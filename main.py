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
        

if iniciar_sistema() == "si":   
            
    # SEGUNDA ETAPA: CARGA DE DATOS
    datos_ingresados = etapa_carga_de_datos(sistema_operativo)
            
    # TERCERA ETAPA: DIAGNÓSTICO
    resultados_de_diagnostico = etapa_ejecucion_del_diagnostico(datos_ingresados, sistema_operativo, tipo_servidor)
            
    # CUARTA ETAPA: REPORTE FINAL
    etapa_reporte_final(resultados_de_diagnostico)
            
else:
    mostrar_salida_del_sistema()