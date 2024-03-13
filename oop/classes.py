import random
# class Animal:
#     def __init__(self, sex, place):
#         self.sex = sex 
#         self.place = place 


#     def getPlace(self):
#         return 'Место обитания' + self.place
    

# animal1 = Animal('M','Male','College')

# class Insects(Animal):
#     def __init__(self, color, sex, place):
#         super().__init__(sex, place)
#         self.color = color 

# class Mammals(Animal):
#     def __init__(self, size, sex, place):
#         super().__init__(sex, place)
#         self.size = size


# tiger = Mammals('M','Male','College')
# print(tiger.getPlace())


        # self.__sex = sex 
        # self.__name = name

#     def greeting(self):
#         print('Hello everyone, I am an Animal class '+ self.name)

# erlan = Animal('male', 'Erlan')
# davlet = Animal('female', 'Davlet')

# erlan.sex = 'jnfoef'

# print(erlan.sex)

# erlan.greeting()

# class Car:
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand 
#         self.model = model
#         self.year = year
#         self.mileage = mileage

#     def display_info(self):
#         return f"{self.brand} {self.model} ({self.year}), Mileage: {self.mileage} miles"

# class ElectricCar(Car):
#     def __init__(self, battery_capacity, brand, model, year, mileage):
#         super().__init__(brand, model, year, mileage)
#         self.battery_capacity = battery_capacity

#     def display_info(self):
#         return f"Electric Car - {self.brand} {self.model} ({self.year}), Mileage: {self.mileage} miles, Battery: {self.battery_capacity}"
    

# tesla = ElectricCar('500w','Mercedes','Banan',2020,25000)
# mers = Car('Mercedes','Banan',2020,25000)
# print(mers.display_info())
# print(tesla.display_info())



# class WashingMachine:
#     def __init__(self, powder = 1000, conditioner = 1000):
#         self.powder = powder 
#         self.conditioner = conditioner

#     def subtract_powder(self, powder):
#         self.powder -= 600
#         return self.powder
    
#     def subtract_conditioner(self, conditioner):
#         self.conditioner -= 720
#         return self.conditioner
    
#     def wash_clothes(self):
#         minimumpowder = 600
#         minimumconditioner = 720
#         currentpowder = self.powder
#         currentconditioner = self.conditioner
#         if currentpowder >= minimumpowder:
#             self.subtract_powder()
#             print('You have got enough powder to wash it.')
#         elif currentpowder < minimumpowder:
#             less = minimumpowder - currentpowder
#             print(f'You have {less} powder less than must!')
#         if currentconditioner >= minimumconditioner:
#             self.subtract_conditioner()
#             print('You have got enough conditioner to wash it.')
#         elif currentconditioner < minimumconditioner:
#             less = minimumconditioner - currentconditioner
#             print(f'You have {less} conditioner less than must!')

# suit = WashingMachine(100, 200)
# print(suit.wash_clothes())




# class Player:
#     def __init__(self, name, health, armour, attack_damage):
#         self.name = name 
#         self.health = health 
#         self.armour = armour
#         self.attack_damage = attack_damage

#     def get_attacked(self):
#         damage = ( self.health - random.randint(0, self.attack_damage) ) + random.randint(0, self.armour)
#         return damage 
    
# players = [Player('Nurdan',100, 100, 100,),
#            Player('Zalkar',100, 100, 100,),
#            Player('Adilet',100, 100, 100,),
#            Player('Akbar',100, 100, 100,),
#            Player('Abu',100, 100, 100,),
#            Player('Zhumabek',100, 100, 100,),
#            ]

# while len(players) <= 1:
#     for i in range(len(players) - 1):
#         pair = (players[i], players[i + 1].get_attacked())
#         print(f'Игрок {players[i]} атаковал {players[i + 1]}')
#         if players[i].health == 0:
#             players[i].remove()
    
#     if len(players) == 1:
#         print(f'Игрок {players[i]} выиграл.')


# import random

# class Player:
#     def __init__(self, name, health, armour, attack_damage):
#         self.name = name 
#         self.health = health 
#         self.armour = armour
#         self.attack_damage = attack_damage

#     def get_attacked(self):
#         damage = random.randint(0, self.attack_damage) - random.randint(0, self.armour)
#         return max(0, damage)

# players = [
#     Player('Nurdan', 100, 100, 100),
#     Player('Zalkar', 100, 100, 100),
#     Player('Adilet', 100, 100, 100),
#     Player('Akbar', 100, 100, 100),
#     Player('Abu', 100, 100, 100),
#     Player('Zhumabek', 100, 100, 100),
# ]

# while len(players) > 1:
#     i = 0
#     while i < len(players) - 1:
#         damage = players[i + 1].get_attacked()
#         players[i + 1].health = max(0, players[i + 1].health - damage)
#         print(f'Игрок {players[i].name} атаковал Игрока {players[i + 1].name}. Урон: {damage}. Здоровье: {players[i + 1].health}')

#         if players[i + 1].health == 0:
#             removed_player = players.pop(i + 1)
#             print(f'Игрок {removed_player.name} выбыл из игры.')
#         else:
#             i += 1

# if len(players) == 1:
#     print(f'Игрок {players[0].name} выиграл.')

# todos = []

# class Todo:
    
#     def __init__(self):
#         pass 

#     def add_todo(objectclass):
#         todos.append(objectclass) 
#         return todos
    
#     def list_items(todos):
#         return todos 
    
#     def find(tofind):
#         for todo in todos:
#             if tofind in todos:
#                 return f'{tofind} is in this list of todos'
#             else:
#                 return f'{tofind} is not in this list of todos'

# class TodoItem:

#     def __init__(self, stroka, is_done = False):
#         self.is_done = is_done
#         self.stroka = stroka

#     def check(self):
#         checked = self.is_done = True 
#         return checked

#     def uncheck(self):
#         unchecked = self.is_done = False
#         return unchecked

# to_do = TodoItem('To help my mom to make the dinner', False)
# Todo.add_todo(to_do)
# print(Todo.list_items(todos))

class Todo:
    
    def __init__(self):
        self.todos = []

    def add_todo(self, objectclass):
        self.todos.append(objectclass) 
        return self.todos
    
    def list_items(self):
        return [todo.stroka for todo in self.todos]
    
    def find(self, tofind):
        for todo in self.todos:
            if tofind in todo.stroka:
                return f'{tofind} is in this list of todos'
        return f'{tofind} is not in this list of todos'

class TodoItem:

    def __init__(self, stroka, is_done=False):
        self.is_done = is_done
        self.stroka = stroka

    def check(self):
        self.is_done = True 

    def uncheck(self):
        self.is_done = False

# Создание экземпляров Todo и TodoItem
to_do = TodoItem('To help my mom to make the dinner', False)

# Создание экземпляра Todo и добавление в него TodoItem
to_do_list = Todo()
to_do_list.add_todo(to_do)

# Проверка метода list_items
print(to_do_list.list_items())  # Выведет: ['To help my mom to make the dinner']

# Проверка метода find
print(to_do_list.find('help'))  # Выведет: 'help is in this list of todos'
print(to_do_list.find('study'))  # Выведет: 'study is not in this list of todos'
