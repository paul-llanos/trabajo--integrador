# Sistema de Diagnóstico de Servidores 🖥️

## 📝 Descripción
Sistema de monitoreo avanzado para infraestructura de TI que utiliza un motor de decisiones secuencial para evaluar la salud de los servidores en tiempo real. 

El programa detecta saturaciones críticas en el uso de CPU, RAM y almacenamiento, identificando cuellos de botella y vulnerabilidades de seguridad mediante reglas lógicas cruzadas y análisis heurístico. Su objetivo es transformar métricas complejas en diagnósticos claros y brindar recomendaciones preventivas para garantizar la estabilidad y seguridad operativa del servidor.

---

## 👥 Integrantes
- **Cristian Llanos**

---

## 🎯 Objetivos del Programa
* **Evaluación del Rendimiento:** Analizar las métricas clave de consumo de hardware.
* **Detección de Riesgos:** Identificar de forma temprana anomalías y configuraciones inseguras.
* **Aislamiento de Problemas:** Determinar la causa raíz (individual o cruzada) de las fallas.
* **Recomendaciones de Mitigación:** Brindar soluciones preventivas y correctivas basadas en buenas prácticas de SysAdmin.

---

## 🧠 Lógica de Diagnóstico (Motor de Reglas)
El sistema evalúa el estado de salud del servidor mediante un conjunto de umbrales estrictos y reglas correlacionadas:

### Métricas Individuales 
* **CPU Crítica:** Se activa cuando el uso de CPU supera el 85% (`CPU_MAX`).
* **RAM Crítica:** Se activa cuando el uso de memoria RAM supera el 85% (`RAM_MAX`).
* **Almacenamiento en Riesgo:** Se activa si el espacio disponible en disco baja de 60 GB (`DISCO_DISPONIBLE_MIN`).
* **Saturación de Procesos:** Se activa si los procesos activos superan los 120 (`PROCESOS_MAX`).
* **Saturación de Usuarios:** Se activa si los usuarios concurrentes superan los 50 (`USUARIOS_MAX`).
* **Brecha de Seguridad (Firewall):** Se detecta riesgo alto si el estado del Firewall está en `"inactivo"`.

### Reglas Cruzadas y Correlación de Eventos
* **Cuello de Botella de Hardware:** Detecta asimetría en el rendimiento si existe una diferencia de uso $\ge$ 40% entre la CPU y la RAM (`RAM_CPU_CUELLO_DE_BOTELLA`).
* **Intensidad de CPU por Usuario:** Alerta si el porcentaje promedio de CPU consumido por un único usuario supera el 20% (`MAX_PROCESOS_POR_USER`).
* **Estado Crítico Multivariable (RAM/Disco):** Dispara una alerta de colapso inminente si la RAM y el Disco se encuentran en estado crítico en simultáneo.
* **Sospecha de Ataque (Procesos por Usuario):** Alerta por posible denegación de servicio (DoS) o fuga de hilos si un solo usuario genera más de 40 procesos (`POSIBLE_ATAQUE`).
* **Vulnerabilidad de Entorno Corporativo:** Alerta crítica si el servidor aloja un entorno crítico (`"base de datos"` o `"archivos"`) corriendo sobre Sistema Operativo `"linux"` con el Firewall `"inactivo"`.

---

## 🔀 Arquitectura del Sistema (Flujo de Decisión)
El sistema implementa un patrón de diseño arquitectónico basado en la separación de responsabilidades. Para evitar el desorden de lógica en el punto de entrada, **los distintos módulos de tareas individuales (`inputs`, `output`, `reglas`, `calculos`, `funciones_de_validacion`) se agrupan y centralizan en un único módulo coordinador llamado `integracion_de_tareas.py`**.

Este módulo de integración actúa como un orquestador que encapsula la complejidad del sistema y **divide el programa en 4 etapas limpias y secuenciales para el `main.py`**. La comunicación entre estas etapas se realiza mediante un pasaje de parámetros explícito a través de tuplas nativas, manteniendo la integridad de los datos sin recurrir a variables globales.

```text
[main.py] (Coordinador Principal)
│
├──➔ 1. etapa_bienvenida_y_login() ➔ Retorna (sistema_operativo, tipo_servidor)
│
├──➔  if iniciar_sistema() == "si"
│         │
│         ├──➔ 2. etapa_carga_de_datos(sistema_operativo) ➔ Retorna (datos_ingresados)
│         │
│         ├──➔ 3. etapa_ejecucion_del_diagnostico(datos_ingresados, sistema_operativo, tipo_servidor) ➔ Retorna (resultados)
│         │
│         └──➔ 4. etapa_reporte_final(resultados_de_diagnostico)
│
└──➔ else: mostrar_salida_del_sistema()
```
1. **PRIMERA ETAPA: Bienvenida y Login**
Muestra la interfaz inicial y gestiona el bucle de credenciales.
Una vez validada la autenticación, exporta el entorno del servidor (`sistema_operativo` y `tipo_servidor`) hacia el bloque principal.

2. **SEGUNDA ETAPA: Carga de Datos**
Recibe el sistema operativo actual para su posterior renderizado y solicita al operador las métricas actuales de hardware (CPU, RAM, Disco) y red.
Almacena y empaqueta estos valores en una tupla nativa limpia (`datos_ingresados`).

3. **TERCERA ETAPA: Diagnóstico (Motor de Reglas)**
Toma la tupla de métricas junto con el contexto del servidor obtenido en el login.
Ejecuta de forma secuencial las verificaciones individuales y las reglas cruzadas para correlacionar eventos (como cuellos de botella o sospechas de ataques), devolviendo la tupla con los veredictos (`resultados_de_diagnostico`).

4. **CUARTA ETAPA: Reporte Final**
Recibe los resultados analíticos, los desempaqueta posicionalmente y los envía a la interfaz de salida para imprimir en consola los riesgos, problemas detectados y las recomendaciones técnicas de mitigación.

---

## 📋 Ejemplo de Salida en Consola

### Datos Ingresados:
* **Hardware:** CPU: 95% | RAM: 40% | Disco: 25 GB
* **Concurrencia:** Usuarios: 2 | Procesos: 80
* **Entorno:** SO: linux | Firewall: Inactivo

### Reporte Generado:
```text
[ CPU ]
Riesgo: CRÍTICO | CUIDADO
Problema: Sobrecarga en CPU. CPU al 95% genera cuello de botella respecto a RAM al 40% (Diferencia del 55%).
Recomendación: Optimizar el consumo de procesos de la CPU o actualizar módulos de memoria RAM.

------------------------------
[ PROCESOS ]
Riesgo: ALERTA | CUIDADO
Problema: El promedio de PROCESOS de cada usuario es de 40.0. Posible ataque cibernético o fuga de hilos.
Recomendación: Realizar una auditoría de hilos activos en el servidor para asegurar la estabilidad.

------------------------------
[ USUARIOS ]
Riesgo: ALERTA | CUIDADO
Problema: Carga anormal. Cada usuario consume un promedio de 47.5% de CPU. Sospecha de proceso malicioso.
Recomendación: Investigar los identificadores de procesos (PID) asociados a ese usuario de inmediato.

------------------------------
[ ALMACENAMIENTO ]
Riesgo: CRÍTICO
Problema: EL ALMACENAMIENTO ESTÁ POR AGOTARSE por debajo del mínimo seguro.
Recomendación: Aumentar la capacidad de almacenamiento o purgar archivos temporales / logs antiguos.

------------------------------
[ SEGURIDAD - FIREWALL ]
Riesgo: CRÍTICO
Problema: El firewall perimetral está desactivado de forma insegura.
Recomendación: Activar las reglas de iptables/ufw y revisar el servidor por posibles vectores de intrusión.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ALERTAS DE INFRAESTRUCTURA: El servidor de tipo [BASE DE DATOS] se encuentra altamente 
vulnerable a ataques en entornos bajo el sistema operativo [LINUX].
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
