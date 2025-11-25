import unittest
from core.logica_de_tareas import agregar_tarea, completar_tarea, eliminar_tarea
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


#Para correr el test usar en la terminal desde la raiz del proyecto: python -m unittest test.test_tareas_core 

class TestTareasCore(unittest.TestCase):

    def test_agregar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar Python")

        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["descripcion"], "Estudiar Python")
        self.assertFalse(tareas[0]["completada"])

    def test_completar_tarea_valida(self):
        tareas = [{"descripcion": "A", "completada": False}]
        resultado = completar_tarea(tareas, 0)

        self.assertTrue(resultado)
        self.assertTrue(tareas[0]["completada"])

    def test_completar_tarea_invalida(self):
        tareas = [{"descripcion": "A", "completada": False}]
        resultado = completar_tarea(tareas, 5)

        self.assertFalse(resultado)
        self.assertFalse(tareas[0]["completada"])

    def test_eliminar_tarea_valida(self):
        tareas = [{"descripcion": "A", "completada": False}]
        resultado = eliminar_tarea(tareas, 0)

        self.assertTrue(resultado)
        self.assertEqual(len(tareas), 0)

    def test_eliminar_tarea_invalida(self):
        tareas = [{"descripcion": "A", "completada": False}]
        resultado = eliminar_tarea(tareas, 3)

        self.assertFalse(resultado)
        self.assertEqual(len(tareas), 1)


if __name__ == "__main__":
    unittest.main()
