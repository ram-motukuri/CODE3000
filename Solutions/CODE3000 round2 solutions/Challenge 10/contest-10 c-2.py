def maxev(a,d):
    k=list(sorted(zip(a,d)))
    j=0
    m=max([u+v for u,v in k])
    dp=[0]*(m+1)
    for i in range(1,m+1):
        dp[i]=max(dp[i-1],dp[i])
        while(j<len(k) and k[j][0]==i):
            dp[i+k[j][1]]=max(dp[i+k[j][1]],dp[i]+1)
            j=j+1
    return dp[-1]
while(1):
    n=int(input())
    a=list(map(int,input().split(" ")))
    d=list(map(int,input().split(" ")))
    print(maxev(a,d))
