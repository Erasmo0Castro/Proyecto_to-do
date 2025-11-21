from core.logica_de_tareas import agregar_tarea, completar_tarea, eliminar_tarea
from storage.tareas_storage import cargar_tareas, guardar_tareas

def mostrar_tareas(tareas):
    print("\n=== LISTA DE TAREAS ===")
    if not tareas:
        print("No hay tareas todavía.")
        return

    for i, tarea in enumerate(tareas):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i}. {tarea['descripcion']} [{estado}]")

def main():
    tareas = cargar_tareas()

    while True:
        mostrar_tareas(tareas)
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Completar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            agregar_tarea(tareas, descripcion)
            guardar_tareas(tareas)

        elif opcion == "2":
            indice = int(input("Número de tarea a completar: "))
            if completar_tarea(tareas, indice):
                print("Tarea completada.")
                guardar_tareas(tareas)
            else:
                print("Índice inválido.")

        elif opcion == "3":
            indice = int(input("Número de tarea a eliminar: "))
            if eliminar_tarea(tareas, indice):
                print("Tarea eliminada.")
                guardar_tareas(tareas)
            else:
                print("Índice inválido.")

        elif opcion == "4":
            print("Saliendo...")
            guardar_tareas(tareas)
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
