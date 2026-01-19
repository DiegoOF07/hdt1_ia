import random

class Environment:
    def __init__(self):
        self.temperature = random.randint(0, 30)

    def get_percept(self):
        return self.temperature

    # La acción debe ser una de las 3 opciones: enfriar, calentar o esperar
    def update(self, action):
        if action == "enfriar":
            self.temperature -= 2
        elif action == "calentar":
            self.temperature += 2
        elif action == "esperar":
            pass