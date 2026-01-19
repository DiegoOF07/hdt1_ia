import random

class Environment:
    def __init__(self):
        self.temperature = random.randint(0, 30)

    def get_percept(self):
        return self.temperature

    def update(self, action):
        if action == "enfriar":
            self.temperature -= 2
        elif action == "calentar":
            self.temperature += 2
        elif action == "esperar":
            pass