import random

class Player:
    health = 120
    colors = ['green', 'red', 'blue', 'yellow']

    def __init__(self, name: object, color: object, damage: object, defense: object, crit: object, speed: object) -> object:
        self.name = name
        self.color = color
        self.damage = damage
        self.defense = defense
        self.crit = crit
        self.speed = speed

    def setName(self, name):
        if (type(name) == str and len(name) > 3):
            self.name = name
        else:
            print('Неверное имя')

    def setColor(self, color):
        if (color in self.colors):
            self.color = color
        else:
            print('Неверный цвет')
    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    def takeDamage(self, damage):
        totalDamage = damage - random.randint(self.defense // 4, self.defense)
        if (totalDamage <= 0):
            totalDamage = 1
        generate = random.randint(0, 100)
        if (generate <= self.speed * 2):
            totalDamage = 0
            print('Игрок уклонился')
        print('Получение урона игроком ' + self.name + ': ' + str(damage))
        self.health = self.health - totalDamage
        print('Остаток здоровья: ' + str(self.health))
        print('\n\n')

    def perf(self):
        damage = random.randint(self.damage // 2, self.damage)
        generate = random.randint(0, 100)
        if (generate <= self.crit * 3):
            damage *= 2
            print('Игрок совершил критический урон')
        print('Нанесение урона игроком ' + str(self.name) + ': ' + str(damage))
        return damage

    def getHealth(self):
        return self.health