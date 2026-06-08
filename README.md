# Monitor de Integridad de Archivos (FIM)

# Descripción

Este proyecto consiste en el desarrollo de un Monitor de Integridad de Archivos (FIM - File Integrity Monitoring) utilizando Python. La herramienta permite detectar modificaciones realizadas sobre archivos monitoreados mediante el uso de funciones hash SHA-256.

El sistema genera una línea base de integridad almacenando los hashes de los archivos seleccionados. Posteriormente, compara los hashes actuales con los previamente registrados para determinar si los archivos han sido modificados.

# Objetivo

Detectar cambios no autorizados en archivos críticos mediante la comparación de hashes SHA-256, permitiendo identificar posibles alteraciones ocasionadas por errores humanos, usuarios malintencionados o software malicioso.

# Tecnologías Utilizadas

* Python
* Librería hashlib
* Librería json
* Librería os

# Estructura del Proyecto

FIM-Hash/
│
├── FIM_Hash.py
├── hashes.json
│
└── archivos/
    ├── config.txt
    ├── passwords.txt
    └── sistema.ini

# Funcionamiento

# Primera ejecución

Si el archivo `hashes.json` no existe, el programa:

1. Calcula el hash de cada archivo monitoreado.
2. Almacena los hashes en `hashes.json`.
3. Crea la línea base de integridad.

Salida esperada:

Hashes registrados correctamente.
Vuelve a ejecutar el programa para verificar integridad.

# Verificación de integridad

Si `hashes.json` ya existe, el programa:

1. Carga los hashes almacenados.
2. Calcula nuevamente los hashes actuales.
3. Compara ambos valores.
4. Informa si los archivos fueron modificados.

Salida esperada:

Revisando integridad de los archivos...

[OK] archivos/config.txt - Sin cambios
[OK] archivos/sistema.ini - Sin cambios
[OK] archivos/passwords.txt - Sin cambios

Si un archivo fue alterado:

Revisando integridad de los archivos...

[ALERTA] archivos/config.txt - ¡EL ARCHIVO FUE MODIFICADO!
[OK] archivos/sistema.ini - Sin cambios
[OK] archivos/passwords.txt - Sin cambios

# Instalación

1. Descargar o clonar el repositorio.

2. Verificar que Python 3.x esté instalado.

```bash
python --version

3. Mantener la estructura de carpetas del proyecto.

# Ejecución

Desde la carpeta del proyecto ejecutar:

```bash
python FIM_Hash.py

# Autor

Jhoel David Huamán Machacca

Proyecto desarrollado como práctica de formación en empresa en el área de Ciberseguridad (Blue Team).
# FIM-HMH
