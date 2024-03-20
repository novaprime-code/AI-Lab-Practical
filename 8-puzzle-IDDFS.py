from collections import deque
# ready for practical report
# Define the goal state
GOAL_STATE = (0, 1, 2, 3, 4, 5, 6, 7, 8)

# Define the possible moves
MOVES = {
    0: (1, 3),
    1: (0, 2, 4),
    2: (1, 5),
    3: (0, 4, 6),
    4: (1, 3, 5, 7),
    5: (2, 4, 8),
    6: (3, 7),
    7: (4, 6, 8),
    8: (5, 7),
}


def swap(state, i, j):
    """
    Swap the values at indices i and j in the given state.
    """
    new_state = list(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return tuple(new_state)


def generate_next_states(state):
    """
    Generate the next possible states from the given state.
    """
    next_states = []
    blank_index = state.index(0)
    for move in MOVES[blank_index]:
        next_state = swap(state, blank_index, move)
        next_states.append(next_state)
    return next_states


def iddfs_solver(initial_state):
    """
    Solve the 8-puzzle problem using Iterative Deepening Depth-First Search (IDDFS).
    """
    depth = 0
    while True:
        solution_path = dfs_limited(initial_state, depth)
        if solution_path is not None:
            return solution_path
        depth += 1


def dfs_limited(state, depth, path=None):
    """
    Perform Depth-First Search (DFS) with a limited depth.
    """
    if path is None:
        path = []

    if state == GOAL_STATE:
        return path

    if depth == 0:
        return None

    for next_state in generate_next_states(state):
        if next_state not in path:
            next_path = path + [next_state]
            solution_path = dfs_limited(next_state, depth - 1, next_path)
            if solution_path is not None:
                return solution_path

    return None


def display_puzzle(state):
    """
    Display the puzzle grid for the given state.
    """
    grid = [
        [state[0], state[1], state[2]],
        [state[3], state[4], state[5]],
        [state[6], state[7], state[8]],
    ]

    for row in grid:
        print(" ".join([str(val) if val != 0 else "_" for val in row]))
    print()


# Example usage
initial_state = (7, 2, 4, 5, 0, 6, 8, 3, 1)
solution_path = iddfs_solver(initial_state)

if solution_path:
    print("Solution found!")
    for i, state in enumerate(solution_path):
        print(f"Step {i}:")
        display_puzzle(state)
else:
    print("No solution found!")
