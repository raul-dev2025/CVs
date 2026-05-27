===============
Sector Regulado
===============

Prototipo A
===========

La Gran Empresa Tradicional / Sector Regulado (Banca, Seguros, Salud).

* **El Rol Interlocutor**: Infrastructure Manager / CISO (Chief Information Security Officer).
* **Su obsesión**: Seguridad, auditoría, cumplimiento normativo (ISO 27001, ENS) y control de accesos.
* **Enfoque**:

-----

1. El "Pitch" Inicial (Tu Presentación)
=======================================

``>>`` **Pregunta**: *"Háblame de ti y de tu trayectoria reciente."*

``>>`` **Respuesta**: "Hola, buenos días. Soy Raúl Vílchez y me defino como un Administrador de Sistemas Linux especializado en el diseño, despliegue y operación de infraestructura crítica y entornos de alta disponibilidad.

En mi trayectoria reciente, me he enfocado en resolver dos de los mayores retos de cualquier departamento de TI a gran escala: la gobernanza de la seguridad y la eficiencia de los recursos. Por un lado, tengo experiencia robusta implementando arquitecturas centralizadas de gestión de identidades utilizando Red Hat IdM y FreeIPA bajo topologías Maestro-Réplica, asegurando la consistencia de accesos bajo estrictos estándares de seguridad. Por otro lado, me apasiona la optimización del almacenamiento físico mediante tecnologías avanzadas del kernel como VDO y LVM, lo que me permite maximizar la densidad de virtualización sin disparar los costes de hardware.

Lo que me diferencia es mi enfoque metodológico: trato la infraestructura como código. En lugar de configuraciones manuales, aplico flujos de Git avanzados, Pull Requests y Code Reviews para asegurar que todo cambio esté auditado, documentado con Sphinx y libre de errores antes de ejecutarse. Me interesa su compañía porque operan en un sector donde la rigurosidad, el cumplimiento normativo y la tolerancia cero a fallos son críticos, y mi perfil está precisamente alineado con esa cultura operativa."



2. Bloque Técnico: Gestión de Identidad y Seguridad (Tu pilar fuerte)
=====================================================================

``>>`` **Pregunta**: *"Veo que has montado una arquitectura Maestro-Réplica con FreeIPA/Red Hat IdM. ¿Cómo gestionas la consistencia, la replicación y qué problemas has tenido con la sincronización de Kerberos o PKI?"*

``>>`` **Respuesta**: "En un entorno regulado, la gestión de identidades es el corazón de la seguridad de los accesos, por lo que la arquitectura Maestro-Réplica se diseñó bajo un principio estricto de tolerancia a fallos y segregación geográfica. La consistencia de la base de datos LDAP se mantiene mediante topologías de replicación multimáster controladas, evitando bucles y asegurando que las políticas de acceso e identidades estén sincronizadas en tiempo real en todos los nodos.  

El mayor reto crítico en estas arquitecturas es la sincronización de tiempos para Kerberos. Debido a que el protocolo rechaza tickets con un desfase temporal superior a 5 minutos para evitar ataques de denegación o repetición, implementamos políticas rigurosas de sincronización horaria mediante chronyd apuntando a servidores NTP corporativos redundantes y monitorizados.

Respecto a la PKI (Infraestructura de Clave Pública) integrada en FreeIPA, la gestión del ciclo de vida de los certificados se maneja mediante certmonger para automatizar las renovaciones en los hosts clientes. Para mitigar riesgos de consistencia en la replicación de la CA (Certificate Authority), designamos un nodo específico como gestor principal de la renovación de la CA raíz y mantenemos listas de revocación (CRLs) y respuestas OCSP con alta disponibilidad, asegurando que cualquier revocación de credenciales se propague inmediatamente por toda la red para cumplir con las normativas de auditoría interna." 



3. Bloque Técnico: Almacenamiento y Virtualización
==================================================

``>>`` **Pregunta:** *"¿Por qué decidiste implementar VDO (Virtual Data Optimizer) sobre LVM en tu entorno de virtualización? ¿Qué tasas de deduplicación/compresión has conseguido y cómo afecta esto al rendimiento de IOPS en discos NVMe?"*

``>>`` **Respuesta**: "La implementación de VDO (Virtual Data Optimizer) sobre LVM en el entorno de virtualización responde a una estrategia de optimización de costes de almacenamiento bajo un criterio estricto de alta disponibilidad. En arquitecturas masivas con libvirt y KVM, los sistemas operativos de las máquinas virtuales comparten un gran porcentaje de bloques idénticos. Al aplicar deduplicación y compresión en tiempo real a nivel de bloque, logramos optimizar el aprovisionamiento de almacenamiento (Thin Provisioning) de manera muy eficiente.  

En cuanto al rendimiento sobre tecnología NVMe, la prioridad en un sector regulado es mantener una latencia predecible. VDO requiere ciclos de CPU y memoria RAM para calcular los hashes de los bloques y gestionar la compresión. Para mitigar el impacto en los IOPS, la arquitectura se diseñó dimensionando correctamente los hilos de procesamiento dedicados a VDO y asegurando que las escrituras concurrentes no saturasen el bus.  

Además, desde la perspectiva de la gestión de riesgos y la operación, al estar VDO integrado de forma nativa en el stack de almacenamiento de Red Hat/Rocky Linux, garantizamos el cumplimiento de las normativas de soporte técnico empresarial. Todo el entorno se monitoriza de forma rigurosa para evitar el overcommitting crítico de almacenamiento real, asegurando alertas tempranas antes de que el volumen físico se aproxime a su límite operativo."


4. Bloque DevOps y Automatización
=================================

* **El enfoque para la Respuesta 4**: Aquí el argumento estrella es Rootless. Les fascina saber que cumples con el principio de mínimo privilegio de forma nativa sin abrir brechas en el host, y que el ciclo de vida se integra con systemd para que los operadores tradicionales de sistemas puedan auditarlo como cualquier otro servicio Linux.

El entrevistador técnico o el CISO no quieren oír hablar de "lo último que está de moda", sino de reducción de riesgos, auditoría, cumplimiento de normativas y aislamiento.A ellos les preocupa enormemente que un contenedor comprometido comprometa todo el servidor host.

``>>`` **Pregunta:** *"Mencionas el uso de Podman en entornos Rootless. ¿Por qué elegiste Podman sobre Docker para tus contenedores y qué ventajas de seguridad te aporta?"*

``>>`` **Respuesta**: "En un entorno regulado, la prioridad absoluta es mitigar el riesgo de escalada de privilegios y cumplir con el principio de mínimo privilegio. Por ello, la elección de Podman en modo Rootless sobre Docker tradicional es una decisión de arquitectura de seguridad.

Al eliminar por completo el demonio de Docker (dockerd) corriendo como root, neutralizamos el principal vector de ataque en la virtualización de contenedores: si un proceso dentro del contenedor se ve comprometido, el atacante sigue estando confinado al UID de un usuario sin privilegios en el host, impidiendo que tome el control del sistema operativo crítico.  

Desde el punto de vista de la gobernanza y la auditoría, integro este flujo mediante scripts en Python y Bash junto con systemd a nivel de usuario. Esto nos permite tratar los contenedores como servicios estándar del sistema. No dependemos de herramientas de terceros ni de 'cajas negras'; todo el ciclo de vida del contenedor se registra en los diarios nativos de Linux (journald), lo que facilita la centralización de logs y simplifica las auditorías de seguridad e infraestructura sin añadir sobrecostes de rendimiento."

.. note::
   
   * **El enfoque para la Respuesta 4**: Aquí el argumento estrella es Rootless. Les fascina saber que cumples con el principio de mínimo privilegio de forma nativa sin abrir brechas en el host, y que el ciclo de vida se integra con systemd para que los operadores tradicionales de sistemas puedan auditarlo como cualquier otro servicio Linux.

   * El entrevistador técnico o el CISO no quieren oír hablar de "lo último que está de moda", sino de reducción de riesgos, auditoría, cumplimiento de normativas y aislamiento.A ellos les preocupa enormemente que un contenedor comprometido comprometa todo el servidor host.



5. Pregunta de Situación / Metodología (Soft Skills + Hard Skills)
==================================================================

``>>`` **Pregunta:** *"Veo que gestionas tu propio laboratorio de alto rendimiento y aplicas flujos de Git avanzados (Pull Requests, Code Review). ¿Cómo trasladas esta cultura de desarrollo al mundo de la administración de sistemas?"*

``>>`` **Respuesta**: "Trasladar la cultura de desarrollo a la administración de sistemas en un sector regulado no es una cuestión de velocidad, sino de gobernanza y mitigación de riesgos. Para mí, la infraestructura y su documentación técnica son activos que deben gestionarse con el mismo rigor que el código fuente de una aplicación crítica.  

En mi flujo de trabajo, ningún cambio en la configuración de un servidor o en una política de seguridad se realiza directamente en caliente. Todo cambio se define primero de manera estructurada y se somete a un flujo de Pull Requests y Code Review en Git. Esto actúa como un mecanismo natural de segregación de funciones: permite que otros miembros del equipo auditen el impacto técnico, validen que se alinee con las normativas de seguridad y aporten correcciones antes de su aprobación.  

Además, vinculo estrechamente este control de versiones con la documentación mediante Sphinx y reStructuredText. Al tratar la documentación como código, garantizamos que cualquier modificación operativa vaya indisolublemente ligada a su manual técnico actualizado. Si un cambio no está versionado, revisado y documentado bajo estos flujos, no existe. Esto elimina los silos de conocimiento, reduce drásticamente el error humano y proporciona un historial de auditoría impecable para cualquier inspección de cumplimiento normativo."


-----

Volver al índice :doc:`/index`.