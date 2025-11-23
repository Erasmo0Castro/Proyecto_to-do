def menu(tareas):
    ''' INTERFAZ INTERACTIVA DE USUARIO'''

    while True:
        print('---------------------------------')
        print('         MENU DE TAREAS         -')
        print('1.   Agregar tarea-------------->')
        print('2.   Completar tarea------------>')
        print('3.   Eliminar tarea------------->')
        print('4.   Mostrar tarea-------------->')
        print('5.   Guardar tarea-------------->')
        print('6.   argar tareas--------------->')
        print('0.   Salir---------------------->')
        print('-------------------------------->')

        opcion = input('Seleccionar una opcion > ').strip()

        if opcion not in ['1','2','3','4','5','6']:
            print('Opcion invalidad. Intente nuevamente')
            continue

        if opcion == '1':
            # Jesimiel -------------- > agregar_tarea()
            continue
        elif opcion == '2':
            # Jesimiel ----------------> completar_tarea()
            continue
        elif opcion =='3':
            # Jesimiel -------------- > eliminar_tarea()
            continue
        elif opcion == '4':
            # Jeimy -----------------> mostrar_tarea()
            print('Tarea guardadas con con exito')
        elif opcion == '5':
            # Yogendry ----------------> guarda_tarea()
            continue
        elif opcion =='6':
            # Yogendry ----------------> cargar()
            # nuevas = cargar_tareas()
            # if nuevas is not none:
            #   tareas.clear()
            #   tareas.extend(nuevas)
            #   print('Tareas cargadas correctamente')
            continue
        elif opcion == '0':
            print('Saliendo del programa')
            break

