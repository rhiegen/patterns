import random
import string

class VehicleRegistry:

    def generate_id(length):
        return ''.join(random.choices(string.ascii_uppercase,k=length))

    def generate_vehicle_license(id):
        return f"{id[:2]}-{''.join(random.choices(string.digits,k=2))}-{''.join(random.choices(string.ascii_uppercase,k=2))}"

class application:
    def register_vehicle(self, brand : str):
        registry = VehicleRegistry()
        vehicle_id = registry.generate_id(12)
        license_plate = registry.generate_vehicle_license(vehicle_id)
sss
