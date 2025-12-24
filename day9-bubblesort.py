# Bubble Sort
arr=[13,24,9,52,46,20]
n=len(arr)
for i in range(n-1,0,-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

# Selection sort
arr=[13,24,9,52,46,20]
n=len(arr)
for i in range(n):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)