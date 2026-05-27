==============================
SRE, Site Reliability Engineer
==============================

Prototipo D
===========

Rol de Administrador de Sistemas Senior / "Site Reliability Engineer" (SRE) puro

* **El Rol Interlocutor**: Platform Engineer / SysAdmin Manager.
* **Su obsesión**: Mantenimiento a largo plazo, estabilidad del sistema operativo y que el código de automatización sea limpio.
* **enfoque**:

-----

1. El "Pitch" Inicial (Tu Presentación)
=======================================

``>>`` **Pregunta**: *"Háblame de ti y de tu trayectoria reciente."*

``>>`` **Respuesta**: "Hola, buenas. Soy Raúl Vílchez, Administrador de Sistemas Linux orientado a la fiabilidad, predictibilidad y rendimiento de la infraestructura crítica.

En mi trayectoria reciente, me he especializado en el diseño de plataformas deterministas de alto rendimiento, asegurando que cada capa del stack sea escalable y observable. En el ámbito del almacenamiento y la virtualización con libvirt/KVM, trabajo optimizando el stack del kernel mediante la implementación de VDO directamente sobre bloques NVMe, gestionando el aprovisionamiento fino con LVM de forma segura y controlando los ciclos de descarte de bloques (fstrim) para evitar la degradación del rendimiento físico.

En cuanto a la gestión de identidad, opero arquitecturas de alta disponibilidad Maestro-Réplica con FreeIPA, controlando las colas de replicación LDAP a bajo nivel y garantizando la consistencia de Kerberos mediante la mitigación de derivas temporales con clústeres redundantes de chronyd.

Mi filosofía operativa se basa en que la infraestructura debe ser tratada como código fuente. Automatizo tareas mediante scripts modulares en Python y Bash que interactúan con la CLI nativa y delegan en systemd y journald, evitando demonios centralizados innecesarios y puntos únicos de fallo como ocurre con Docker tradicional. Gestiono todo bajo Git con Pull Requests, revisiones por pares y documentación de ingeniería compilada con Sphinx de forma automatizada. Busco integrarme en su equipo porque sé que valoran el purismo técnico, el control total sobre el sistema operativo y la resiliencia de la plataforma."



2. Bloque Técnico: Gestión de Identidad y Seguridad (Tu pilar fuerte)
=====================================================================

``>>`` **Pregunta:** *"Veo que has montado una arquitectura Maestro-Réplica con FreeIPA/Red Hat IdM. ¿Cómo gestionas la consistencia, la replicación y qué problemas has tenido con la sincronización de Kerberos o PKI?"*

``>>`` **Respuesta**: "Operar FreeIPA en producción bajo una arquitectura Maestro-Réplica implica gestionar la consistencia a nivel de topología de replicación del motor 389 Directory Server. Para garantizar la consistencia, evitamos topologías en anillo plano y diseñamos arquitecturas en malla con acuerdos de replicación multimáster cruzados. Esto nos permite monitorizar el retraso de replicación (replication lag) y mitigar los conflictos de modificación de atributos LDAP mediante la resolución nativa de colisiones basada en marcas de tiempo y vectores de modificación.

A nivel de Kerberos, el principal reto operativo es la ventana de tolerancia de sincronización de tickets. Una deriva temporal superior a 5 minutos rompe la autenticación de la plataforma. Para solucionarlo de raíz, desacoplamos la dependencia de redes externas implementando un clúster local de chronyd con fuentes de tiempo redundantes de estrato bajo, asegurando un jitter mínimo y una convergencia horaria constante en todos los nodos.

Respecto a la PKI (Dogtag), la consistencia en el intercambio de certificados de subsistema es crítica. Gestionamos la renovación de las CAs y los certificados de agente mediante agentes de seguimiento locales como certmonger. El nodo maestro inicial retiene el rol de renovación de la autoridad de certificación principal para evitar condiciones de carrera en la base de datos de Dogtag, y monitorizamos las colas de replicación de certificados (RUV - Replica Update Vectors) para asegurar la consistencia del catálogo antes de que afecte a la validación TLS de los clientes de la infraestructura."


3. Bloque Técnico: Almacenamiento y Virtualización
==================================================

``>>`` **Pregunta:** *"¿Por qué decidiste implementar VDO (Virtual Data Optimizer) sobre LVM en tu entorno de virtualización? ¿Qué tasas de deduplicación/compresión has conseguido y cómo afecta esto al rendimiento de IOPS en discos NVMe?"*

``>>`` **Respuesta**: "A nivel de ingeniería de sistemas y fiabilidad, la implementación de VDO (Virtual Data Optimizer) se diseñó respetando estrictamente el orden del stack de almacenamiento en Linux: colocamos VDO directamente sobre los volúmenes físicos NVMe y, por encima de él, gestionamos el volumen lógico con LVM para aprovisionar las instancias de libvirt. Esto nos permite aislar la lógica de la deduplicación y la compresión por debajo de la capa de asignación flexible de almacenamiento.  

Abordar el uso de VDO sobre NVMe requiere entender el impacto en los IOPS debido a la serialización de las escrituras durante la fase de cálculo de hashes de bloques. Para mitigar la latencia, ajustamos el tamaño de la caché de bloques en memoria RAM y dimensionamos los hilos de procesamiento (vdo_bio) para balancear la carga de la CPU sin ahogar el bus PCIe.

El mayor riesgo operativo del Thin Provisioning con VDO es el agotamiento del espacio físico real. Para mitigar esto, implementamos una política rigurosa de monitorización mediante scripts que reportan métricas directas a través de vdostats. Además, automatizamos la ejecución controlada de comandos de descarte de bloques (fstrim/discard) desde los sistemas de archivos de las máquinas virtuales hacia el host, asegurando que el espacio liberado sea devuelto eficientemente al pool físico de VDO y evitando desbordamientos catastróficos en producción."



4. Bloque DevOps y Automatización
=================================

* El enfoque para la Respuesta 4: Aquí venderemos el control total del entorno. Explicarás cómo la combinación de herramientas Unix nativas junto con tus scripts evita la "magia negra" de Docker, aislando los procesos por usuario y facilitando la resolución de problemas (troubleshooting) con herramientas estándar de Linux.

``>>`` **Pregunta:** *"Mencionas el uso de Podman en entornos Rootless. ¿Por qué elegiste Podman sobre Docker para tus contenedores y qué ventajas de seguridad te aporta?"*

``>>`` **Respuesta**: "Para un perfil enfocado en la estabilidad de la plataforma y la fiabilidad del sistema, la arquitectura daemonless de Podman es una evolución lógica frente a Docker. Al eliminar el demonio central, eliminamos un punto único de fallo (Single Point of Failure); si el proceso de gestión de Docker se cuelga o se satura, puede arrastrar a los contenedores que dependen de él. Con Podman, cada contenedor es simplemente un proceso hijo directo del usuario que lo lanzó.

Esta arquitectura se alinea perfectamente con las herramientas nativas de Linux. En lugar de depender de una API externa para controlar los contenedores, utilizo scripts en Python y Bash que interactúan con la CLI, y delego la gestión del ciclo de vida en systemd a nivel de usuario. Esto significa que puedo aplicar políticas de reinicio estándar, gestionar límites de recursos con cgroups de forma limpia y, lo más importante, la observabilidad es directa: los logs van a journald y los procesos se pueden monitorizar con herramientas estándar del sistema como ps, top o htop. No hay capas ocultas, lo que reduce drásticamente el tiempo de diagnóstico y resolución de incidentes en producción."


5. Pregunta de Situación / Metodología (Soft Skills + Hard Skills)
==================================================================

``>>`` **Pregunta:** *"Veo que gestionas tu propio laboratorio de alto rendimiento y aplicas flujos de Git avanzados (Pull Requests, Code Review). ¿Cómo trasladas esta cultura de desarrollo al mundo de la administración de sistemas?"*

``>>`` **Respuesta**: "Trasladar las metodologías de desarrollo a las operaciones de sistemas es la única vía para garantizar el determinismo, la observabilidad y la reproducibilidad de la plataforma. En mi infraestructura, sigo un principio estricto de 'Configuración como Código': ningún cambio se realiza de manera imperativa o interactiva en los servidores; todo se declara y se gestiona a través de repositorios Git.

Aplicar flujos de Pull Requests y Code Review a nuestros scripts de Python y Bash es lo que nos permite mantener la salud del código de automatización. El proceso de revisión por pares no es burocracia, sino una herramienta de diseño técnico que expone errores de lógica, problemas de escalabilidad en scripts o configuraciones inseguras antes de que se ejecuten. Esto convierte el historial de Git en un diario de auditoría técnico inestimable para entender el porqué y el cuándo de cada cambio de infraestructura.

Esta misma rigurosidad la aplico a la ingeniería de documentación con Sphinx y reStructuredText. Rechazo las wikis tradicionales porque sufren de obsolescencia inmediata y no reflejan la realidad del sistema. Al tratar los manuales técnicos como código fuente dentro del mismo repositorio, la documentación se revisa en el mismo Pull Request que la propia infraestructura. Automatizamos el pipeline para que, tras cada merge, se recompile el Hub técnico. Esto garantiza que la documentación sea siempre la única fuente de verdad fidedigna de lo que realmente está corriendo en el host, facilitando diagnósticos rápidos y precisos durante incidentes."

-----

Volver al índice :doc:`/index`.