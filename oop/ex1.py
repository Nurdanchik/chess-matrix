 
from random import shuffle
from ex2 import Player

davlet = Player('Davlet', 'yellow', 15, 20, 5, 10)
akbar = Player('Akbar', 'red', 10, 25, 10, 5)
myrza = Player('Myrza', 'green', 40, 0, 10, 0)
Zhumabek = Player('Zhumabek', 'green', 7, 30, 3, 10)
Kutmansher = Player('Kutmansher', 'green', 10, 10, 15, 15)
Timur = Player('Timur', 'green', 20, 10, 10, 10)
Temirlan = Player('Temirlan', 'green', 14, 20, 12, 4)
Zalkarbek = Player('Zalkarbek', 'green', 10, 20, 10, 10)
Abu = Player('Abu', 'green', 25, 10, 8, 7)
Tilekmat = Player('Tilekmat', 'green', 15, 10, 15, 10)
Tariel = Player('Tariel', 'green', 10, 40, 0, 0)
Erlan = Player('Erlan', 'green', 20, 15, 5, 10)
Ayana = Player('Ayana', 'green', 15, 15, 10, 10)
Rayana = Player('Rayana', 'green', 25, 15, 0, 10)
Aliya = Player('Aliya', 'green', 13, 7, 15, 15)
Karim = Player('Karim', 'green', 20, 10, 0, 20)
Beknazar = Player('Beknazar', 'green', 20, 20, 5, 5)
Barsbek = Player('Barsbek', 'green', 40, 10, 0, 0)
Artur = Player('Artur', 'green', 25, 0, 25, 0)

players = [davlet, akbar, myrza, Zhumabek, Kutmansher, Timur, Temirlan, Zalkarbek, Abu, Tilekmat, Tariel, Erlan, Ayana, Rayana, Karim, Aliya, Beknazar, Artur, Barsbek]
shuffle(players)

while (len(players) > 1):
    i = 0
    while (i < len(players)):
        if (i == len(players) - 1):
            attack = players[i].perf()
            players[0].takeDamage(attack)
            if (players[0].getHealth() <= 0):
                players.pop(0)
        else:
            attack = players[i].perf()
            players[i + 1].takeDamage(attack)
            if (players[i + 1].getHealth() <= 0):
                players.pop(i + 1)
        i += 1

    shuffle(players)