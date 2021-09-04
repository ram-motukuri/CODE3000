while(1):
    import math
    r=int(input())
    h=int(input())
    n=int(input())
    m=int(input())
    k=m/(math.pi*r*r)
    if(n<k):
        ans=(h/(k-n))
        print(ans)
        print(math.ceil(ans))
    else:
        print(n,k)
        print("Impossible")
