from itertools import permutations
def permf(a):
    if len(a)==0:
        return []
    if len(a)==1:
        return [a]
    b=[]
    for i in range(len(a)):
        m=a[i]
        rem=a[:i]+a[i+1:]
        for p in permf(rem):
            b.append([m]+p)
    return b


nv=int(input("Enter no. of nodes: "))
ne=int(input("Enter no. of edges: "))

# graph=[[-1 for c in range(nv)] for r in range(nv)]
# print("Enter edge(u,v,w): ")
# for i in range(ne):
#     [u,v,w]=[int(x) for x in input("Edge {0}: ".format(i+1)).split()]
#     graph[u][v]=graph[v][u]=w

graph=[[-1, 2, -1, 12, 5], [2, -1, 4, 8, -1], [-1, 4, -1, 3, 3], [12, 8, 3, -1, 10], [5, -1, 3, 10, -1]]
print(graph)

start=int(input("Start? "))
other_nodes=list(range(nv))
other_nodes.remove(start)
print(other_nodes)

#perm=list(permutations(other_nodes))
perm=permf(other_nodes)
print(perm)

min_cost=999
best_path=[]
for p in perm:
    cur_cost=0
    path=[start]
    flag=0
    for i in p:
        last=path[-1]
        if graph[last][i]==-1:
            flag=1
            break
        cur_cost+=graph[last][i]
        path.append(i)

    if flag==0 and graph[path[-1]][start]!=-1:
        cur_cost+=graph[path[-1]][start]
        path.append(start)
        print(cur_cost,path)
        if cur_cost<min_cost:
            min_cost=cur_cost
            best_path=path

print("--")
print(min_cost,best_path)
print("Best Path: ")
for i in range(nv):
    print(best_path[i],end=' -> ')
print(start)
print("min cost: ",min_cost)
