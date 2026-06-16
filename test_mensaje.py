import unittest
from mensaje import procesar

class TestMensaje(unittest.TestCase):

    def test_comando_desconocido_error(self):
        frases = ['una frase']
        respuesta = procesar('HOLA', frases)
        self.assertEqual(respuesta, 'ERROR')
    def test_total_devuelve_numero_de_frases(self):
        frases = ['uno', 'dos', 'tres']
        respuesta = procesar('TOTAL', frases)
        self.assertEqual(respuesta, 'TOTAL: 3 FRASES')


if __name__ == '__main__':
    unittest.main()
