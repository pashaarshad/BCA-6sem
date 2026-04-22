g={
    'A':['B','C'],
    'B':['D','E'],
    'C':[],
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
            if nib  not in v :
                q.append(nib)
                v.append(nib)

bfs(v,g,'A')

