#print name N time
def fun(n):
    if n > 5:
        return
    print("yaswanth")
    n+=1
    fun(n)
n=1
fun(n)
#print 1 to n
def fun(n):
    if n >5:
        return
    print(n)
    n+=1
    fun(n)
n=1
fun(n)
#print n to 1
def fun(n):
    if n<0:
        return
    print(n)
    n-=1
    fun(n)
n=5
fun(n)
#print 1 to n by backtrack
def fun(n):
    if n < 0:
        return
    fun(n-1)
    print(n)

n=5
fun(n)