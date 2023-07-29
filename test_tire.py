from unittest import TestCase
from Tire import Carrigan, Octoprime

class TestTire(TestCase):
    def test_carrigan(self):
        # Arrange
        data = [0.9, 0.3, 0.4, 0.5]
        carrigan = Carrigan(data)

        # Act
        result = carrigan.needs_service()

        # Assert
        self.assertTrue(result)

    def test_octoprime(self):
        # Arrange
        data = [0.9, 0.3, 0.4, 0.5]
        octoprime = Octoprime(data)

        # Act
        result = octoprime.needs_service()
        

        # Assert
        self.assertFalse(result)