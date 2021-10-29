import random
class Coordinates:
    def __init__(self):
        pass
    def gen_random(self):
        x = random.randint(0, 60)
        y = random.randint(0, 20)
        return x, y 


