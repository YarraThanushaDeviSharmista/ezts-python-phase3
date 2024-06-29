def fib(n,memo):
    if n<=1:
        return n
    if memo[n]!=-1:
        return memo[n]
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
n=5
memo=[-1]*n+1
memo[0]=0
memo[1]=1
print(fib(n,memo))
#top-down approach
#dp recursion
