from random import randrange
players =[]

class player:
    def __init__(self, x):
        self.score = 0
        self.name = x

    def add_points(self, x):
        self.score += x


def add_player(name):
    new = player(name)
    players.append(new)
    return players

def random(x):
    return randrange(x)