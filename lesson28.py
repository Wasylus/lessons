# Inheritance example
# TODO show how polymorphism works


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def make_sound(self):
        print("woof woof")
        # self.sound = "woof"
        # return "woof woof"


    # def __init__(self, name, age):
    #     super().__init__(name, age)

class Cat(Animal):
    pass
    # def __init__(self, name: str, age: str):
    #     super().__init__(name, age)

cat_one: Animal = Cat(age=14, name="zdzisiek")
dog_one: Animal = Dog("rysiek", 14)
print(dog_one.age == cat_one.age)
dog_one.make_sound()
