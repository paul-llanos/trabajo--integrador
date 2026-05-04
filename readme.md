# Sistema de Diagnóstico de Servidores 

 detección de fallas y vulnerabilidades en servidores mediante un motor de decisiones basado en reglas lógicas, brindando recomendaciones técnicas .

#1. Reglas de Diagnóstico
El motor de decisiones evalúa el estado del servidor utilizando un mínimo de 8 reglas lógicas que combinan múltiples variables[cite: 4, 7]:

_Sobrecarga de CPU/RAM**: Se activa si el uso de CPU o RAM supera el **85%** (CPU_MAX/RAM_MAX)[cite: 6, 7].
_Riesgo de Seguridad**: Detecta peligro si el firewall no está en estado "activo" (Uso de **NOT**)[cite: 6, 7].
_Almacenamiento Crítico**: Alerta si el espacio disponible es menor a **60 GB**[cite: 6, 7].
_Cuello de Botella: Identifica desequilibrios si la diferencia entre CPU y RAM es mayor al **40%** (Rango numérico)[cite: 6, 7].*   **Detección de Anomalías**: Identifica _posibles ataques si un usuario promedia más de **20 procesos**[cite: 6, 7].
_Vulnerabilidad Específica: Evalúa riesgos si el servidor es de "base de datos" o "archivos" **Y** utiliza Windows con el firewall inactivo (Combinación **AND/OR**)[cite: 6, 7].
_Riesgo de Caída: Alerta combinada cuando la memoria RAM y el disco se encuentran simultáneamente en estado crítico[cite: 6].
_Carga Anómala: Detecta posibles procesos colgados o posibles amenazas pro el exeso de consumo si el consumo de CPU por usuario individual supera el **45%**.

#  Flujo de Decisión
El sistema opera bajo un flujo secuencial para garantizar la integridad de los resultados

_Validación de Credenciales: Un bucle while asegura que los datos de acceso (Admin, Servidor, SO) sean correctos antes de iniciar
_Entrada y Validación: Se solicitan 10 variables (5 numéricas, 3 categóricas, 2 cadenas) validadas mediante el módulo de funciones_de_validacion.py
_Cálculo de Variables Derivadas: Se procesan datos como "procesos por usuario" para profundizar el análisis
_Contador de Riesgos**: Por cada regla incumplida, se incrementa un contador que define el nivel de estado
    0 Riesgos: Servidor en buen estado.
    1 - 2 Riesgos: Fuera de lo normal.
    3 - 4 Riesgos: Estado de Alerta/Elevado.
    5 o más: Estado Crítico.

# Ejemplo de Salida
El informe final utiliza f-strings para presentar un diagnóstico detallado con problemas y soluciones:

_DATOS INGRESADOS: 
uso de cpu: 95% 
uso de ram: 40% 
espacio libre en disco: 25.0 GB
cantidad de usuarios conectados: 2
cantidad de procesos activos: 80
sistema operativo: windows
estado del firewall: inactivo

 ATENCION: SERVIDOR EN ESTADO CRITICO
         DIAGNOSTICO DE SERVIDOR

------------------------------
[ CPU ]
Riesgo: critico | CUIDADO
Problema: sobrecarga en CPU. | CPU: 95% cuello de botella respecto a RAM: 40% Diferencia de: 55% de uso)
Recomendación: optimizar el consumo del CPU. | COMPRE UNA MEJOR RAM

------------------------------
[ PROCESOS Y USUARIOS ]
USUARIOS:  | CUIDADO | ALERTA: Carga anómala. Cada usuario consume 47.5% de CPU. Posible proceso colgado. | El usuario promedio tiene 40.0 procesos. Posible ataque cibernetico o fuga de hilos.
Recomendación:  / eliminar usuarios inactivos.

------------------------------
[ ALMACENAMIENTO ]
Riesgo: critico
Problema: EL ALMACENAMIENTO ESTA POR AGOTARSE
Recomendación: Aumentar capacidad de almacenamiento o eliminar archivos.

------------------------------
[ SEGURIDAD - FIREWALL ]
Riesgo: critico
Problema: El firewall esta desactivado.
Recomendación: Activar el firewall y revisar el servidor por posibles amenazas.

!!!!!!!!!!!!!!!!!
ALERTAS DEL SISTEMA: cuidado el servior de tipo: base de datos esta vulnerable a ataques de windows