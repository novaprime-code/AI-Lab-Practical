# Define the possible states
STATES = ["s1", "s2", "s3", "s4"]
# This list represents the possible states in the environment.

# Define the utility values for each state
UTILITIES = {"s1": 0.2, "s2": 0.8, "s3": 0.4, "s4": 0.6}
# This dictionary defines the utility values associated with each state.
# The utility value represents the desirability or "reward" of being in that state.

# Define the possible actions
ACTIONS = ["a1", "a2", "a3", "a4"]
# This list represents the possible actions the agent can take.

# Define the transition model
TRANSITION_MODEL = {
    "s1": {
        "a1": [
            "s2",
            "s3",
        ],  # If the current state is 's1' and action 'a1' is taken, the possible next states are 's2' and 's3'.
        "a2": ["s2", "s4"],
        "a3": ["s1", "s3"],
        "a4": ["s1", "s4"],
    },
    "s2": {
        "a1": ["s1", "s3"],
        "a2": ["s2", "s4"],
        "a3": ["s1", "s3"],
        "a4": ["s2", "s4"],
    },
    "s3": {
        "a1": ["s1", "s3"],
        "a2": ["s2", "s4"],
        "a3": ["s3", "s4"],
        "a4": ["s3", "s4"],
    },
    "s4": {
        "a1": ["s1", "s3"],
        "a2": ["s2", "s4"],
        "a3": ["s3", "s4"],
        "a4": ["s3", "s4"],
    },
}
# This dictionary defines the transition model, which specifies the possible next states for each state-action pair.
# For example, if the current state is 's1' and action 'a1' is taken, the possible next states are 's2' and 's3'.


# Utility-based agent function
def utility_agent(current_state):
    """
    Utility-based agent that chooses the action that maximizes the expected utility.
    """
    max_utility = -float("inf")  # Initialize max_utility to negative infinity
    best_action = None  # Initialize best_action to None

    for action in ACTIONS:
        possible_next_states = TRANSITION_MODEL[current_state][action]
        # Get the possible next states for the current state and action from the transition model

        expected_utility = sum(
            UTILITIES[next_state] for next_state in possible_next_states
        ) / len(possible_next_states)
        # Calculate the expected utility by taking the average of the utility values of the possible next states

        if expected_utility > max_utility:
            max_utility = expected_utility
            best_action = action
            # If the expected utility is greater than the current max_utility, update max_utility and best_action

    return best_action
    # Return the action that maximizes the expected utility


# Example usage
current_state = "s1"
print(f"Current state: {current_state}")
action = utility_agent(current_state)
print(f"Action chosen: {action}")
