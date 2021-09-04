while(1):
    p=float(input())
    n=int(input())
    m=int(input())
    x=n//m
    x=1/x
    ans=1-(1-p)**x
    print(round(ans,4))
