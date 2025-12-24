def quicksort(arr,low,high):
    if low > high:
        return
    partion=qsort(arr,low,high)
    quicksort(arr,low,partion-1)
    quicksort(arr,partion+1,high)

def qsort(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i <j:
        while arr[i]<=pivot and i <=high-1:
            i+=1
        while arr[j]>pivot and j >=low+1:
            j-=1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
arr=[9,4,2,5,6,3,1,7,8]
n=len(arr)
quicksort(arr,0,n-1)
print(arr)