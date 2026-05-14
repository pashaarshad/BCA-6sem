start = [1,2,3,
         4,0,6,
         7,5,8]

goal = [ 1,2,3,
         4,5,6,
         7,8,0]

index_v=[0,1,2,
         3,4,5,
         6,7,8]
moves={
    0:[1,3],
    1:[0,4,2],
    2:[1,5],
    3:[0,4],
    4:[1,3,7,5],
    5:[2,4,8],
    6:[3,7],
    7:[6,4,6],
    8:[5,7]

    }

def solve(start):
    v = []
    q = []

    v.append(start)
    q.append((start, []))

    while q:

        current , path = q.pop(0)

        if current == goal:
            return path+[current]

        zero_index = current.index(0)

        for move in moves[zero_index]:
            new_state = current.copy()
            new_state[move],new_state[zero_index] = new_state[zero_index],new_state[move]

            if new_state not in v:
                v.append(new_state)
                q.append((new_state, path + [current]))

       
    return None

def print_steps(start):
    for i in range(0,9,3):
        print(start[i:i+3])
    print()

sol = solve(start)

if sol:
    print("Solution FOund")

    for step in sol:
        print_steps(step)
    print("Total Number of step",len(sol)-1)
else :
    print("Not found")

            

            




