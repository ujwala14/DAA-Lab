def find_items(m,n,w,cap):
    i=n
    k=cap
    print("Items chosen: ")
    while i>0 and k>0:
        if m[i][k] != m[i-1][k]:
            print(i,end="  ")
            k=k-w[i]
        i-=1
    print()

def knap(n,w,v,cap):
    m=[[0 for x in range(cap+1)] for y in range(n+1)]
    print(m)
    for i in range(1,n+1):
        for j in range(1,cap+1):
            if w[i]>j:
                m[i][j]=m[i-1][j]
            else:
                m[i][j]=max(m[i-1][j],v[i]+m[i-1][j-w[i]])
    print(m)
    find_items(m,n,w,cap)
    print("Max profit/value: ",m[n][cap])

n=int(input("Enter no. of items: "))
w,v=[0],[0]
print("Enter weight and value for")
for i in range(n):
    wi,vi=input("Item {0}: ".format(i+1)).split()
    w.append(int(wi))
    v.append(int(vi))
print(w,v)
cap=int(input("Enter capacity: "))

knap(n,w,v,cap)
