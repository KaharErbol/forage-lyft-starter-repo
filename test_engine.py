from unittest import TestCase
from Engine import CapuletEngine, WilloughbyEngine, SternmanEngine

"""
Capulet Engine	Once every 30,000 miles
Willoughby Engine	Once every 60,000 miles
Sternman Engine	Only when the warning indicator is on

"""

class TestEngines(TestCase):
    def test_capulet(self):
        # Arrange
        last_service_mileage = 10000
        current_mileage = 50000
        capulate = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        # Act
        result = capulate.needs_service()


        # Assert
        self.assertEqual(result, True)

    def test_willoughby(self):
        # Arrange
        last_service_mileage = 10000
        current_mileage = 50000
        willoughby = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)

        # Act
        result = willoughby.needs_service()

        # Assert
        self.assertEqual(result, False)

    def test_sternman(self):
        # Arrange
        warning = True
        sterman = SternmanEngine(warning_light_on=warning)

        # Act
        result = sterman.needs_service()

        # Assert
        self.assertEqual(result, True)

# Command for running the test
# python -m unittest -v test_engine