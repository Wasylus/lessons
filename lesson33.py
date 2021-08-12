class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): 
        return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    # when someone calls repr(Fighter()), then run str() under the hood
    # so output will be identical for both methods
    __repr__ = __str__

    # How it works (implicitly) - I
    # def __repr__(self):
    #     return str(self)
    
    # How it works (implicitly) - II
    # def __repr__(self):
    #     return self.__str__()

    # Our custom __repr__ that is different than implementation of __str__
    # def __repr__(self) :
    #     return f"<Fighter name: {self.name}>"

miczi = Fighter("Michał", 1000, 10)
martin = Fighter("Martin", 1000, 10)
asia = Fighter("Asia", 1000, 10)
#     Explicit | explicit, but weird | implicit conversion to string under the hood
print(str(miczi), miczi.__str__(), miczi)

#     Explicit | explicit, but weird, noone does that
print(repr(miczi), miczi.__repr__())


# How str(some_list) might look like, or at least inferred from its behavior
# "[<Fighter name: Michał>, <Fighter name: Martin>, <Fighter name: Asia>]"
# class list:
#     def __str__(self):
#         result = "["
#         for element in self.elements:
#             elem_as_str = repr(element)
#             result += elem_as_str
#             result += ", "
#         result += "]"
#         return result

print(str([miczi, martin, asia]))