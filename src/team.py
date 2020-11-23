class Team:
    def __init__(self, name, players, coach):
        self.name = name 
        self.players = players
        self.coach = coach
    
    def add_player(self, name):
        self.players.append(name)
