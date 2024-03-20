from collections import deque

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


def bfs_solver(initial_state):
    """
    Solve the 8-puzzle problem using Breadth-First Search (BFS).
    """
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == GOAL_STATE:
            return path

        if current_state not in visited:
            visited.add(current_state)

            for next_state in generate_next_states(current_state):
                next_path = path + [next_state]
                queue.append((next_state, next_path))

    return []  # No solution found


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
solution_path = bfs_solver(initial_state)

if solution_path:
    print("Solution found!")
    for i, state in enumerate(solution_path):
        print(f"Step {i}:")
        display_puzzle(state)
else:
    print("No solution found!")
