class FootballPlayer:
    def __init__(self, name, position, goals_scored=0):
        self.name = name 
        self.position = position 
        self.goals_scored = goals_scored 

    def display_info(self):
        pass
    
    def score_goal(self):
        pass


class Forward(FootballPlayer):
    def __init__(self, name, position, goals_scored=0, assists=0):
        super().__init__(name, position, goals_scored)
        self.assists = assists

    def display_info(self):
        return f'''
Player: {self.name}.
Position: {self.position}
Goals scored: {self.goals_scored}
Assists: {self.assists}
'''

class Goalkeeper(FootballPlayer):
    def __init__(self, name, position, goals_scored=0, saves=0):
        super().__init__(name, position, goals_scored)
        self.saves = saves

    def display_info(self):
        return f'''
Player: {self.name}.
Position: {self.position}
Saves: {self.saves}
'''

class Midfielder(FootballPlayer):
    def __init__(self, name, position, goals_scored=0, passes=0):
        super().__init__(name, position, goals_scored)
        self.passes = passes

    def display_info(self):
        return f'''
Player: {self.name}.
Position: {self.position}
Passes: {self.passes}
'''
    

middle = Midfielder('Iniesto', 'middlefielder', 0, 1000)
print(middle.display_info())
forward = Forward('Ronaldo Lima', 'forward', 100, 100)
print(forward.display_info())
goalkeeper = Goalkeeper('Yashin', 'goalie', 0, 100)
print(goalkeeper.display_info())