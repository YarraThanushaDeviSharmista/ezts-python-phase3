count=1
def tabulation(n):
    if n<=0:
        return n
        return
    dp=[0]*(n+1)
    dp[1]=1
    global count
    for i in range(2,n+1):
        count+=1
        dp[i]=dp[i-2]+dp[i-1]
    return dp
print(tabulation(10),count)
#fibonacci series in tabulation 
