import unittest
from unittest.mock import mock_open, patch
import json
from storage.tareas_storage import cargar_tareas, guardar_tareas, RUTA_ARCHIVO

#Para correr el test usar en la terminal desde la raiz del proyecto: python -m unittest test.test_storage 

class TestStorage(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.path.exists", return_value=True)
    def test_cargar_tareas_archivo_vacio(self, _, mock_file):
        tareas = cargar_tareas()
        self.assertEqual(tareas, [])

    @patch("os.path.exists", return_value=False)
    def test_cargar_tareas_archivo_no_existe(self, _):
        tareas = cargar_tareas()
        self.assertEqual(tareas, [])

    @patch("builtins.open", new_callable=mock_open, read_data='[{"descripcion": "A", "completada": false}]')
    @patch("os.path.exists", return_value=True)
    def test_cargar_tareas_correctamente(self, _, mock_file):
        tareas = cargar_tareas()
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["descripcion"], "A")

    @patch("builtins.open", side_effect=json.JSONDecodeError("err", "doc", 0))
    @patch("os.path.exists", return_value=True)
    def test_cargar_tareas_json_corrupto(self, _, mock_file):
        tareas = cargar_tareas()
        self.assertEqual(tareas, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_guardar_tareas(self, mock_file):
        datos = [{"descripcion": "A", "completada": False}]
        guardar_tareas(datos)

        mock_file.assert_called_once_with(RUTA_ARCHIVO, "w", encoding="utf-8")
        handle = mock_file()
        handle.write.assert_called()  # se escribió algo al archivo


if __name__ == "__main__":
    unittest.main()

'''Aquí probamos:

Guardar JSON

Cargar JSON

Manejo de archivo inexistente

Manejo de JSON corrupto

Todo con mock para no usar el archivo real.'''