def dijk(graph,start,nv):
    d=[999 for x in range(nv)]
    d[start]=0
    q=[[0,start]]

    while q:
        q.sort()
        [len,u]=q.pop(0)
        for v in range(nv):
            if d[u]+graph[u][v] < d[v]:
                d[v]=d[u]+graph[u][v]
                q.append([d[v],v])

    print(d)
    for i in range(nv):
        if i!=start:
            print("{0} -> {1} cost: {2}".format(start,i,d[i]))

nv=int(input("Enter no. of vertices: "))
ne=int(input("Enter no. of edges: "))

graph=[[999 for c in range(nv)] for r in range(nv)]
for i in range(nv):
    graph[i][i]=0

print("Enter edges (u,v,cost): ")
for i in range(ne):
    u,v,w=input("Edge {0} : ".format(i+1)).split()
    graph[int(u)][int(v)]=int(w)
    graph[int(v)][int(u)]=int(w)

print(graph)
#graph=[[0, 10, 999, 999, 100], [10, 0, 50, 999, 999], [999, 50, 0, 20, 10], [999, 999, 20, 0, 60], [100, 999, 10, 60, 0]]

start=int(input("Start? "))
dijk(graph,start,nv)
