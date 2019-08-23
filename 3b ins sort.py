import random,time

def ins_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while arr[j]>temp and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

n=int(input("Enter no. of elements: "))
arr=[random.randint(1,1000) for x in range(n)]
print("The elements: \n",arr)

start=time.clock()
ins_sort(arr)
end=time.clock()

print("The sorted elements:\n",arr)
print("Time taken: ",end-start,"s")
