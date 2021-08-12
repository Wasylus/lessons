# https://www.codewars.com/kata/54fe05c4762e2e3047000add

class Ship:
    CREW_MEMBER_WEIGHT = 1.5
    MIN_WEIGHT_OF_SHIP_WORTH_LOOTING = 20

    def __init__(self, total_weight: int, num_crew_members: int):
        self.total_weight = total_weight
        self.num_crew_members = num_crew_members

        self.crew_weight = self.num_crew_members * self.CREW_MEMBER_WEIGHT
        self.ship_weight = total_weight - self.crew_weight
        self.validate_ship()

    def validate_ship(self):
        if self.ship_weight <= 0:
            raise ValueError("Ship weight cannot be negative")
        elif self.ship_weight < self.crew_weight:
            raise ValueError("It shouldnt be like that, how is it even possible")

    def is_worth_it(self):
        crew_member_weight = 1.5
        total_crew_weight = self.crew * crew_member_weight
        ship_weight = self.draft - total_crew_weight

        # We could simplify to oneliner
        if ship_weight > 20:
            return True
        else:
            return False

    def is_worth_it(self):
        return self.ship_weight > self.MIN_WEIGHT_OF_SHIP_WORTH_LOOTING
    
    def __str__(self):
        return f"Total weight: {self.total_weight},\n" \
            f"crew weight: {self.crew_weight},\n" \
            f"ship weight: {self.ship_weight},\n" \
            f"number of crew members: {self.num_crew_members}"
    
    __repr__ = __str__

titanic = Ship(40, 15)
print(repr(titanic))



