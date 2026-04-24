s = [
    1,2,3,
    4,8,6,
    7,5,0
]
g = [
    1,2,3,
    4,5,6,
    7,8,0
]

moves = {
     0:[1,2],
     1:[0,2,4],
     2:[1,5],
     3:[0,4,6],
     4:[3,1,5,7],
     5:[4,2,8],
     6:[3,7],
     7:[6,4,8],
     8:[7,5]
}

def sol(s):
     v = []
     q = []

     v.append(s)
     q.append((s,[]))
     while q:
        current, path = q.pop(0)

        if (current == g):
           return path  + [current]
        zero_index = current.index(0)

        for  move in moves[zero_index]:
           new_state = current.copy()

           new_state[zero_index],new_state[move] = new_state[move],new_state[zero_index]
           
           if new_state not in v:
               v.append(new_state)
               q.append((new_state,path+[current]))

     return None  

def print_puzzle(state):
    # state is a list like [1,2,3,4,5,6,7,8,0]

    for i in range(0, 9, 3):
        # range(0, 9, 3) gives: 0, 3, 6

        # state[i:i+3] means:
        # s from index i
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

solution = sol(s)

if solution:
    print("Solution Found!\n")

    for step in solution:
        print_puzzle(step)

    print("Total Moves:", len(solution) - 1)

else:
    print("No Solution")

       
