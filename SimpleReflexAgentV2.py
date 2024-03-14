import random

# Define the percepts and actions
PERCEPTS = ["dirty", "clean"]
ACTIONS = ["clean", "move_right", "move_left"]
ROOMS = ["A", "B"]

# Define the reflex rules
REFLEX_RULES = {
    ("dirty", "A"): "clean",
    ("clean", "A"): "move_right",
    ("dirty", "B"): "clean",
    ("clean", "B"): "move_left",
}


# Reflex Agent function
def reflex_agent(percept, room):
    """
    Takes a percept and room as input and returns the corresponding action based on the REFLEX_RULES.
    """
    state = (percept, room)
    action = REFLEX_RULES.get(state, "move_right")  # Default action is to move right
    return action


# Environment function
def environment(action, room):
    """
    Simulates the environment's response to the agent's action.
    Updates the room and returns a new percept based on the action.
    """
    if action == "move_right":
        new_room = ROOMS[(ROOMS.index(room) + 1) % len(ROOMS)]
    elif action == "move_left":
        new_room = ROOMS[(ROOMS.index(room) - 1) % len(ROOMS)]
    else:
        new_room = room

    if new_room == "A":
        new_percept = "dirty"
    else:
        new_percept = random.choice(PERCEPTS)

    return new_percept, new_room


# Main loop
def main():
    """
    The main function that runs the agent-environment loop.
    """
    print("Welcome to the Vacuum Cleaner World with Two Rooms!")
    print("The agent will perceive the environment and take actions accordingly.")

    # Randomly select an initial room and percept
    room = random.choice(ROOMS)
    percept = random.choice(PERCEPTS)
    print(f"Initial room: {room}, Initial percept: {percept}")

    while True:
        # Call the reflex agent function to get the action based on the current percept and room
        action = reflex_agent(percept, room)
        print(f"Action: {action}")

        # Simulate the environment's response to the action
        percept, room = environment(action, room)
        print(f"New room: {room}, New percept: {percept}")

        # Ask the user if they want to continue
        if input("Continue? (y/n) ") != "y":
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()
