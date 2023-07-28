from Car import Car 
from datetime import datetime
from Engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from Battery import SpindlerBattery, NubbinBattery

class CarFactory:
    def date_str_convert(self, date):
        converted_date = datetime.strptime(date, '%Y-%m-%d').date()
        return converted_date


    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        curr_date = self.date_str_convert(current_date)
        last_date = self.date_str_convert(last_service_date)

        calliope_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        calliope_battery = SpindlerBattery(last_service_date=last_date,current_date=curr_date)

        calliope = Car(engine=calliope_engine, battery=calliope_battery)

        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        curr_date = self.date_str_convert(current_date)
        last_date = self.date_str_convert(last_service_date)

        glissade_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        glissade_battery = SpindlerBattery(last_service_date=last_date,current_date=curr_date)

        glissade = Car(engine=glissade_engine, battery=glissade_battery)

        return glissade
    
    def create_plaindrome(self, current_date, last_service_date, warning_light_on):
        curr_date = self.date_str_convert(current_date)
        last_date = self.date_str_convert(last_service_date)

        plaindrome_engine = SternmanEngine(warning_light_on=warning_light_on)
        plaindrome_battery = SpindlerBattery(last_service_date=last_date,current_date=curr_date)

        plaindrome = Car(engine=plaindrome_engine, battery=plaindrome_battery)

        return plaindrome
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        curr_date = self.date_str_convert(current_date)
        last_date = self.date_str_convert(last_service_date)

        rorschach_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        rorschach_battery = NubbinBattery(last_service_date=last_date, current_date=curr_date)

        rorschach = Car(engine=rorschach_engine, battery=rorschach_battery)

        return rorschach
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        curr_date = self.date_str_convert(current_date)
        last_date = self.date_str_convert(last_service_date)

        thovex_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        thovex_battery = NubbinBattery(last_service_date=last_date, current_date=curr_date)

        thovex = Car(engine=thovex_engine, battery=thovex_battery)

        return thovex