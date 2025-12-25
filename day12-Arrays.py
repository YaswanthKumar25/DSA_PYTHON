#Largest Element in Array
#Brute
arr=[3,5,4,2,1]
arr.sort()
print(arr[-1])

#Optimal
arr=[3,5,4,2,1]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)

#Second Largest
#Brute
arr=[3,5,4,2,1]
n=len(arr)
arr.sort()
largest=arr[n-1]
Slargest=-1
for i in range(n-1,-1,-1):
    if arr[i] != largest:
        Slargest=arr[i]
        break
print(Slargest)

#Better
arr=[3,5,5,4,2,1]
largest=arr[0]
Slargest=-1
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
for i in range(len(arr)):
    if arr[i]>Slargest and arr[i]!=largest:
        Slargest=arr[i]
print(Slargest)

#optimal
arr=[3,5,4,2,1,5,6]
largest=arr[0]
Slargest=-1
for i in range(len(arr)):
    if arr[i]>largest or arr[i]!=largest and arr[i]>Slargest:
        Slargest=largest or arr[i]
        largest=arr[i]
print(Slargest)

#Check Array is Sorted or Not
def fun(arr):
    n=len(arr)
    for i in range(1,n):
        if arr[i] >= arr[i-1]:
            continue
        else:
            return("Is not Sorted")
    return("It is a Sorted Array")
arr=[3,5,4,2,1]
arr1=[1,2,3,4,5]
print(fun(arr1))