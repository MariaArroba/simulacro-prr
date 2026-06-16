import unittest
from mensaje import procesar

class TestMensaje(unittest.TestCase):

    def test_comando_desconocido_error(self):
        frases = ['una frase']
        respuesta = procesar('HOLA', frases)
        self.assertEqual(respuesta, 'ERROR')

if __name__ == '__main__':
    unittest.main()
