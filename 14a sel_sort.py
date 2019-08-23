import random,time

def sel_sort(arr,n):
    for i in range(n-1):
        sm=i
        for j in range(i+1,n):
            if arr[j]<arr[sm]:
                sm=j
        arr[i],arr[sm] = arr[sm],arr[i]

n=int(input("Enter n: "))
arr=[random.randint(1,1000) for x in range(n)]
print("the list: ",arr)

s=time.clock()
sel_sort(arr,n)
e=time.clock()

print("The sorted list: ",arr)
print("time: ",e-s)
