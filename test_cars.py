from CarFactory import CarFactory

create_car = CarFactory()

calliope = create_car.create_calliope(last_service_date='2020-01-01', current_date='2023-07-28', current_mileage=80000, last_service_mileage=70000)
print(calliope.needs_service())

glissade = create_car.create_glissade(last_service_date='2023-01-01', current_date='2023-07-28', current_mileage=80000, last_service_mileage=70000)
print(glissade.needs_service())

palindrome = create_car.create_plaindrome(warning_light_on=True, last_service_date='2023-01-01', current_date='2023-07-28')
print(palindrome.needs_service())

rorschach = create_car.create_rorschach(last_service_date='2020-01-01', current_date='2023-07-28', current_mileage=80000, last_service_mileage=70000)
print(rorschach.needs_service())

thovex = create_car.create_thovex(last_service_date='2020-01-01', current_date='2023-07-28', current_mileage=80000, last_service_mileage=70000)
print(thovex.needs_service())