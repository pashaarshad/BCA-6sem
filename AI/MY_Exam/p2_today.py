g = {
        'A':['B','C'],
        'B':['D','E'],
        'C':[],
        'D':[],
        'E':['F'],
        'F':[]
    }
v = set()

def dfs(v,g,n):
    if n not in v:
        v.add(n)
        print(n,end="")

        for nib in g[n]:
            dfs(v,g,nib)

dfs(v,g,'A')

