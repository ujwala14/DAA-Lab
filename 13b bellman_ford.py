def bf(graph,start,nv):
    m=[999 for x in range(nv)]
    m[start]=0

    for i in range(nv-1):
        for e in graph:
            u,v,c=e[0],e[1],e[2]
            m[v]=min(m[v] , m[u]+c)
    print(m)
    print("Shortest paths :-")
    for i in range(nv):
        if start!=i:
            print("{0} -> {1} cost: {2}".format(start,i,m[i]))

nv=int(input("Enter no. of vertices: "))
ne=int(input("Enter no. of edges: "))

graph=[]
print("Enter edges (u,v,w): ")
for i in range(ne):
    e=[int(x) for x in input("Edge {0}: ".format(i+1)).split()]
    graph.append(e)

#graph=[[0, 1, -4], [1, 3, -1], [1, 4, -2], [3, 0, 6], [3, 5, 4], [4, 5, 2], [4, 2, -3], [2, 1, 8], [2, 5, 3], [0, 5, -3]]
print(graph)

start=int(input("start? "))
bf(graph,start,nv)
