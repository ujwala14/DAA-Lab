n=int(input("Enter no. of intervals: "))
s,f,v=[0],[0],[0]

print("Enter start time, end time and value of ")
for i in range(n):
    [si,fi,vi]=[int(x) for x in input("Interval {0}: ".format(i+1)).split()]
    s.append(si)
    f.append(fi)
    v.append(vi)

#pred
p=[0,0]
for i in range(2,n+1):
    j=i-1
    while f[j]>s[i] and j>0:
        j-=1
    p.append(j)
print(s,f,v,p)


#iter-opt-compute
m=[0]
for i in range(1,n+1):
    m.append(max(m[i-1] , v[i]+m[p[i]]))
print(m)
print("Max profit: ",m[n])

#find_soln
j=n
print("Intervals selected: ")
while j>0:
    if v[j]+m[p[j]] > m[j-1]:
        print(j,end="  ")
        j=p[j]
    else:
        j=j-1
print()
