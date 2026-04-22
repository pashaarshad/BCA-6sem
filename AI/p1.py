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

        for nib in g[s]:
            if nib not in v:
                v.append(nib)
                q.append(nib)


bfs(v,g,'A')
