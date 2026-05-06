# Sistema de Diagnóstico de Servidores 

 **Descripcion**
   Sistema de monitoreo avanzado que utiliza un motor de decisiones para evaluar la salud de la infraestructura en tiempo real. El programa detecta saturaciones críticas en el uso de CPU, RAM y almacenamiento, identificando cuellos de botella y vulnerabilidades de seguridad mediante reglas lógicas predefinidas. Su objetivo es transformar métricas complejas en diagnósticos claros y recomendaciones preventivas para garantizar la estabilidad del servidor.
---

## **Integrantes**
- Cristian Llanos
- Bryan Vargas

## **Objetivo del Programa**
- Evaluacion del Rendimiento del servidor 
- Detectar si hay Riesgo
- Detectar el Problema
- Brindar Recomendaciones

## **Logica de diagnostico**
El sistema evalúa el estado del servidor mediante un conjunto de reglas que analizan distintas métricas del sistema.
### **Reglas Implementadas**
- La CPU se considera en Riesgo  cuando la misma supera el 85% `CPU_MAX`
- La RAM Se considera en Riesgo  cuando la misma supera el 85% `RAM_MAX` 
- El ALMACENAMIENTO se considera en Riesgo  cuando la misma esta por debajo de 60 `DISCO_DISPONIBLE_MIN`
- Los PROCESOS se consideran en Riesgo  cuando los mismos superan los 120 procesos `PROCESOS MAX`
- Los USUARIOS se consideran en Riesgo  cuando los mismos superan los 50 usuarios simultaneos `USUARIOS_MAX`
- El FIREWALL se detectara en riesgo de seguridad cuando el `estado_firewall` está en "inactivo" 
- Se detectara riesgo si hay cuello de botella del Hardware (CPU o RAM) si estos tienen una direfencia de uso del 40% `RAM_CPU_CUELLO_DE_BOTELLA`
- Se detectara riesgo en los USUARIOS si es que % de CPU que ocupa un solo usuario es mayor a 20% `MAX_PROCESOS_POR_USER`
- Se detectara riesgo en la RAM o en DISCO si LA RAM Y el DISCO se escuentran en estado CRITICO 
- Se derectara riesgo en los PROCESOS si la canditad de 40 procesos `POSIBLE_ATAQUE` es usada por un solo usuario
- Se detecta riesgo si  (TIPO SERVIDOR = BASE DE DATOS o ARCHIVOS) y (SISTEMA OPERATIVO = LINUX Y FIREWALL = INACTIVO) 


## **Flujo de Decisión**
El sistema sigue un proceso secuencial para analizar el estado del servidor:

1. **Ingreso y validacion de credenciales**  
   Se le pedira al usuario que ingrese el (administrador, servidor, tipo de base de datos y sistema operativo) las mismas  seran validas mediante funciones importadas

2. **Inicio**  
   Se le preguntara al usuario si desea iniciar el diagnotico o salir

3. **Ingreso y validación de datos**  
   Se solicitaran variables referentes al servidor, las cuales son validadas mediante funciones importadas.

4. **Evaluación de reglas**  
   Se aplican las logicas de diagnostico del sistema para detectar problemas y dar soluciones.

5. **Contador de riesgos**  
   Cada regla cumplida incrementa un contador que determina el estado final del servidor:

   - 0 → Servidor en buen estado  
   - 1 a 2 : Fuera de lo normal  
   - 3 a 4 : Estado de alerta
   - 5 o más : Estado crítico  

## **Ejemplo de Salida**

**Datos ingresados:**
CPU: 95% | RAM: 40% | Disco: 25 GB  
Usuarios: 2 | Procesos: 80  
SO: windows | Firewall: Inactivo  


**Datos que muestra:**
------------------------------

[ CPU ]
Riesgo: critico| CUIDADO
Problema: sobrecarga en CPU. |  CPU: 95% cuello de botella respecto a RAM: 40% Diferencia de: 55% de uso
Recomendación: optimizar el consumo del CPU. | COMPRE UNA MEJOR RAM

------------------------------
[  PROCESOS ]
Riesgo:  | CUIDADO
Problema:  |  El el promedio de PROCESOS de cada usuario es 40.0 . Posible ataque cibernetico o fuga de hilos
Recomendación:  | Haga una verificacion del servidor para estar seguro.

------------------------------
[ USUARIOS ]
Riesgo:  | CUIDADO
Problema:  | Carga anormal. Cada usuario consume 47.5% de CPU. Sospecha de ataque cibernetico.
Recomendación:  | investigue a ese usuario.

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

ALERTAS DEL SISTEMA: cuidado el servior de tipo: base de datos esta vulnerable a ataques en este sistema operativo linux

!!!!!!!!!!!!!!!!! 
