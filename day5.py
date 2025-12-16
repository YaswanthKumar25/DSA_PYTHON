#problem statement:-
#Given a number n,calculate the sum of numbers from 1 to n using recursion
#input n=3
#output: 6
#(1 + 2 + 3 = 6)

#Method 1
def fun(i,total):
    if i < 1:
        return total
    total+=i
    return fun(i-1,total)
n=3
print(fun(n,0))

#Method 2
def fun(i):
    if i == 0:
        return 0
    return i + fun(i-1)
print(fun(3))








#problem statement:-
#Given an array you should reverse a array and return it
#Method 1 using two pointers
def reve(i,n,arr):
    if i >= n :
        return arr
    arr[i],arr[n]=arr[n],arr[i]
    return reve(i+1,n-1,arr)
arr=[1,2,3,4,5]
n=len(arr)
print(reve(0,n-1,arr))

#Method 2 
def reve(i,n,arr):
    if i >= n//2:
        return arr
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    return reve(i+1,n,arr)
arr=[1,2,3,4,5]
n=len(arr)
print(reve(0,n,arr))
