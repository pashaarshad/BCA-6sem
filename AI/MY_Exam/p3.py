s = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

g = [
    1,2,3,
    4,5,6,
    7,8,0
]

moves = {
     0:[1,3],
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
    q =[]

    v.append(s)
    q.append((s,[]))

    while q:
        current , path = q.pop(0)

        if current == g:
            return path + [current]
        
        z_i = current.index(0)

        for move in moves[z_i]:
            n_s = current.copy()

            n_s[z_i],n_s[move] = n_s[move],n_s[z_i]

            if n_s not in v:
                v.append(n_s)
                q.append((n_s,path + [current]))

    return None


def p_puzzle(s):

    for i in range(0,9,3):
        print(s[i:i+3])

    print()

sol = sol(s)

if sol:
    print("Solution Found \n")

    for step in sol:
        p_puzzle(step)

    print("Total Moves :",len(sol)-1)

else:
    print("No solution")

