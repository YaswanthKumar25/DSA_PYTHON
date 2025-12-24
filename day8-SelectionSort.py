arr=[13,46,24,52,9]
n=len(arr)
for i in range(n-1):
    mini=i
    for j in range(i,n):
        if arr[j]<arr[mini]:
            mini=j
            arr[mini],arr[i]=arr[i],arr[mini]
print(arr)
#output:-[9, 13, 24, 46, 52]