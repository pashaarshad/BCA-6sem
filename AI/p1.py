#1. Write a program to implement breadth first search using python.

g={
        'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':['F'],
        'F':[]


    }

v = []
q = []

def bfs(v,g,n):
    v.append(n)
    q.append(n)

    while q:
        s=q.pop(0)
        print(s,end="")

        for n in g[s]:
            if n not in v:
                v.append(n)
                q.append(n)


bfs(v,g,'A')
