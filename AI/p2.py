g={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
v = set()

def dfs(v,g,n):
    if n not in v:
        print(n,end="")
        v.add(n)
        
        for n in g[n]:
            dfs(v,g,n)

dfs(v,g,'A')