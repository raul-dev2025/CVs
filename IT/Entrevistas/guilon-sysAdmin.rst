==============
Guión SysAdmin
==============

Perfil técnico equilibrado entre la administración de sistemas tradicional ("**SysAdmin puro**") y la evolución hacia metodologías modernas (**Cloud/DevOps**, automatización y optimización de recursos).

-----

1. El "Pitch" Inicial (Tu Presentación)
=======================================

``>>`` **Pregunta:** *"Háblame de ti y de tu trayectoria reciente."*

* **Enfoque de respuesta:** No repitas el CV cronológicamente. Enfócate en tu capacidad para resolver problemas complejos de infraestructura.
* **Guion sugerido:** Destaca que eres un especialista en infraestructura Linux con un fuerte enfoque en la **eficiencia** (optimización de almacenamiento) y la **seguridad/centralización** (IdM/FreeIPA), que además utiliza la programación (Python/Bash) para automatizar y evitar tareas repetitivas.

-----

2. Bloque Técnico: Gestión de Identidad y Seguridad (Tu pilar fuerte)
=====================================================================

``>>`` **Pregunta:** *"Veo que has montado una arquitectura Maestro-Réplica con FreeIPA/Red Hat IdM. ¿Cómo gestionas la consistencia, la replicación y qué problemas has tenido con la sincronización de Kerberos o PKI?"*

* **Enfoque de respuesta:** Aquí buscan profundidad. Habla de cómo manejas los conflictos de replicación, la importancia de la sincronización horaria (NTP) para Kerberos, y cómo gestionas el ciclo de vida de los certificados (PKI). Demuestra que entiendes el impacto de que este servicio caiga (infraestructura crítica).

-----

3. Bloque Técnico: Almacenamiento y Virtualización
==================================================

``>>`` **Pregunta:** *"¿Por qué decidiste implementar VDO (Virtual Data Optimizer) sobre LVM en tu entorno de virtualización? ¿Qué tasas de deduplicación/compresión has conseguido y cómo afecta esto al rendimiento de IOPS en discos NVMe?"*

-----

4. Bloque DevOps y Automatización
=================================

``>>`` **Pregunta:** *"Mencionas el uso de Podman en entornos Rootless. ¿Por qué elegiste Podman sobre Docker para tus contenedores y qué ventajas de seguridad te aporta?"*

``>>`` **Respuesta:** "La decisión de elegir Podman sobre Docker se basó principalmente en el principio de privilegio mínimo y la reducción de la superficie de ataque.  

Al trabajar en entornos Rootless, eliminamos por completo la necesidad de un demonio con privilegios de root (dockerd) corriendo en el sistema. Si un contenedor se ve comprometido en un entorno Docker tradicional, el atacante tiene una vía directa para escalar privilegios hacia el host a través del socket Unix del demonio. Con Podman Rootless, el proceso del contenedor corre bajo el UID del usuario que lo lanza, mitigando este riesgo drásticamente.  

Respecto a la automatización, integro este flujo mediante Python y Bash Scripting. En lugar de depender de herramientas pesadas, utilizo scripts que interactúan directamente con la CLI de Podman (aprovechando que los comandos son un drop-in replacement de Docker) o mediante systemd para gestionar el ciclo de vida de los contenedores como servicios del sistema a nivel de usuario. Esto me permite un despliegue predecible, ligero y alineado con los flujos de control de versiones de Git."  

-----

5. Pregunta de Situación / Metodología (Soft Skills + Hard Skills)
==================================================================

``>>`` **Pregunta:** *"Veo que gestionas tu propio laboratorio de alto rendimiento y aplicas flujos de Git avanzados (Pull Requests, Code Review). ¿Cómo trasladas esta cultura de desarrollo al mundo de la administración de sistemas?"*

* **Enfoque de respuesta:** Esto demuestra tu mentalidad **DevOps/GitOps**. Explica que para ti, la infraestructura y la documentación (mencionando tu Hub con Sphinx/rST) se tratan como código: se revisan, se versionan y se testean antes de darles luz verde.

 
-----

Volver al índice :doc:`/index`.