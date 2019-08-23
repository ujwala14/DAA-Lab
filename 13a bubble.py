import random,time

def bub_sort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

n=int(input("Enter no: "))
arr=[random.randint(1,1000) for x in range(n)]
print("The list: ",arr)

s=time.clock()
bub_sort(arr,n)
e=time.clock()

print("The sorted array: ",arr)
print("Time: ",e-s)
