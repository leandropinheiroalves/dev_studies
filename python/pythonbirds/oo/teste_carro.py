from unittest import TestCase

from python.pythonbirds.oo.carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_incial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
