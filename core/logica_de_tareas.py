
# core/tareas_core.py

def agregar_tarea(tareas, descripcion):
    """
    Agrega una nueva tarea a la lista.

    Parámetros:
        tareas (list): Lista de tareas (cada tarea es un dict).
        descripcion (str): Texto descriptivo de la tarea.

    Estructura de tarea:
        {
            "descripcion": str,
            "completada": bool (false si no está completada es el valor por default)
        }

    Retorna:
        list: La lista modificada.
    """
    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(nueva_tarea)
    return tareas


def completar_tarea(tareas, indice):
    """
    Marca una tarea como completada.

    Parámetros:
        tareas (list): Lista de tareas.
        indice (int): Índice de la tarea a completar (0-based).

    Retorna:
        bool: True si se completó exitosamente, False si el índice es inválido.
    """
    if 0 <= indice < len(tareas): # si el número de índice es válido
        tareas[indice]["completada"] = True
        return True
    return False


def eliminar_tarea(tareas, indice):
    """
    Elimina una tarea de la lista.

    Parámetros:
        tareas (list): Lista de tareas.
        indice (int): Índice de la tarea a eliminar (0-based).

    Retorna:
        bool: True si se eliminó correctamente, False si el índice no existe.
    """
    if 0 <= indice < len(tareas): 
        tareas.pop(indice)
        return True
    return False
