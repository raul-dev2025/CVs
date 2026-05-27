===========================
Empresa Tecnológica Mediana
===========================

Prototipo B
===========

Empresa Tecnológica Mediana / Consultora Cloud-Native (En pleno crecimiento)

* **El Rol Interlocutor**: DevOps Lead / Principal Engineer.
* **Su obsesión**: Escalabilidad, consistencia de entornos y migración limpia hacia Kubernetes/OpenShift.
* **Enfoque**:
 
-----

1. El "Pitch" Inicial (Tu Presentación)
=======================================

``>>`` **Pregunta**: *"Háblame de ti y de tu trayectoria reciente."*

``>>`` **Respuesta**: "Hola, qué tal. Soy Raúl Vílchez y me considero un Técnico de Sistemas Linux orientado a la cultura DevOps, especializado en automatización de infraestructura, seguridad de accesos y optimización de entornos locales de alto rendimiento.

En mis proyectos recientes, me he centrado en eliminar la fricción entre el laboratorio de desarrollo y las arquitecturas Cloud-Native. Para ello, diseño entornos de virtualización densos y eficientes utilizando KVM, optimizando el almacenamiento subyacente con VDO sobre NVMe. Además, apuesto firmemente por tecnologías alineadas con los estándares OCI como Podman, automatizando ciclos de vida de contenedores con Python y Bash de forma ligera, e integrando flujos que generan manifiestos listos para Kubernetes.

En cuanto a la gestión de identidad, me gusta estructurar las bases de accesos con FreeIPA/Red Hat IdM, pero pensando en su integración con capas modernas de microservicios mediante federación. Mi fuerte es que aplico una mentalidad puramente de desarrollo a las operaciones: todo mi trabajo se gestiona bajo Git mediante Pull Requests y revisiones de código, y mi infraestructura se auto-documenta compilando dinámicamente con Sphinx. Me entusiasma su consultora porque están en pleno crecimiento escalando plataformas Cloud-Native, y busco aportar esa mentalidad donde sistemas y automatización hablan exactamente el mismo idioma."


2. Bloque Técnico: Gestión de Identidad y Seguridad (Tu pilar fuerte)
=====================================================================

``>>`` **Pregunta:** *"Veo que has montado una arquitectura Maestro-Réplica con FreeIPA/Red Hat IdM. ¿Cómo gestionas la consistencia, la replicación y qué problemas has tenido con la sincronización de Kerberos o PKI?"*

``>>`` **Respuesta**: "En un ecosistema orientado a Cloud-Native, la gestión de identidades no puede ser un silo tradicional; debe funcionar como una plataforma de habilitación dinámica. La arquitectura Maestro-Réplica con FreeIPA se diseñó para proporcionar una fuente de verdad centralizada y de alta disponibilidad, pero pensada para integrarse con flujos modernos de automatización. La consistencia de los datos LDAP se asegura mediante topologías multimáster ágiles, lo que permite que los cambios de políticas o accesos se propaguen de inmediato.

Uno de los mayores desafíos en estos entornos híbridos es unificar la autenticación tradicional basada en Kerberos y LDAP con los stacks de microservicios. Para resolver esto, concebimos FreeIPA como el backbone de seguridad e identidades, exponiendo y cruzando sus datos hacia gestores de identidad modernos como Keycloak mediante federación LDAP. Esto permite mapear roles de sistemas hacia tokens JWT (OIDC/SAML) de forma transparente.

Respecto a la PKI integrada, el foco está en la automatización del ciclo de vida del certificado para evitar fricciones. Utilizamos la API de FreeIPA junto con certmonger para que el aprovisionamiento de certificados internos en nuevos nodos o contenedores pesados sea automático durante el despliegue de la infraestructura, eliminando la gestión manual y asegurando comunicaciones TLS seguras desde el minuto uno en todo el clúster."


3. Bloque Técnico: Almacenamiento y Virtualización
==================================================

``>>`` **Pregunta:** *"¿Por qué decidiste implementar VDO (Virtual Data Optimizer) sobre LVM en tu entorno de virtualización? ¿Qué tasas de deduplicación/compresión has conseguido y cómo afecta esto al rendimiento de IOPS en discos NVMe?"*

``>>`` **Respuesta**: "La elección de implementar VDO (Virtual Data Optimizer) sobre LVM bajo un entorno de virtualización masiva con libvirt responde a la necesidad de maximizar la densidad de VMs y optimizar el uso de hardware de alto rendimiento. En un entorno ágil o de consultoría tecnológica, los laboratorios y entornos de pruebas sufren de una altísima redundancia de datos (mismas imágenes base de sistemas operativos, dependencias replicadas, etc.). VDO ataca este problema directamente reduciendo la huella en disco mediante deduplicación y compresión en tiempo real a nivel de bloque.

Trabajar sobre almacenamiento NVMe nos proporciona un colchón de IOPS excelente, pero para evitar que el procesamiento de VDO se convierta en un cuello de botella para las ráfagas de escritura de las pipelines, la clave está en el tuneo del stack. Configuro el tamaño de los bloques de VDO de forma alineada con los sistemas de archivos de las VMs y dimensiono los hilos de compresión para mantener las latencias bajo mínimos.

El resultado práctico es una arquitectura de Thin Provisioning altamente eficiente: conseguimos ratios de ahorro de almacenamiento muy agresivos, lo que nos permite levantar decenas de entornos efímeros de KVM de forma simultánea, manteniendo la velocidad nativa del almacenamiento de estado sólido y agilizando los ciclos de pruebas y despliegue técnico de los equipos."


4. Bloque DevOps y Automatización
=================================

* **El enfoque para la Respuesta 4**: Aquí destacaremos que Podman genera ficheros YAML listos para Kubernetes (podman generate kube). Tu respuesta se enfocará en que usas Podman porque prepara la infraestructura local para ser migrada a la nube o a orquestadores de manera transparente y sin fricción.

``>>`` **Pregunta**: *"Mencionas el uso de Podman en entornos Rootless. ¿Por qué elegiste Podman sobre Docker para tus contenedores y qué ventajas de seguridad te aporta?"*

``>>`` **Respuesta**: "En un entorno volcado a metodologías Cloud-Native, la consistencia entre el desarrollo local y el orquestador de producción es clave. Opté por Podman porque está diseñado bajo los estándares de la OCI (Open Container Initiative) y, a diferencia de Docker, se integra de forma nativa con el ecosistema de Kubernetes.

Una de las mayores ventajas que aprovecho en mis automatizaciones es la capacidad de Podman para generar y ejecutar manifiestos de Kubernetes directamente desde el entorno local mediante comandos como podman generate kube. Esto reduce drásticamente la fricción al pasar de un contenedor aislado en el laboratorio a un despliegue real en un clúster.

En cuanto a la automatización, utilizo scripts en Python y Bash para orquestar estos entornos locales sin meter la sobrecarga ni la complejidad de un demonio centralizado. Al interactuar directamente con la CLI de Podman, puedo automatizar la creación de Pods locales (un concepto que Docker no maneja de forma nativa), asegurando que la arquitectura de red y el aislamiento de los contenedores repliquen fielmente el comportamiento que luego nos encontraremos en los pipelines de CI/CD y en producción."


5. Pregunta de Situación / Metodología (Soft Skills + Hard Skills)
==================================================================

``>>`` **Pregunta:** *"Veo que gestionas tu propio laboratorio de alto rendimiento y aplicas flujos de Git avanzados (Pull Requests, Code Review). ¿Cómo trasladas esta cultura de desarrollo al mundo de la administración de sistemas?"*

``>>`` **Respuesta**: "Trasladar la cultura de desarrollo al mundo de la infraestructura es la base de mi filosofía de trabajo, aplicando principios de GitOps tanto a las configuraciones como a la documentación técnica. Mi laboratorio de alto rendimiento no se gestiona de forma imperativa; cada entorno virtual de KVM o contenedor de Podman se despliega mediante automatizaciones estructuradas.  

El uso de flujos avanzados de Git, como Pull Requests y Code Review, me permite asegurar la consistencia y la calidad de los scripts de automatización en Python y Bash antes de que toquen el entorno operativo. Esto abre la puerta a dinámicas de integración continua donde los cambios se testean y validan de forma colaborativa, simulando fielmente los flujos de una factoría de software moderna.  

Además, aplico esta misma ingeniería a la documentación mediante Sphinx y reStructuredText. Al tratar los manuales técnicos como código, la documentación se integra en el mismo repositorio de la infraestructura. Automatizo su generación para que, con cada Pull Request aprobado, el Hub de documentación se compile y actualice de forma transparente. Esto garantiza que el conocimiento del equipo evolucione al mismo ritmo que la plataforma, eliminando el desfase entre lo que está desplegado y lo que está documentado."

-----

Volver al índice :doc:`/index`.