class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand=brand
    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model=model
my_car=Car("Tesla","Model S")
print(my_car.get_brand())
print(my_car.get_model())
my_car.set_brand("hello")
my_car.set_model("Bye")
print(my_car.get_brand())
print(my_car.get_model())