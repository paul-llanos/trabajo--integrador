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

**Estado:** Crítico  

**Problemas detectados:**
- Sobrecarga de cpu y posible cuello de botella  
- Consumo elevado por usuario (posibles procesos anómalos)  
- Bajo espacio en disco  
- Firewall desactivado  

**Recomendaciones:**
- Optimizar uso de CPU y recursos  
- Revisar procesos y usuarios activos  
- Liberar o ampliar almacenamiento  
- activar el firewall  