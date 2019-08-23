import random,time

def ins_sort(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp

def bucket_sort(a,n):
    b=[[] for x in range(n) ]
    for i in range(n):
        index=int(n*a[i])
        b[index].append(a[i])
    c=[]
    for i in range(n):
        ins_sort(b[i])
        c+=b[i]
    return c

n=int(input("Enter no:"))
arr=[round(random.uniform(0,1),4) for x in range(n)]
print("the list: ",arr)

s=time.clock()
arr=bucket_sort(arr,n)
e=time.clock()

print("the sorted list: ",arr)
print("time: ",e-s)
