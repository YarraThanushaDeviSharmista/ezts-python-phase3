def fact(n):
    if n==1:
        print("done")
        return
    else:
        fact(n-1)
        print("hi")
fact(4)
#recursion based