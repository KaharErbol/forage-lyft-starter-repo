from unittest import TestCase
from Battery import SpindlerBattery, NubbinBattery
from datetime import datetime

"""
Spindler Battery	Once every 2 years
Nubbin Battery	Once every 4 years

"""

class TestBattery(TestCase):
    def test_spinder(self):
        # Arrange
        last_service_date = datetime.strptime('2020-01-01', '%Y-%m-%d')
        current_date = datetime.today()
        spinder = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)

        # Act
        result = spinder.needs_service()

        # Assert
        self.assertEqual(result, True)

    def test_nubbin(self):
        # Arrange
        last_service_date = datetime.strptime('2020-01-01', '%Y-%m-%d')
        current_date = datetime.today()
        nubbin = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        # Act
        result = nubbin.needs_service()

        # Assert
        self.assertEqual(result, False)