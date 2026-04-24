# -------------------------------
# Initial and Goal States
# -------------------------------

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


# -------------------------------
# Possible moves (index positions)
# -------------------------------

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# -------------------------------
# BFS Solve Function
# -------------------------------

def solve(start):
    visited = []
    queue = []

    queue.append((start, []))   # (current_state, path)
    visited.append(start)

    while queue:
        current, path = queue.pop(0)

        # Check if goal reached
        if current == goal:
            return path + [current]

        zero_index = current.index(0)

        # Try all possible moves
        for move in moves[zero_index]:
            new_state = current.copy()

            # Swap 0 with neighbor
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]

            if new_state not in visited:
                visited.append(new_state)
                queue.append((new_state, path + [current]))

    return None


# -------------------------------
# Print Puzzle Function
# -------------------------------

def print_puzzle(state):
    # state is a list like [1,2,3,4,5,6,7,8,0]

    for i in range(0, 9, 3):
        # range(0, 9, 3) gives: 0, 3, 6

        # state[i:i+3] means:
        # start from index i
        # go up to (but not including) i+3

        # Example:
        # i = 0 → state[0:3] → [1, 2, 3]
        # i = 3 → state[3:6] → [4, 5, 6]
        # i = 6 → state[6:9] → [7, 8, 0]

        print(state[i:i+3])  # prints one row (3 elements)

    print()  # empty line for spacing


# -------------------------------
# Main Execution
# -------------------------------

solution = solve(start)

if solution:
    print("Solution Found!\n")

    for step in solution:
        print_puzzle(step)

    print("Total Moves:", len(solution) - 1)

else:
    print("No Solution")