# Sistema de Diagnóstico de Servidores 
## **Descripcion**
Sistema orientado a la detección de fallas, cuellos de botella y vulnerabilidades en servidores mediante un motor de decisiones basado en reglas lógicas.

---

## **Integrantes**
- Cristian Llanos
- Bryan Vargas

## **Objetivo del Programa**
- Evaluacion del Rendimiento del servidor 
- Detectar Riesgos 
- Generar Alertas
- Brindar Recomendaciones

## **Logica de diagnostico**
El sistema evalúa el estado del servidor mediante un conjunto de reglas que analizan distintas métricas del sistema.
### **Reglas Implementadas**
- Se genera sobrecarga crítica cuando `cpu_usada` o `ram_usada` superan el 85%.
- Se considera estado estable cuando `cpu_usada` y `ram_usada` están en un rango medio de uso.
- Se activa alerta de mantenimiento cuando `espacio_disco` es menor a 60 GB o `procesos_activos`es elevado (or).
- Se detectara el riesgo de seguridad cuando `estado_firewall` está en "inactivo" (Not)
- Se detecta riesgo en servidores de tipo "base de datos" o "archivos" con `espacio_disco` bajo y `ram_usada` elevada.


## **Flujo de Decisión**
El sistema sigue un proceso secuencial para analizar el estado del servidor:

1. **Validación de credenciales**  
   Se utiliza un bucle `while` para verificar que los datos de acceso (administrador, servidor y sistema operativo) sean correctos.

2. **Ingreso y validación de datos**  
   Se solicitan 10 variables (numéricas, categóricas y de texto), las cuales son validadas mediante funciones específicas.

3. **Cálculo de variables derivadas**  
   Se generan valores adicionales, como los procesos por usuario, para mejorar el análisis.

4. **Evaluación de reglas**  
   Se aplican las condiciones del sistema para detectar posibles problemas.

5. **Contador de riesgos**  
   Cada regla cumplida incrementa un contador que determina el estado final del servidor:

   - 0 → Servidor en buen estado  
   - 1 a 2 : Fuera de lo normal  
   - 3 a 4 : Estado de alerta / elevado 
   - 5 o más : Estado crítico  

## **Ejemplo de Salida**

**Datos ingresados:**
CPU: 95% | RAM: 40% | Disco: 25 GB  
Usuarios: 2 | Procesos: 80  
SO: windows | Firewall: Inactivo  

**Salida:**
DATOS INGRESADOS: 

uso de cpu: 95% 
uso de ram: 40% 
espacio libre en disco: 25.0 GB
cantidad de usuarios conectados: 2
cantidad de procesos activos: 80
sistema operativo: linux
estado del firewall: inactivo

------------------------------
  ATENCION: SERVIDOR EN ESTADO CRITICO
         DIAGNOSTICO DE SERVIDOR


------------------------------

[ CPU ]
Riesgo: critico| CUIDADO
Problema: sobrecarga en CPU. |  CPU: 95% cuello de botella respecto a RAM: 40% Diferencia de: 55% de uso)
Recomendación: optimizar el consumo del CPU. | COMPRE UNA MEJOR RAM

------------------------------
[ PROCESOS Y USUARIOS ]
USUARIOS:  | CUIDADO | ALERTA: Carga anormalmala. Cada usuario consume 47.5% de CPU. Posible proceso colgado. |  El usuario promedio tiene 40.0 procesos. Posible ataque cibernetico o fuga de hilos.
Recomendación:  / 

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
