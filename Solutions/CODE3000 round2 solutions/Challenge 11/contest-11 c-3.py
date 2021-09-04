import math
import random
while(1):
    arr=[]
    n,q=input().split(" ")
    for i in range(int(n)):
        arr.append(69)
    print(" ".join(list(map(str,arr))))
    for i in range(int(q)):
        ans=0
        a=list(map(int,input().split(" ")))
        if(a[0]==2):
            for i in range(a[1]-1,a[2]):
                ans=ans+(arr[i]%(math.gcd(a[3],a[4])))
            print(ans)
        else:
            arr[a[1]-1]=a[2]
