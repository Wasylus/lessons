

# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.
class Person:
    def __init__(self, my_name):
        self.name = my_name
        
    def greet(self, your_name: str) -> str:
        msg = f"Hello {your_name}, my name is {self.name}"
        print(msg)
        return msg
    
    def greet_long_names(self,name: str):
        if len(name) >= 4:
            return f"You have a long name: {name}"
        return f"Hello, you have a short name {name}"
        # Exact same behavior can be achieved by:
        # else:
        #     return f"Hello, you have a short name {name}"


person_one = Person("Jill")
person_two = Person("Jack")

assert person_two.greet("Jill") == "Hello Jill, my name is Jack"
assert person_two.greet("Mary") ==  "Hello Mary, my name is Jack"
assert person_one.greet("Jack") == "Hello Jack, my name is Jill"
assert person_one.name == "Jill", "Person's name could not be retrieved"

# This is how "assert" keyword works under the hood
# if not (jill.name == "Jill"):
#     raise AssertionError("Person's name could not be retrieved")

