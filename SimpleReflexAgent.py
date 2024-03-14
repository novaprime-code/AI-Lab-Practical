import random


class Environment:
    def __init__(self):
        # Randomly initialize the status of rooms A and B
        self.room_a_status = random.choice(["Dirty", "Clean"])
        self.room_b_status = random.choice(["Dirty", "Clean"])
        # Randomly choose the agent's starting location
        self.agent_location = random.choice(["A", "B"])

    def percept(self):
        # Return the percept of the agent's current location and content
        return [
            self.agent_location,
            self.room_a_status if self.agent_location == "A" else self.room_b_status,
        ]

    def clean_room(self):
        # Clean the current room
        if self.agent_location == "A":
            self.room_a_status = "Clean"
        else:
            self.room_b_status = "Clean"

    def move_right(self):
        # Move the agent to the right room (from A to B)
        print("Moving from room A to room B.")
        self.agent_location = "B"

    def move_left(self):
        # Move the agent to the left room (from B to A)
        print("Moving from room B to room A.")
        self.agent_location = "A"


class ReflexAgent:
    def __init__(self, environment):
        self.environment = environment

    def act(self):
        # Check the percept and decide the action
        percept = self.environment.percept()
        location, status = percept

        if status == "Dirty":
            self.environment.clean_room()
        elif location == "A":
            self.environment.move_right()
        else:
            self.environment.move_left()


def main():
    # Create the environment
    env = Environment()

    # Create the reflex agent
    agent = ReflexAgent(env)

    # Run the simulation until both rooms are clean
    while env.room_a_status == "Dirty" or env.room_b_status == "Dirty":
        print("Agent Location:", env.agent_location)
        print("Room A Status:", env.room_a_status)
        print("Room B Status:", env.room_b_status)

        # Let the agent act based on the current environment
        agent.act()

        print()

    print("Both rooms are clean.")


if __name__ == "__main__":
    main()
