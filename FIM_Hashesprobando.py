import hashlib
import json
import os

def calcular_hash(ruta):
    sha256 = hashlib.sha256()

    with open(ruta, "rb") as archivo:
        while chunk := archivo.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

archivos = [
    "archivos/config.txt",
    "archivos/sistema.ini",
    "archivos/passwords.txt"
]

# Primera ejecución
if not os.path.exists("hashes.json"):

    datos = {}

    for archivo in archivos:
        datos[archivo] = calcular_hash(archivo)

    with open("hashes.json", "w") as f:
        json.dump(datos, f, indent=4)

    print("Hashes registrados correctamente.")
    print("Vuelve a ejecutar el programa para verificar integridad.")

# Verificación
else:

    with open("hashes.json", "r") as f:
        hashes_guardados = json.load(f)

    print("Revisando integridad de los archivos...\n")

    for archivo, hash_original in hashes_guardados.items():

        hash_actual = calcular_hash(archivo)

        if hash_actual == hash_original:
            print(f"[OK] {archivo} - Sin cambios")
        else:
            print(f"[ALERTA] {archivo} - ¡EL ARCHIVO FUE MODIFICADO!")