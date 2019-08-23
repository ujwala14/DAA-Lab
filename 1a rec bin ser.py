import random
import time

def bin_search(a,k,l,h):
    if l<=h:
        m=(l+h)//2
        if a[m]==k:
            return m
        elif k>a[m]:
            return bin_search(a,k,m+1,h)
        else:
            return bin_search(a,k,l,m-1)
    return -1

n=int(input("Enter no. of elements: "))
arr=[random.randint(1,1000) for x in range(n)]
arr.sort()

print("The elements: ",arr)
key=int(input("Enter key: "))

start=time.clock()
res=bin_search(arr,key,0,n-1)
end=time.clock()

if res==-1:
    print("Not found!")
else:
    print("found at pos : ",res+1)
print("time complexity: ",end-start,'s')
