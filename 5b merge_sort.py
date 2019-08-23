import random,time

def merge_sort(a):
    if len(a)>1:
        half=len(a)//2
        b=a[:half]
        c=a[half:]
        merge_sort(b)
        merge_sort(c)
        merge(b,c,a)

def merge(b,c,a):
    i,j,k=0,0,0
    while i<len(b) and j<len(c):
        if b[i]<c[j]:
            a[k]=b[i]
            i+=1
        else:
            a[k]=c[j]
            j+=1
        k+=1
    if i==len(b):
        a[k:]=c[j:]
    else:
        a[k:]=b[i:]

n=int(input("Enter no: "))
arr=[random.randint(1,1000) for x in range(n)]

print("the list: ",arr)
s=time.clock()
merge_sort(arr)
e=time.clock()

print("the sorted list: ",arr)
print("time: ",e-s,"s")
