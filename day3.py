#print all divisors
n=36
for i in range(1,n+1):
    if n % i ==0:
        print(i)

#check prime number
n=11
cnt=0
for i in range(1,n+1):
    if n % i == 0:
        cnt+=1
if cnt == 2:
    print("prime number")
else:
    print("not a prime number")

#GCD & HCF
a=52
b=10
while a > 0 and b > 0:
    if a >b:
        a= a % b
    else:
        b= b % a
if a == 0:
    print(b)
else:
    print(a)  
