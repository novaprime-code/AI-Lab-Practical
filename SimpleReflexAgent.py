import random  # Import random module for generating random statuses


# Define a function to represent the environment and its current state
def environment(percept):
    # Print the current percept or sensory input
    print("Percept received:", percept)

    # Check the percept to decide the action
    if percept == "Dirty":
        return "Clean"
    elif percept == "Clean":
        return "Move"
    else:
        return "No Operation"


# Define a function to represent the agent's behavior
def reflex_agent(location, status):
    # Print the current location and status of the agent
    print("Location:", location, ", Status:", status)

    # Call the environment function with the current percept
    action = environment(status)

    # Print the action chosen by the agent
    print("Action:", action)
    print()  # Add a newline for better readability


# Main function to run the simulation
def main():
    # Define the initial state of the rooms
    room_a_status = random.choice(["Dirty", "Clean"])
    room_b_status = random.choice(["Dirty", "Clean"])

    # Run the reflex agent for a few iterations
    for i in range(3):
        # Call the reflex agent function for room A
        reflex_agent("Room A", room_a_status)

        # Call the reflex agent function for room B
        reflex_agent("Room B", room_b_status)

        # Randomly update the status of rooms A and B for the next iteration
        room_a_status = random.choice(["Dirty", "Clean"])
        room_b_status = random.choice(["Dirty", "Clean"])


# Run the main function to start the simulation
if __name__ == "__main__":
    main()
