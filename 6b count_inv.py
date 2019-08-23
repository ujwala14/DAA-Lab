import random,time

def sort_count(a):
    if len(a)==1:
        return 0,a
    half=len(a)//2
    b=a[:half]
    c=a[half:]
    rb,b = sort_count(b)
    rc,c = sort_count(c)
    ra,a = merge_count(b,c)
    return ra+rb+rc , a

def merge_count(a,b):
    i,j=0,0
    count=0
    x=[]
    while i<len(a) and j<len(b):
        if b[j]<a[i]:
           count+=len(a)-i
           x.append(b[j])
           j+=1
        else:
            x.append(a[i])
            i+=1
    if i==len(a):
        x.extend(b[j:])
    else:
        x.extend(a[i:])
    return count,x

n=int(input("Enter n: "))
arr=[random.randint(1,100) for x in range(n)]
#arr=[11,6,12,5,14,22,2,4,17,1]
print("The list: ",arr)
ci,a=sort_count(arr)
print("The sorted list: ",a)
print("No. of inversions: ",ci)
