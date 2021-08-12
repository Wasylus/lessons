class Meta:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.whatever = kwargs

    def __str__(self):
        self.name 

# coordinate = (14, 15)

# test_obj = Meta("hello", 12, [], {}, some_name="Michał", some_other_name="Marcin")
# print(type(test_obj.args))
# print(test_obj.whatever)

# class DatasetFile:
#     def __init__(self):
#         self.permissions = ''
#         self.amount_of_records = ''
#         self.disk_path = ''
    
#     def count_labels():
#         for 

#     def find_unique_records():
#         pass

#     def copy_to_machine(ip_address):
#         pass
class Car:   
    def __init__(self, name, mileage, car_type="Sedan"):
        self.name = name 
        self.mileage = mileage 
        self.car_type = car_type
        self.color = "black"

    def description(self):                 
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

    def max_speed(self, speed):
        # self.name = "Fastest car in the world"
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"

    def __str__(self):
        return f"Car name is {self.name}, mileage equals {self.mileage}, car_type is {self.car_type}"
    
    def paint(self,new_color):
        self.color = new_color

obj2 = Car("Honda City", 24.1, car_type="Family")
obj1 = Car("Tesla", 224.1, car_type="Sedan")
obj3 = Car("Toyota Auris", 224.1)

print(obj3.color)
obj3.paint("red")
print(obj3.color)
# print(obj3)
# print(obj3)
# print(obj3)
# print(obj3.description())

# print(obj1.car_type, obj2.car_type)
# print(obj2.name, obj2.mileage)
# print(obj2.description())
# print(obj2.max_speed(150))