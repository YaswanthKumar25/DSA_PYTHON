#reverse a number
n=77890
rev=0
while n >0:
    last=n%10
    rev=rev*10+last
    n=n//10
print(rev)

#problem statement:-  Check palindrome or not
n=121
original=n
rev=0
while n >0:
    last=n%10
    rev=rev*10+last
    n=n//10
if rev==original:
    print("palindrome")
else:
    print("not palindrome")

#check armstrong num
n=371
k=len(str(n)
original=n
sum1=0
while n>0:
    last=n%10
    sum1+=last**k
    print(sum1)
    n=n//10
if sum1 == original:
    print("armstrong number")
else:
    print("not a armstrong number")