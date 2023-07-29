from abc import ABC, abstractmethod

"""
Carrigan tires should be serviced only when one or 
more of the values in the tire wear array is 
greater than or equal to 0.9.

Octoprime tires should be serviced only when the 
sum of all values in the tire wear array is 
greater than or equal to 3.
"""

class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Carrigan(Tire):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data
    
    def needs_service(self):
        count = 0
        for data in self.sensor_data:
            if data >= 0.9:
                count += 1
        
        return count >= 1
    
class Octoprime(Tire):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def needs_service(self):
        return sum(self.sensor_data) >= 3
