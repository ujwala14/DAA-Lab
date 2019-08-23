def prims(graph,start,nv):
    s=[start]
    vert=list(range(nv))
    t=[]

    while sorted(s)!=vert:
        mx,my,mv=-1,-1,999
        for u in s:
            for v in vert:
                if v not in s and graph[u][v]<mv:
                    mx,my,mv = u,v,graph[u][v]
        t.append([mx,my,mv])
        s.append(my)
    #print("--",t)
    min_cost=0
    for e in t:
        print("{0} -> {1} cost: {2}".format(e[0],e[1],e[2]))
        min_cost+=e[2]
    print("min cost: ",min_cost)

nv=int(input("Enter no. of vertices: "))
ne=int(input("Enter no. of edges: "))

graph=[[999 for c in range(nv)] for r in range(nv)]
for i in range(nv):
    graph[i][i]=0

print("Enter the edges (u,v,w-cost): ")
for i in range(ne):
    [u,v,w]=[int(x) for x in input("Edge {0}: ".format(i+1)).split()]
    graph[u][v]=graph[v][u]=w

print(graph)
#graph=[[0, 4, 999, 8, 999], [4, 0, 3, 1, 999], [999, 3, 0, 7, 8], [8, 1, 7, 0, 3], [999, 999, 8, 3, 0]]

start=int(input("Start? "))
prims(graph,start,nv)
