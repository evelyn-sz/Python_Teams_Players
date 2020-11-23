class Team:
    def __init__(self, name, players, coach):
        self.name = name 
        self.players = players
        self.coach = coach
    
    def add_player(self, name):
        self.players.append(name)
    
    def has_player(self, name):
        for player in self.players:
            if player == name:
                return True
        else: 
            return False

    # same as above but in short line:
    # return name in self.players

