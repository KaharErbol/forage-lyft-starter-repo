from unittest import TestCase
from CarFactory import CarFactory


"""
Car Model       Engine	       Battery
Calliope	Capulet Engine	Spindler Battery

"""


class TestCar(TestCase):
    def test_calliope(self):
        # Arrange
        create_car = CarFactory()
        
        current_date = '2023-7-29'
        last_service = '2020-01-01'
        curr_mileage = 50000
        last_mileage = 20000

        calliope = create_car.create_calliope(
            current_date=current_date,
            last_service_date=last_service,
            current_mileage=curr_mileage,
            last_service_mileage=last_mileage
            )

        # Act
        result = calliope.needs_service()

        # Assert
        self.assertEqual(result, True)