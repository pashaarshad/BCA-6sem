g={
    'A':['B','C'],
    'B':['D','E'],
    'C':[],
    'D':[],
    'E':['F'],
    'F':[]
   
}
v = set()
def dfs(v,g,n):
    v.add(n)
    print(n,end=" ")

    for n in g[n]:
        if n not in v:
            dfs(v,g,n)


dfs(v,g,'A')
