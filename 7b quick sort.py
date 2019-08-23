def quick_sort(a,low,high):
    if low<=high:
        ip=part(a,low,high)
        p=a[ip]
        quick_sort(a,low,ip-1)
        quick_sort(a,ip+1,high)

def part(a,low,high):
    pivot=a[high]
    i=low-1
    for j in range(low,high):
        if a[j]<=pivot:
            i+=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1

import random,time
n=int(input("Enter no: "))
arr=[random.randint(1,1000) for x in range(n)]

print("The list: ",arr)
s=time.clock()
quick_sort(arr,0,len(arr)-1)
e=time.clock()

print("The sorted list: ",arr)
print("Time: ",e-s)
