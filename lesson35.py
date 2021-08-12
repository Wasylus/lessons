class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(
            self.name, self.health, self.damage_per_attack
        )


# fight_result = declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")
# test.assert_equals(fight_result, "Lew")


def declare_winner(fa: Fighter, fb: Fighter, first_attacker: str):
    # Identify Fighter objects which attacks first
    if first_attacker == fa.name:
        current_attacker = fa
        attack_receiver = fb
    else:
        current_attacker = fb
        attack_receiver = fa

    # current_attacker.health = 40
    if current_attacker.health <= 0:
        return attack_receiver.name
    if attack_receiver.health <= 0:
        return current_attacker.name

    while True:
        # Everything inside this loop is just one round (2 punches)
        # print(f"BEFORE | {attack_receiver.name}'s HP: {attack_receiver.health}")
        attack_receiver.health -= current_attacker.damage_per_attack
        # print(f"AFTER | {attack_receiver.name}'s HP: {attack_receiver.health}")

        if attack_receiver.health <= 0:
            # Harry is dead
            return current_attacker.name
        else:
            # Now they change roles (swap places)
            current_attacker, attack_receiver = attack_receiver, current_attacker
            # print(
            #     ">>>> SWAPPING ROLES\n"
            #     f">>>> {current_attacker.name} is attacking now,\n"
            #     f">>>> {attack_receiver.name} will receive a punch in the face\n"
            # )

            # Harry is still alive, so he can punch Lew
            # print(f"BEFORE | {attack_receiver.name}'s HP: {attack_receiver.health}")
            attack_receiver.health -= current_attacker.damage_per_attack
            # print(f"AFTER | {attack_receiver.name}'s HP: {attack_receiver.health}")

            if attack_receiver.health <= 0:
                return current_attacker.name
        # print("-----------------------")


# -----------------------0+++++++++++++++++++++++++++
# Example 1:
# Let's assume that foo has 5 HP
# is_alive(foo) == not is_dead(foo)
# True == not False 
# True == True 
# True

# Example 2:
# LEt's assume that foo has -5 HP
# is_alive(foo) == not is_dead(foo)
# False == (not True)
# False == False 
# True

# Conculusion:
# is_alive(foo) is exactly the same as writing: not is_dead(foo)

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(
            self.name, self.health, self.damage_per_attack
        )

    def is_alive(self) -> bool:
        return self.health > 0

    # NOTE: this method is redundant, but at least it does not create the opportunity for introducing bugs
    # def is_dead(self) -> bool:
    #     return not self.is_alive()

    def punch(self, receiver: Fighter) -> None:
        receiver.health -= self.damage_per_attack

def declare_winner(fa: Fighter, fb: Fighter, first_attacker: str):
    # Identify Fighter objects which attacks first
    if first_attacker == fa.name:
        current_attacker = fa
        attack_receiver = fb
    else:
        current_attacker = fb
        attack_receiver = fa

    # attack_receiver = Harry, 2
    # current_attacker = Lew, 5
    while attack_receiver.is_alive() and current_attacker.is_alive():
        current_attacker.punch(attack_receiver)

        # attack_receiver = Harry, -400
        # current_attacker = Lew, 5
        current_attacker, attack_receiver = attack_receiver, current_attacker

        # Note what can happen after fighters swap
        # attack_receiver = Lew, 5
        # current_attacker = Harry, -400
    return attack_receiver.name
    
fighter_a = Fighter("Harry", 10, 2)
fighter_b = Fighter("Lew", 5, 4)

# 1. Just analyze the code as it is"""
# Our test
# winner = declare_winner(fighter_a, fighter_b, first_attacker="Harry")
# print("And the winner is... ", winner)
# assert winner == "Harry", "Harry is supposed to win"

# Offtopic on how assertion behaves
# if winner == "Harry":
#     pass
# else:
#     raise AssertionError("Harry is supposed to win")

# Codewars tests
assert declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") == "Lew"
assert declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry") == "Harry"
assert (
    declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry")
    == "Harald"
)
assert (
    declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald")
    == "Harald"
)
assert (
    declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry")
    == "Harald"
)
assert (
    declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald")
    == "Harald"
)


# 2. Advanced homework - change the code so that Harry wins
# winner = declare_winner(fighter_a, fighter_b , first_attacker="Harry")
# print("And the winner is... ", winner)
# assert winner == "Harry", "If Harry attacks first, he should win this fight"


