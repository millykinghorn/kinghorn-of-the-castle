class player:
    def __init__(self, x):
        self.score = 0
        self.name = x
        print(self.name)

    def add_points(self, x):
        self.score += x
