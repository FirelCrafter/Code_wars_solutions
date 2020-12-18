class Fighter:

    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter ({}, {}, {})".format(self.name, self.health, self.damage_per_attack)


def fight(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        while True:
            fighter2.health -= fighter1.damage_per_attack
            if fighter1.health <= 0 or fighter2.health <= 0:
                break
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0 or fighter2.health <= 0:
                break
    if fighter2.name == first_attacker:
        while True:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0 or fighter2.health <= 0:
                break
            fighter2.health -= fighter1.damage_per_attack
            if fighter1.health <= 0 or fighter2.health <= 0:
                break

    return fighter1.health, fighter2.health


def declare_winner(fighter1, fighter2, first_attacker):
    fight(fighter1=fighter1, fighter2=fighter2, first_attacker=first_attacker)
    if fighter1.health < fighter2.health:
        return fighter2.name
    if fighter2.health < fighter1.health:
        return fighter1.name
