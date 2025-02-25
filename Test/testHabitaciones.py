import unittest
from Laberinto.juego import *
from Laberinto.creator import *

class TestHabitaciones(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.juego = Juego()
        self.fm = Creator()
        self.juego.crearLaberinto2HabitacionesFM(self.fm)

    def test_habitaciones(self):
        hab1 = self.juego.obtenerHabitacion(1)
        hab2 = self.juego.obtenerHabitacion(2)

        self.assertIsInstance(hab1, Habitacion)
        self.assertIsInstance(hab2, Habitacion)

        # Asumiendo que los elementos "norte", "sur", "este", "oeste" son atributos de las habitaciones.
        norte = self.fm.fabricarNorte()
        sur = self.fm.fabricarSur()
        este = self.fm.fabricarEste()
        oeste = self.fm.fabricarOeste()

        # Verificar paredes en hab1
        self.assertTrue(hab1.obtenerElementoOr(norte).esPared())
        self.assertTrue(hab1.obtenerElementoOr(este).esPared())
        self.assertTrue(hab1.obtenerElementoOr(oeste).esPared())

        # Verificar paredes en hab2
        self.assertTrue(hab2.obtenerElementoOr(sur).esPared())
        self.assertTrue(hab2.obtenerElementoOr(este).esPared())
        self.assertTrue(hab2.obtenerElementoOr(oeste).esPared())

        # Verificar puertas
        pt12 = hab1.obtenerElementoOr(sur)
        self.assertTrue(pt12.esPuerta())
        self.assertTrue(hab2.obtenerElementoOr(norte).esPuerta())
        self.assertFalse(pt12.abierta)

if __name__ == "__main__":
    unittest.main()