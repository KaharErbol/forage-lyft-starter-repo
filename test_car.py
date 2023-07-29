from unittest import TestCase
from CarFactory import CarFactory



class TestCar(TestCase):
    def test_calliope(self):
        # Arrange
        create_car = CarFactory()
        
        current_date = '2023-7-29'
        last_service = '2020-01-01'
        curr_mileage = 50000
        last_mileage = 20000
        data = [1,1,1,1]

        calliope = create_car.create_calliope(
            current_date=current_date,
            last_service_date=last_service,
            current_mileage=curr_mileage,
            last_service_mileage=last_mileage,
            sensor_data=data
            )

        # Act
        result = calliope.needs_service()

        # Assert
        self.assertEqual(result, True)

    def test_glissade(self):
        # Arrange
        create_car = CarFactory()
        
        current_date = '2023-7-29'
        last_service = '2020-01-01'
        curr_mileage = 50000
        last_mileage = 20000
        data = [1,1,1,1]

        glissade = create_car.create_glissade(
            current_date=current_date,
            last_service_date=last_service,
            current_mileage=curr_mileage,
            last_service_mileage=last_mileage,
            sensor_data=data
        )

        # Act
        result = glissade.needs_service()

        # Assert
        self.assertTrue(result)

    def test_plaindrome(self):
        # Arrange
        create_car = CarFactory()
        
        current_date = '2023-7-29'
        last_service = '2020-01-01'
        warning = True
        data = [1,1,1,1]

        plaindrome = create_car.create_plaindrome(
            current_date=current_date,
            last_service_date=last_service,
            warning_light_on=warning,
            sensor_data=data
        )

        # Action
        result = plaindrome.needs_service()


        # Assert
        self.assertTrue(result)

    def test_rorschach(self):
        # Arrange 
        create_car = CarFactory()
        
        current_date = '2023-7-29'
        last_service = '2020-01-01'
        curr_mileage = 50000
        last_mileage = 20000
        data = [1,1,1,1]

        rorschach = create_car.create_rorschach(
            current_date=current_date,
            last_service_date=last_service,
            current_mileage=curr_mileage,
            last_service_mileage=last_mileage,
            sensor_data=data
        )

        # Act
        result = rorschach.needs_service()

        # Assert
        self.assertTrue(result)

    def test_thoves(self):
        # Arrange
        create_car = CarFactory()
        
        current_date = '2023-7-29'
        last_service = '2020-01-01'
        curr_mileage = 50000
        last_mileage = 20000
        data = [1,1,1,1]

        thovex = create_car.create_thovex(
            current_date=current_date,
            last_service_date=last_service,
            current_mileage=curr_mileage,
            last_service_mileage=last_mileage,
            sensor_data=data
        )

        # Act
        result = thovex.needs_service()

        # Assert
        self.assertTrue(result)