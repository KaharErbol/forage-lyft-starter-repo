from Car import Car 
from Engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from Battery import SpindlerBattery, NubbinBattery

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        calliope_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        calliope_battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)

        calliope = Car(engine=calliope_engine, battery=calliope_battery)

        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        glissade_engine = WilloughbyEngine(self, last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        glissade_battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)

        glissade = Car(engine=glissade_engine, battery=glissade_battery)

        return glissade
    
    def create_plaindrome(self, current_date, last_service_date, warning_light_on):
        plaindrome_engine = SternmanEngine(warning_light_on=warning_light_on)
        plaindrome_battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)

        plaindrome = Car(engine=plaindrome_engine, battery=plaindrome_battery)

        return plaindrome
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        rorschach_battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        rorschach = Car(engine=rorschach_engine, battery=rorschach_battery)

        return round
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        thovex_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        thovex_battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)

        thovex = Car(engine=thovex_engine, battery=thovex_battery)

        return thovex