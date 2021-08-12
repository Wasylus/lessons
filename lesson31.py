from icecream import ic
from datetime import datetime

def square(num):
    return num * num

def current_time():
    return str(datetime.now())

print(square(num=2))
ic.configureOutput(prefix=current_time)
ic(square(2))



# result = square(2) 
# message = str(datetime.now()) + str(result)
# print(message)

class Car:
    num_wheels = 123
    def __init__(self, name):
        self.name = name
        self.some_random_field = "asdas baqsdbasda"
    
    # def __repr__(self):
    #     return f"Our {self.name} has {self.num_wheels}"

# repr(Car("Martin"))
ic()
name = "Martinr"
print(vars(Car("Volvo")))
ic()









