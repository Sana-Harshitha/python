class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"Brand:{self.brand} Model:{self.model}"
    @staticmethod
    def gen_desc():
        return "Cars are means of transport"
    
my_car =Car("Toyota","Coralla")
print(my_car.full_name())
print(my_car.gen_desc())