import json
import os

RUTA_ARCHIVO = "tareas.json"

def cargar_tareas():
    """
    Carga las tareas desde un archivo JSON.

    Retorna:
        list: Lista de tareas. Si el archivo no existe o está vacío, retorna [].
    """
    if not os.path.exists(RUTA_ARCHIVO):
        return []

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def guardar_tareas(tareas):
    """
    Guarda las tareas en un archivo JSON.

    Parámetros:
        tareas (list): Lista de tareas a guardar.
    """
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)
