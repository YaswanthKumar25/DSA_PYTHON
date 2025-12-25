#Largest Element in Array
#Brute
# The code snippet `arr=[3,5,4,2,1] arr.sort() print(arr[-1])` is finding the largest element in the
# array `arr` using a brute force approach.
arr=[3,5,4,2,1]
arr.sort()
print(arr[-1])

# The code snippet is finding the largest element in the array `arr` using an optimal approach. It
# initializes a variable `largest` with the first element of the array. Then, it iterates through the
# array and compares each element with the current largest element. If the current element is greater
# than the current largest element, it updates the `largest` variable to the current element. Finally,
# it prints the largest element found in the array.
#Optimal
arr=[3,5,4,2,1]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)

# The code snippet is finding the second largest element in the array `arr` using a brute force
# approach. Here's a breakdown of the code:
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

# The code snippet you provided is finding the second largest element in the array `arr` using a
# better approach compared to the brute force method. Here's a breakdown of the code:
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

# The code snippet you provided is finding the second largest element in the array `arr` using an
# optimal approach. Here's a breakdown of the code:
#optimal
arr=[3,5,4,2,1,5,6]
largest=arr[0]
Slargest=-1
for i in range(len(arr)):
    if arr[i]>largest or arr[i]!=largest and arr[i]>Slargest:
        Slargest=largest or arr[i]
        largest=arr[i]
print(Slargest)

    # The function checks whether an array is sorted in ascending order or not.
    # :param arr: The `arr` parameter is a list of numbers that you want to check if it is sorted or not.
    # In the provided code snippet, the function `fun` takes an array `arr` as input and checks if the
    # elements in the array are sorted in non-decreasing order. If the array
    # :return: "It is a Sorted Array"
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