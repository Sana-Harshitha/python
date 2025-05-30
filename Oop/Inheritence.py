class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"Brand:{self.brand} Model:{self.model}"
class Electrical_Car(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size



my_tesla=Electrical_Car("Tesla","Model S","85kwh")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.battery_size)