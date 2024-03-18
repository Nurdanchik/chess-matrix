import random

class Character:
    def __init__(self, name,damage, defense, critical_damage, evasion,  health=120):
        self.name = name
        self.damage = damage
        self.defense = defense
        self.critical_damage = critical_damage
        self.evasion = evasion
        self.health = health

    def take_damage(self):
        pass 

    def generate_damage(self):
        pass

class Viking(Character):
    def __init__(self, name, damage, defense, critical_damage, evasion, health=120):
        super().__init__(name, damage, defense, critical_damage, evasion, health)

    def take_damage(self, whofrom):
        damag = whofrom.damage.random.randint(0, whofrom.damage)
        (self.health - whofrom.damage) + (self.defense.random.randint(0, self.defense))
        return f'{whofrom} damaged {damag}hp from {self.name}. Player {self.name} has {self.health}hp left. '