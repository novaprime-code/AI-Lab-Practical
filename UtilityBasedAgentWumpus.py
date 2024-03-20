import random


class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_location = (0, 0)
        self.gold_location = (size - 1, size - 1)
        self.wumpus_location = (1, 1)
        self.pit_locations = [(2, 2)]

    def percept(self):
        x, y = self.agent_location
        if self.gold_location == (x, y):
            return "Glitter"
        elif self.wumpus_location == (x, y):
            return "Stench"
        elif (x, y) in self.pit_locations:
            return "Breeze"
        else:
            return "Safe"


class SimpleReflexAgent:
    def __init__(self, world):
        self.world = world

    def act(self):
        percept = self.world.percept()
        if percept == "Glitter":
            print("Found gold! Taking gold...")
            # Agent takes gold and exits
            return "Exit"
        elif percept == "Stench":
            print("Wumpus ahead! Turn back...")
            # Agent turns back
            return "TurnBack"
        elif percept == "Breeze":
            print("Pit ahead! Jumping over...")
            # Agent jumps over pit
            return "Jump"
        else:
            print("Safe to move forward...")
            # Agent moves forward
            return "MoveForward"


def main():
    world = WumpusWorld()
    agent = SimpleReflexAgent(world)

    while True:
        action = agent.act()
        if action == "MoveForward":
            # Move the agent forward
            x, y = world.agent_location
            world.agent_location = (min(x + 1, world.size - 1), y)
        elif action == "TurnBack":
            # Move the agent back
            x, y = world.agent_location
            world.agent_location = (max(x - 1, 0), y)
        elif action == "Jump":
            # Jump over the pit
            print("Successfully jumped over the pit!")
        elif action == "Exit":
            print("Agent exited the Wumpus World with gold!")
            break


if __name__ == "__main__":
    main()
