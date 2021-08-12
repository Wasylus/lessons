
# my_dog_age = 10
# my_dog_tail_length = 10

# another_dog_name = "asdasd"
# another_dog_age = 10
# another_dog_tail_length = 10


# def dashjgdfhghld():
#     # pass
#     # another_dog_age += 1
#     my_dog_age = "asd"
# print(dashjgdfhghld.__code__)

def add_two_numbers(a: int, b: int = 0):
    return a + b

add_two_numbers(1, 3) # 4
add_two_numbers(1) # 1
add_two_numbers(1, b=5) # 6
add_two_numbers(b=1, a=5) # 6



# class JavaDog {
#     JavaDog(String name, int age) {
#         this.name = name;
#         this.age = age;
#     }
# }

# JavaDog myDog = new JavaDog("zdzisiek", 12)


class Dog:
    def __init__(self, name: str = "reksio", age: int = 0):
        self.name = name 
        self.age = age
        self.distance_from_house = 0
        self.bladder = 100
    
    def bark():
        print("woof woof")

    def go_for_a_walk(self):
        # implementation detail, owner does not care, but dog does
        self.distance_from_house = 10
        self.bladder_fullness = 0

    def return_back_home(self):
        self.distance_from_house = 0
        
    
my_dog = Dog("zdzisiek", 12) # name="zdzisiek, age=12
my_dog.go_for_a_walk() 
print(my_dog.distance_from_house) # 10
print(my_dog.bladder_fullness) # 0

another_dog = Dog()
another_dog.distance_from_house = 12
print(another_dog.distance_from_house) # 12

# ordered arguments vs keyword arguments
my_dog = Dog(age=12, name="zdzisiek") # name="zdzisiek, age=12
my_dog = Dog(12, "zdzisiek") # name=12, age="zdzisiek"
print(my_dog.name, my_dog.age)
# other_dog = Dog("rysiek")
# other_dog = Dog(age=12)
# another_dog = Dog()
# print(another_dog.name)

# print(my_dog.age)
# my_dog.age = 14
# print(my_dog.age)
    #     self.age = 10
    #     self.color = "red" 
        # self.num_legs = name 
    
    # def __str__(self):
    #     return self.name

    # def __gt__(self, other_dog):
    #     return self.age > other_dog.age # and self.tail_length > other_dog.tail_length
    
# my_dog = Dog()
# print(my_dog)
# my_dog = Dog("piesek", 5, "red")
# your_dog = Dog("zdzisiek", 23, "black")
# her_dog = Dog("rysiek", 34, "white")
# her_dog = Dog("rysiek", 34, "ggg")
# her_dog = Dog("rysiek", 34, "vvv")

# print("is dog of mine older than yours: ", my_dog > your_dog)


# print(my_dog.name)
# print(your_dog.name)
# print(her_dog.name)
# print(my_dog.__str__())
# print(str(my_dog))
# print(my_dog)
# print(Dog.__class__.__bases__)

# class Knight:
#     def __init__(self, color):
#         self.color = color

from lesson26 import Dog