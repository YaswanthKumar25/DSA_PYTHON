#extracting a number
n=7789
while n >0:
    last=n%10
    print(last)
    n=n//10

#problem statemnet:-

'''given the number 'n'.find out and return the number
of digits present in a number'''

n=156
cnt=0
while n >0:
    last=n%10
    cnt+=1
    n=n//10
print(cnt)