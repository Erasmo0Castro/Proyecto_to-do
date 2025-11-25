import unittest
import core.logica_de_tareas as logica_de_tareas

#Para correr el test usar en la terminal desde la raiz del proyecto: python -m unittest test.test_integracion

#Prueba cómo interactúan las funciones juntas sin usar el menú.
class TestIntegracion(unittest.TestCase):

    def test_flujo_completo(self):
        tareas = []

        # Agregar
        logica_de_tareas.agregar_tarea(tareas, "Tarea 1")
        logica_de_tareas.agregar_tarea(tareas, "Tarea 2")
        self.assertEqual(len(tareas), 2)

        # Completar
        logica_de_tareas.completar_tarea(tareas, 0)
        self.assertTrue(tareas[0]["completada"])

        # Eliminar
        logica_de_tareas.eliminar_tarea(tareas, 1)
        self.assertEqual(len(tareas), 1)

        # Confirmar estados finales
        self.assertEqual(tareas[0]["descripcion"], "Tarea 1")
        self.assertTrue(tareas[0]["completada"])


if __name__ == "__main__":
    unittest.main()


