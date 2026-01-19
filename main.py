from enviroment import Environment
from agent import Agent

def main():
    env = Environment()
    agent = Agent()

    print("Termostato Inteligente\n")

    for i in range(1, 11):
        print(f"Iteración {i}")

        current_temp = env.get_percept()
        print(f"Temperatura actual: {current_temp}°C")

        action = agent.act(current_temp)
        print(f"Acción del agente: {action}")

        env.update(action)
        new_temp = env.get_percept()
        print(f"Nueva temperatura: {new_temp}°C\n")


if __name__ == "__main__":
    main()