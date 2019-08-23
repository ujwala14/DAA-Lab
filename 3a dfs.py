def dfs(graph,start):
    visited[start]=1
    print(start,end='  ')
    for w in graph[start]:
        if visited[w]==0:
            dfs(graph,w)

nv=int(input("Enter no. of vertices: "))
ne=int(input("Enter no. of edges: "))

graph=[[] for x in range(nv)]
print("The vertices: ",list(range(nv)))
for i in range(ne):
    u,v=input("Enter edge (u,v):").split()
    graph[int(u)].append(int(v))
    graph[int(v)].append(int(u))

print(graph)

#graph=[[1, 2, 3], [0, 2, 4], [0, 1, 4], [0, 4], [1, 2, 3]]
visited=[0 for x in range(nv)]
start=int(input("Enter start vertex: "))
print("DFS traversal: ")
dfs(graph,start)
print()
