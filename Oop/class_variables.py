class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.total_car+=1
        Car.total_car+=1

my_test=Car("test1","test1")
Car("test2","test2")
Car("test3","test3")
Car("test4","test4")
print(my_test.total_car)
print(Car.total_car)
