c=0
def fib(n):
    global c
    if n<=1:
        c+=1
        return n
    c+=1
    return fib(n-1)+fib(n-2)
n=10
print(fib(n),c)
#tab