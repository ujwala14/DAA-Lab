def bfs(graph,start):
    visited[start]=1
    q=[start]
    print(start,end="  ")
    while q:
        v=q.pop()
        for w in graph[v]:
            if visited[w]==0:
                visited[w]=1
                q.append(w)
                print(w,end="  ")

nv=int(input("Enter no. of vertices: "))
ne=int(input("Enter no. of edges: "))

graph=[[] for x in range(nv)]
visited=[0 for x in range(nv)]
print("The vertices: ",list(range(nv)))
print("Enter edges (u,v): ")
for i in range(ne):
    u,v=input("Edge {0}: ".format(i+1)).split()
    graph[int(u)].append(int(v))
    #graph[int(v)].append(int(u))
print(graph)
start=int(input("start: "))

#graph = [[1, 2, 3], [0, 2, 4], [0, 1, 4], [0, 4], [1, 2, 3]]
print("BFS traversal: ")
bfs(graph,start)
