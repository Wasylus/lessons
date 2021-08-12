class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): 
        return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

# fight_result = declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")
# test.assert_equals(fight_result, "Lew")

def declare_winner(lew: Fighter, harry: Fighter, first_attacker: str):
    """
    # | Lew's HP | Harry's HP
    0 | 10       | 5
    1 | 10       | 3
    2 | 6        | 3
    3 | 6        | 1 
    4 | 2        | 1 
    5 | 2        | -1  
    """
    # Identify Fighter objects which attacks first
    if first_attacker == lew.name:
        current_attacker = lew
    else:
        current_attacker = harry

    # Punch #1
    # Before: lew 10 | harry 5
    harry.health -= lew.damage_per_attack
    # After: lew 10 | harry 3

    # Punch #2
    # Before: lew 10 | harry 3
    lew.health -= harry.damage_per_attack
    # After: lew 6 | harry 3

    # Punch #3
    # Before: 6 | Harry 3
    harry.health -= lew.damage_per_attack
    # After: lew 6 | Harry 1

    # Punch #4
    # Before: lew 6 | Harry 1
    lew.health -= harry.damage_per_attack
    # After: lew 2 | Harry 1

    # Punch #5
    # Before: lew 2 | Harry 1
    harry.health -= lew.damage_per_attack
    # After: lew 2 | Harry -1

    # TODO Homework 
    assert lew.health == 2, "Lew should've 2 HP"
    assert harry.health == -1, "Harry should be dead already with -1 HP"

    # harry.health = 0.5
    # lew.health = 0.25
    # if lew.health <= 0 and harry.health <= 0:
    #     return "Both died"
    # if lew.health > 0 and harry.health > 0:
    #     return "Both lived"
    if harry.health <= 0:
        return "Lew"
    if lew.health <= 0:
        return "Harry"
    
    
fighter_a = Fighter("Lew", 100, 2)
fighter_b = Fighter("Harry", 50, 4)
declare_winner(fighter_a, fighter_b , "Lew")
# print(declare_winner)