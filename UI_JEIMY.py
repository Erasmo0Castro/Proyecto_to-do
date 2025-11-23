#Jeimy


# ---------------------------------------------------------
#  MENÚ PRINCIPAL
# ---------------------------------------------------------

def menu(tareas):
    while True:
        print("\n" + "═" * 45)
        print("           📝  MENÚ DE TAREAS")
        print("═" * 45)

        print("  1) ➕  Agregar tarea")
        print("  2) ✔️  Completar tarea")
        print("  3) ❌  Eliminar tarea")
        print("  4) 📄  Mostrar tareas")
        print("  5) 💾  Guardar tareas")
        print("  6) 📂  Cargar tareas")
        print("  0) 🚪  Salir")
        print("─" * 45)

        opcion = input("Seleccione una opción > ").strip()
        print()

        if opcion == '1':
            agregar_tarea(tareas)

        elif opcion == '2':
            completar_tarea(tareas)

        elif opcion == '3':
            eliminar_tarea(tareas)

        elif opcion == '4':
            mostrar_tareas(tareas)

        elif opcion == '5':
            guardar_tareas(tareas)

        elif opcion == '6':
            nuevas = cargar_tareas()
            if nuevas is not None:
                tareas.clear()
                tareas.extend(nuevas)

        elif opcion == '0':
            print("Saliendo del programa... 👋")
            break

        else:
            print("⚠️  Opción inválida, intente de nuevo.")


# ---------------------------------------------------------
#  PROGRAMA PRINCIPAL
# ---------------------------------------------------------

if __name__ == "__main__":
    tareas = []
    menu(tareas)