from core.logica_de_tareas import agregar_tarea, completar_tarea, eliminar_tarea
from storage.tareas_storage import cargar_tareas, guardar_tareas

def mostrar_tareas(tareas):
    print("\n=== LISTA DE TAREAS ===")
    if not tareas:
        print("No hay tareas todavía.")
        return

    for i, tarea in enumerate(tareas):
        estado = "✔️  " if tarea["completada"] else "❌ "
        print(f"{i}. {tarea['descripcion']} [{estado}]")


def menu(tareas):
    while True:
        print("\n" + "═" * 50)
        print("               📝  MENÚ DE TAREAS")
        print("═" * 50)

        print("  1) ➕  Agregar tarea")
        print("  2) ✔️  Completar tarea")
        print("  3) ❌  Eliminar tarea")
        print("  4) 📄  Mostrar tareas")
        print("  0) 🚪  Salir")
        print("─" * 50)

        opcion = input("Seleccione una opción > ").strip()
        print()

        # AGREGAR
   
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            agregar_tarea(tareas, descripcion)
            guardar_tareas(tareas)
            print("✔️  Tarea agregada y guardada.💾")

        # COMPLETAR

        elif opcion == "2":
            try:
                indice = int(input("Número de tarea a completar: "))
                if completar_tarea(tareas, indice):
                    print("✔️  Tarea completada.")
                    guardar_tareas(tareas)
                else:
                    print("⚠️  Índice inválido.")
            except ValueError:
                print("⚠️  Debes ingresar un número válido.")

        # ELIMINAR
        
        elif opcion == "3":
            try:
                indice = int(input("Número de tarea a eliminar: "))
                if eliminar_tarea(tareas, indice):
                    print("🗑️  Tarea eliminada.")
                    guardar_tareas(tareas)
                else:
                    print("⚠️  Índice inválido.")
            except ValueError:
                print("⚠️  Debes ingresar un número válido.")

        # MOSTRAR
        
        elif opcion == "4":
            mostrar_tareas(tareas)

        # SALIR
        
        elif opcion == "0":
            print("💾 Guardando antes de salir...")
            guardar_tareas(tareas)
            print("Saliendo del programa... 👋")
            break

        # OPCIÓN INVÁLIDA
        
        else:
            print("⚠️  Opción inválida, intente de nuevo.")


#  PROGRAMA PRINCIPAL

def main():
    tareas = cargar_tareas()
    if tareas is None:
        tareas = []

    menu(tareas)


if __name__ == "__main__":
    main()
